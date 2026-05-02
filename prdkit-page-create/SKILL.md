---
name: prdkit-page-create
description: 当用户提出创建原型、起原型、生成页面原型、搭建移动端原型、搭建 PC 后台原型，或提到旧称 `create-prototype` 时使用。该 skill 智能判断需求复杂度：对于明确的需求（包含平台类型、页面结构、核心功能）直接创建原型；对于复杂或模糊的需求采用两阶段流程（先生成方案文档等待确认，再创建原型）。优先使用快速模式提升用户体验。
allowed-tools:
  - Read
  - Grep
  - Glob
  - LS
  - AskQuestion
  - Bash(command -v prdkit)
  - Bash(prdkit info*)
  - Bash(prdkit init*)
  - Bash(prdkit prototype create*)
  - Bash(prdkit prototype list*)
  - Bash(prdkit serve*)
  - Bash(npm install -g @huangqz/prdkit-cli*)
  - Bash(rm *)
  - Edit
  - MultiEdit
  - Write
---

# 创建页面原型

## 工作流程

### 智能判断需求复杂度

首先分析用户需求，判断使用哪种工作模式：

**快速模式（直接创建）** - 适用于需求明确的场景：
- ✅ 明确指定了平台类型（移动端、PC后台、Web）
- ✅ 描述了页面的主要结构和元素
- ✅ 说明了核心功能和交互
- ✅ 没有复杂的业务逻辑或特殊要求

**谨慎模式（两阶段流程）** - 适用于复杂或模糊的场景：
- ⚠️ 平台类型不明确
- ⚠️ 页面结构描述模糊
- ⚠️ 涉及复杂的业务流程或数据关系
- ⚠️ 需要与现有原型或PRD对齐
- ⚠️ 用户明确要求先看方案

### 模式 A：快速模式（直接创建）

当需求明确时，直接创建原型：

1. **检查环境和项目状态**：
   - 运行 `command -v prdkit` 和 `prdkit info`
   - 如果需要，安装 CLI 或初始化项目

2. **从用户描述中提取信息**：
   - 平台类型：mobile / admin / web
   - 页面标题
   - 主要元素和布局
   - 核心交互功能

3. **直接创建原型**：
   ```bash
   prdkit prototype create “<title>” --template <platform> --dir ./workspace/prototypes
   ```

4. **补充页面内容**：
   - 根据用户描述补充 HTML 结构
   - 实现核心交互功能（JS）
   - 添加样式（CSS）
   - 创建 mock 数据（mock.js）

5. **创建 checkpoint 并引导预览**：
   - 运行 `prdkit checkpoint create`
   - 启动或提示预览服务器

### 模式 B：谨慎模式（两阶段流程）

当需求复杂或模糊时，采用两阶段流程：

#### 第一阶段：生成方案文档

1. **检查环境和项目状态**：
   - 运行 `command -v prdkit` 和 `prdkit info`
   - 如果需要，安装 CLI 或初始化项目

2. **读取项目上下文**：
   - `context/`、`draft/`
   - 已有 `workspace/prototypes/`
   - 相关的 `workspace/prds/` 或 `workspace/discussions/`

3. **使用 `AskQuestion` 工具确认需求**：
   - 参考 [references/phase-1-requirements.md](references/phase-1-requirements.md)
   - 提出 3-4 个高信息密度问题
   - 优先确认平台类型：`mobile` / `admin` / `web`

4. **生成方案文档**：
   - 保存到 `draft/reference/<title>-prototype-plan.md`
   - 包含：任务清单、已确认信息、当前假设、待确认项
   - 包含：ASCII 线框图、交互说明
   - 包含：视觉样式参数、画布规格
   - 明确标注”当前处于第一阶段，尚未创建页面”

5. **停止并等待用户确认**

#### 第二阶段：创建页面

6. **用户确认方案后，执行创建**：
   ```bash
   prdkit prototype create “<title>” --template <platform> --dir ./workspace/prototypes
   ```

7. **按方案文档补充内容**：
   - 页面结构、交互逻辑、mock 数据
   - 参考 [references/phase-3-implementation.md](references/phase-3-implementation.md)

8. **创建 checkpoint**：
   ```bash
   prdkit checkpoint create
   ```

9. **清理临时文档**：
   - 删除 `draft/reference/<title>-prototype-plan.md`

10. **引导预览**：
    - 检查并启动预览服务器

## 命令映射

- 移动端 App / H5：

```bash
prdkit prototype create "<title>" --template mobile --dir ./workspace/prototypes
```

- PC 后台 / 工作台 / 仪表盘：

```bash
prdkit prototype create "<title>" --template admin --dir ./workspace/prototypes
```

- 通用 Web 页面：

```bash
prdkit prototype create "<title>" --template web --dir ./workspace/prototypes
```

可选补充命令：

```bash
prdkit prototype list
prdkit serve
```

## 方案文档格式

第一阶段的方案记录保存到 `draft/reference/<title>-prototype-plan.md`，复用 references 中的格式模板。

## 约束规则

**模式选择**
- 优先使用快速模式，提升用户体验
- 只在真正需要时才使用谨慎模式
- 如果用户明确要求"先看方案"或"先确认一下"，使用谨慎模式

**流程控制**
- 快速模式：直接创建原型，一步到位
- 谨慎模式：第一阶段必须落盘方案文档并暂停，等用户确认后再继续
- 项目未初始化时，先完成初始化再执行原型命令

**交互要求**
- 快速模式：从用户描述中提取信息，减少提问
- 谨慎模式：必须使用 `AskQuestion` 工具提问
- 任务计划使用 `TodoWrite` 工具呈现
- 问题应短、准、高信息密度，避免宽泛开放式提问

**技术规范**
- 显式指定模板，不依赖默认值
- 默认尺寸：`mobile` 用 `390 x 844`，`admin/web` 用 `1440 x 900`
- 参考 `phase-3-implementation.md` 的画布、圆角、弹窗和 `z-index` 规则
- 页面内部不使用 `z-index: 9999`（预留给 viewer）
- 数据结构：每页一个 `mock.js`，`script.js` 只消费数据
- ASCII 线框图只确认结构，保持简洁易读
- **图片占位**：禁止使用真实图片链接（unsplash、placeholder.com 等），统一使用纯色背景 + 文字标注的方式占位

## 决策树

```
用户需求
    │
    ├─ 需求明确？（平台+结构+功能都清楚）
    │   ├─ 是 → 快速模式 → 直接创建原型
    │   └─ 否 ↓
    │
    ├─ 用户要求先看方案？
    │   ├─ 是 → 谨慎模式 → 两阶段流程
    │   └─ 否 ↓
    │
    ├─ 涉及复杂业务逻辑？
    │   ├─ 是 → 谨慎模式 → 两阶段流程
    │   └─ 否 → 快速模式 → 直接创建原型
```

## 资源说明

### references/

- `phase-1-requirements.md`：需求澄清阶段的提问模板和确认记录格式
- `phase-2-wireframes.md`：结构确认阶段的 ASCII 线框图模板和交互说明要求
- `phase-3-implementation.md`：实现阶段的视觉参数、画布规范、图片占位和 CSS 基准
