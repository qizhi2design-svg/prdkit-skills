---
name: prdkit-mark-update
description: 当用户从 viewer 点击已有标注并希望修改时使用。该 skill 解析标注信息，通过 CLI 获取现有内容，结构化提问明确修改内容，然后调用 prdkit mark edit 命令更新标注。
allowed-tools:
  - Bash(prdkit mark get*)
  - Bash(prdkit mark edit*)
  - AskUserQuestion
---

# 修改原型标注

## 工作流程

### 第一阶段：解析和获取标注信息

1. **解析用户提供的标注信息**，通常包含：
   - 项目名称
   - 文件路径（原型目录的绝对路径）
   - DOM 路径（元素的 DOM 层级）
   - **标记文件路径**（已存在的标注文件）

2. **提取关键信息**：
   - 从文件路径提取原型相对路径（相对于 workspace/prototypes/）
   - 从标记文件路径提取 mark ID（文件名去掉 .md 后缀）
   - 例如：`/Users/xxx/workspace/prototypes/admin-demo/marks/mark-1777623767763.md` 
     → 原型路径：`admin-demo`，mark ID：`mark-1777623767763`

3. **获取现有标注内容**：
   ```bash
   prdkit mark get <mark-id> --prototype <原型路径> --json
   ```
   - 解析 JSON 输出，提取 title 和 description
   - 展示给用户当前的标注内容

### 第二阶段：明确修改内容和变更元数据

4. **使用 `AskUserQuestion` 工具结构化提问**，明确要修改的内容和变更背景：

   **必须明确的维度**：
   
   **A. 修改内容**：
   - **修改类型**：要修改什么？
     - 只修改标题
     - 只修改描述
     - 同时修改标题和描述
   
   - **新的标题**（如果修改标题）：新的标注标题
   
   - **新的描述**（如果修改描述）：新的标注描述内容
   
   **B. 变更元数据**（用于生成详细的 checkpoint 信息）：
   - **变更原因**：为什么要改？
     - 需求变更（产品需求调整）
     - 问题修正（原标注有误）
     - 内容补充（补充遗漏信息）
     - 优化改进（优化表达或结构）
   
   - **变更类型**：这是什么性质的变更？
     - 需求增强（添加新功能点或细节）
     - 需求削减（删除某些功能或降低要求）
     - 需求替换（用新方案替代旧方案）
     - 优先级调整（调整功能优先级）
     - 内容修正（修正错误或不准确的描述）
   
   - **影响范围**：这个变更会影响哪些其他功能或标注？
     - 仅影响当前标注
     - 可能影响相关功能（需要用户说明）
     - 需要同步更新其他标注（需要用户列出）
   
   - **关联信息**（可选）：
     - 关联的 PRD 文档或讨论链接
     - 变更来源（用户反馈、数据分析、竞品分析等）
     - 决策背景或上下文

   提问要点：
   - 展示当前的标题和描述，让用户了解现状
   - 询问用户想要修改哪些部分
   - 收集新的内容
   - **重点询问变更原因和影响范围**
   - 引导用户思考是否需要同步更新其他标注

### 第三阶段：更新标注并记录变更

5. **生成详细的变更说明**（用于 checkpoint message）：
   
   根据用户提供的变更元数据，生成结构化的变更说明：
   ```
   更新标注: [标注标题]
   
   变更类型: [需求增强/需求削减/需求替换/优先级调整/内容修正]
   变更原因: [需求变更/问题修正/内容补充/优化改进] - [具体原因]
   
   变更内容:
   - [具体修改了什么]
   
   影响范围:
   - [影响的其他功能或标注]
   
   关联信息:
   - [PRD 文档链接、变更来源等]
   ```

6. **构建并执行 prdkit mark edit 命令**：
   ```bash
   prdkit mark edit <mark-id> \
     --prototype <原型路径> \
     [--title "<新标题>"] \
     [--desc "<新描述>"]
   ```
   - 只传递需要修改的参数
   - 命令会自动创建 checkpoint，message 使用生成的变更说明
   - 检查命令执行结果

7. **提示用户**：
   - 告知标注已更新
   - 展示变更说明
   - 如果有影响范围，提醒用户检查相关标注
   - 提示可以在 viewer 中查看更新后的标注
   - 说明已创建 checkpoint 并记录了详细的变更信息

## 约束规则

- 必须先使用 `prdkit mark get` 获取现有内容
- 必须使用 `AskUserQuestion` 工具明确修改内容和变更元数据
- 展示当前内容，让用户知道要修改什么
- **必须询问变更原因、变更类型和影响范围**
- 根据变更元数据生成详细的 checkpoint message
- 使用 `prdkit mark edit` 命令更新标注
- 原型路径必须是相对路径（相对于 workspace/prototypes/）
- 如果用户提到影响其他标注，提醒用户同步更新

## 最佳实践

1. **展示现状**：在提问时展示当前的标题和描述
2. **明确修改**：清楚地询问用户要修改哪些部分
3. **精准更新**：只传递需要修改的参数
4. **友好提示**：告知用户更新成功并说明如何查看

## 示例

**用户输入**：
```
项目名: 测试项目
文件路径: /Users/xxx/workspace/prototypes/admin-demo
DOM 路径: body > div.app-shell > div.content-shell > main.workspace > section.panel
标记文件: /Users/xxx/workspace/prototypes/admin-demo/marks/mark-1777623767763.md
```

**Skill 提取信息**：
- 原型路径：`admin-demo`
- Mark ID：`mark-1777623767763`

**Skill 获取现有内容**：
```bash
prdkit mark get mark-1777623767763 --prototype admin-demo --json
```

输出：
```json
{
  "prototype": "admin-demo",
  "mark": {
    "id": "mark-1777623767763",
    "title": "工作区面板",
    "selector": "body > div.app-shell > div.content-shell > main.workspace > section.panel",
    "domPath": "body > div.app-shell > div.content-shell > main.workspace > section.panel",
    "description": "# 工作区面板\n\n## 功能说明\n展示当前工作区的内容",
    "timestamp": 1777623767763
  }
}
```

**Skill 提问**：
```
当前标注内容：
- 标题：工作区面板
- 描述：
  ## 功能说明
  展示当前工作区的内容

要修改什么？
1. 修改类型：
   - A) 只修改标题
   - B) 只修改描述
   - C) 同时修改标题和描述

2. 新的标题（如果修改）：

3. 新的描述（如果修改）：
```

**用户回答**：
- 修改类型：B) 只修改描述
- 新的描述：
  ```
  ## 功能说明
  展示当前工作区的内容，支持多标签页切换
  
  ## 交互行为
  - 点击标签页切换内容
  - 支持拖拽调整面板大小
  ```

**执行命令**：
```bash
prdkit mark edit mark-1777623767763 \
  --prototype admin-demo \
  --desc "## 功能说明
展示当前工作区的内容，支持多标签页切换

## 交互行为
- 点击标签页切换内容
- 支持拖拽调整面板大小"
```

## 注意事项

- 确保正确提取原型路径和 mark ID
- 使用 --json 参数获取结构化的标注数据
- 只传递需要修改的参数（--title 或 --desc）
- 告知用户标注更新后会自动创建 checkpoint
