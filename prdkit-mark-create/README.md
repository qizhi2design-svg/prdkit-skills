# prdkit-prototype-create-mark Skill

## 概述

当用户从 viewer 点击元素并复制信息后，使用此 skill 创建原型标注。标注用于记录 功能说明、修改说明、验证假设等内容。

## 触发场景

用户提供以下格式的元素信息时触发：

```
项目: 测试项目
文件路径: /Users/xxx/workspace/prototypes/车后本地生活门店知识库
DOM 路径: body > div.app-shell > aside.sidebar > div.brand
```

或包含类似的原型路径和元素信息。

## 工作流程

### 第一阶段：解析元素信息
1. 解析项目名称、文件路径、DOM 路径等信息
2. 从文件路径提取原型的相对路径（相对于 `workspace/prototypes/`）
3. 构建或提取 CSS 选择器

### 第二阶段：明确标注内容
4. 使用 `AskUserQuestion` 工具结构化提问
5. 明确标注类型：
   - **功能说明 说明** - 功能需求、用户价值、验收标准
   - **交互行为说明** - 交互流程、状态变化
   - **数据展示说明** - 数据来源、展示规则
   - **其他** - 其他类型的标注
6. 收集标注标题和详细描述

### 第三阶段：创建标注
7. 构建 `prdkit mark create` 命令
8. 执行命令创建标注文件
9. 提示用户标注已创建，并说明文件位置

## 核心特性

### 1. 智能路径提取
- 自动从绝对路径提取原型相对路径
- 支持多级目录结构（如 `foo/bar/baz`）
- 验证路径格式的正确性

### 2. 结构化提问
- 提供标注类型选项，引导用户选择
- 根据标注类型提供相应的描述模板
- 确保标注内容完整、有价值

### 3. 标注内容模板

提供三种核心标注类型的模板，详见 [references/templates/](references/templates/)：

- [PRD Feature 标注模板](references/templates/prd-feature.md) - 功能需求、用户价值、验收标准
- [交互行为标注模板](references/templates/interaction.md) - 交互流程、状态变化、边界情况
- [数据展示标注模板](references/templates/data-display.md) - 数据来源、展示规则、异常处理

每个模板包含基础版和详细版，根据实际情况选择使用。

### 4. 自动化处理
- 自动转义命令行参数中的特殊字符
- 自动创建 checkpoint 版本快照
- 提供清晰的成功/失败反馈

## 命令参数

### 必需参数
- `--prototype <path>`: 原型相对路径
- `--title <text>`: 标注标题
- `--selector <css>`: CSS 选择器

### 可选参数
- `--dom-path <path>`: DOM 路径
- `--desc <markdown>`: 标注描述
- `--desc-file <file>`: 从文件读取描述

## 使用示例

### 示例 1：PRD Feature 标注

**用户输入**：
```
项目: 测试项目
文件路径: /Users/xxx/workspace/prototypes/dashboard
DOM 路径: body > div.sidebar > nav.menu
```

**Skill 提问**：
```
关于这个元素的标注：

1. 标注类型：
   - A) 功能说明 说明
   - B) 交互行为说明
   - C) 数据展示说明
   - D) 其他

2. 标注标题（一句话概括）：

3. 标注描述（详细说明）：
```

**用户回答**：
- 类型：A) 功能说明 说明
- 标题：侧边导航菜单
- 描述：提供快速访问各功能模块的导航入口

**执行结果**：
```bash
prdkit mark create \
  --prototype "dashboard" \
  --title "侧边导航菜单" \
  --selector "body > div.sidebar > nav.menu" \
  --dom-path "body > div.sidebar > nav.menu" \
  --desc "## 功能说明
提供快速访问各功能模块的导航入口，支持一级和二级菜单

## 交互流程
1. 点击一级菜单展开/收起二级菜单
2. 点击二级菜单跳转到对应页面
3. 当前页面对应的菜单项高亮显示

## 验收标准
- [ ] 菜单项可正常展开/收起
- [ ] 点击跳转正确
- [ ] 当前页面高亮正确"
```

### 示例 2：修改说明标注

**用户输入**：
```
项目: 测试项目
文件路径: /Users/xxx/workspace/prototypes/login
DOM 路径: body > div.form > button.submit
```

**Skill 提问**：
```
关于这个按钮的标注：

1. 标注类型：
   - A) 功能说明 说明
   - B) 交互行为说明
   - C) 数据展示说明

2. 标注标题：

3. 如果是修改项，请说明：
   - 当前问题是什么？
   - 期望的效果是什么？
   - 优先级如何？
```

**用户回答**：
- 类型：B) 待修改项
- 标题：登录按钮缺少加载状态
- 当前问题：点击登录后按钮无反馈，用户不知道是否在处理
- 期望效果：点击后显示加载状态，禁用按钮防止重复提交
- 优先级：P0

**执行结果**：
```bash
prdkit mark create \
  --prototype "login" \
  --title "登录按钮缺少加载状态" \
  --selector "body > div.form > button.submit" \
  --dom-path "body > div.form > button.submit" \
  --desc "## 当前问题
点击登录后按钮无反馈，用户不知道是否在处理请求，可能重复点击

## 期望效果
1. 点击后按钮显示加载状态（loading spinner）
2. 按钮文案改为「登录中...」
3. 禁用按钮防止重复提交
4. 请求完成后恢复正常状态

## 优先级
- [x] P0 - 阻塞上线
- [ ] P1 - 重要但不阻塞
- [ ] P2 - 优化项

## 相关资源
参考其他页面的提交按钮实现"
```

## 标注文件结构

创建的标注文件位于：`workspace/prototypes/<原型路径>/marks/mark-<timestamp>.md`

文件格式：
```markdown
---
title: 标注标题
selector: CSS 选择器
domPath: DOM 路径
timestamp: 时间戳
---
# 标注标题

标注描述内容（Markdown 格式）
```

## 与其他 skill 的关系

| Skill | 用途 | 触发时机 |
|-------|------|---------|
| prdkit-prototype-create-mark | 创建新标注 | 用户复制元素信息并希望添加标注 |
| prdkit-prototype-update-page | 修改页面代码 | 用户希望修改原型的 HTML/JS/CSS |
| prdkit-prototype-create-page | 创建新页面 | 用户希望创建新的原型页面 |

## 最佳实践

1. **标题简洁明确**：用一句话说清楚标注的核心内容
2. **描述结构化**：使用 Markdown 格式，分段落、列表组织
3. **聚焦当前元素**：标注内容应该与选中的元素直接相关
4. **提供上下文**：说明为什么需要这个标注，背景是什么
5. **可操作性**：如果是修改项，要说明具体怎么改
6. **可验证性**：如果是功能需求，要有明确的验收标准

## 注意事项

1. **路径格式**：确保原型路径是相对于 `workspace/prototypes/` 的相对路径
2. **选择器有效性**：CSS 选择器要符合标准格式，能够唯一定位元素
3. **描述质量**：引导用户提供有价值的标注内容，避免空洞的描述
4. **自动 checkpoint**：标注创建后会自动创建版本快照，无需手动操作
5. **命令转义**：处理好描述中的引号、换行符等特殊字符

## 文档结构

```
prdkit-prototype-create-mark/
├── SKILL.md                    # Skill 主文档
├── README.md                   # 本文档
└── references/
    ├── examples.md             # 使用示例
    └── templates/              # 标注内容模板
        ├── README.md           # 模板使用说明
        ├── prd-feature.md      # PRD Feature 标注模板
        ├── interaction.md      # 交互行为标注模板
        └── data-display.md     # 数据展示标注模板
```
