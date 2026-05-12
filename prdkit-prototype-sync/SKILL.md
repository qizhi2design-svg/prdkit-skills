---
name: prdkit-prototype-sync
description: 当用户要求把 prototype 反哺到 PRD、把原型更新同步回需求文档、把 mark 内容沉淀到指定 PRD、根据原型修订具体需求描述、补原型链接、生成 PRD 修订记录时使用。该 skill 通过 prdkit CLI 定位目标 PRD 和 prototype，读取 marks，识别 PRD 中实际对应的需求章节，对比现有内容差异，并把修订结果直接写回 PRD。
allowed-tools:
  - Read
  - Grep
  - Glob
  - LS
  - Bash(command -v prdkit)
  - Bash(prdkit info*)
  - Bash(prdkit prd list*)
  - Bash(prdkit prd check*)
  - Bash(prdkit prototype list*)
  - Bash(prdkit prototype mark list*)
  - Bash(prdkit prototype mark get*)
  - Bash(prdkit prototype release link*)
  - Bash(prdkit prd checkpoint*)
  - Edit
  - MultiEdit
  - Write
---

# 将 Prototype 反哺到 PRD

## 核心原则

- **纯产品视角**：全程使用产品经理的语言。写入 PRD 的内容只关注"用户能做什么"、"系统如何响应"，不描述"界面长什么样"。禁止出现 UI 组件名称（按钮、输入框、弹窗等）、样式属性（颜色、宽度、字体等）和技术实现词汇（API 调用、前端框架等）
- **结果导向**：所有 CLI 命令和文件操作在后台执行，用户只看到更新后的 PRD 内容和修订记录
- **不引外部**：最终输出中不引用外部文档或链接
- **一次成功**：命令参数必须完整准确，原型路径、标注 ID 等参数确认无误后再执行，避免 CLI 报错

## 目标

把指定 prototype 的最新结构和标记内容沉淀回指定 PRD，并留下明确的修订痕迹：

1. 定位目标 PRD
2. 定位目标 prototype
3. 收集 prototype 链接和所有 mark 内容
4. 更新 PRD 中实际对应的需求描述章节
5. 把标注信息沉淀为功能说明、操作流程、约束条件或待确认事项
6. 对比本次回写前后的文档差异
7. 在 PRD 中追加修订记录

## 渐进加载原则

不要一次性读取全部参考资料。按阶段加载：

1. 阶段 0：
   - [references/workflow.md](references/workflow.md)
2. 阶段 1：
   - [references/requirement-sync-contract.md](references/requirement-sync-contract.md)
3. 阶段 2：
   - [references/revision-log-template.md](references/revision-log-template.md)

## 工作流程

### 阶段 0：定位 PRD 与 Prototype

1. 从项目根目录开始，先检查 `prdkit` 与项目状态：
   - `command -v prdkit`
   - `prdkit info`
2. 定位目标 PRD：
   - 优先使用用户提供的标题、文件名或路径：

```bash
prdkit prd check "<target-prd>"
```

   - 如果用户没说清楚，先执行：

```bash
prdkit prd list
```

3. 定位目标 prototype：
   - **如果用户提供了云端 release URL**，优先用 resolve 解析：

```bash
prdkit prototype release link resolve "<url>"
```

   - 返回的 `prototypePaths` 即为关联的本地原型路径列表
   - 若本地未命中，会自动从后端拉取并缓存
   - **如果用户给了本地 prototype 路径**，直接使用
   - **如果用户没给**，执行：

```bash
prdkit prototype list
```

   再根据 PRD 内容、标题和上下文选择最相关的 prototype，并在输出中说明这个映射是假设还是确认事实。

### 阶段 1：收集原型与标记信息

5. 获取 prototype 下的 marks：

```bash
prdkit prototype mark list --prototype <prototype-path> --json
```

6. 对每个 mark 继续取详情：

```bash
prdkit prototype mark get <mark-id> --prototype <prototype-path> --json
```

7. 生成 prototype 链接——查询 release 链接注册表，取云端 URL：

   ```bash
   prdkit prototype release link list --json
   ```

   根据 `prototypePath` 匹配，取最新的 `releaseUrl`：`https://<host>/projects/<projectId>?releaseId=<releaseId>`
8. 读取目标 PRD 全文，特别关注：
   - `## 7. 功能需求`
   - 页面 / 模块 / 功能说明对应的小节
   - 现有 prototype / 原型链接
   - 现有修订记录

### 阶段 2：生成回写内容

9. 根据 marks 把 prototype 内容整理成 PRD 可读的结构：
   - 页面 / 模块标题
   - prototype 链接
   - 对应标记摘要
   - 提炼出的功能说明
   - 操作流程
   - 业务约束
   - 待确认事项
10. 不要把 mark 原文整段机械粘贴进 PRD，要做归纳：
   - 直接描述页面目标的标注 -> 归入功能说明
   - 描述用户操作和系统响应的标注 -> 归入操作流程
   - 描述边界、限制或说明的标注 -> 归入约束条件 / 风险 / 待确认事项
11. 过滤指标数据：读取标注详情后，识别其中包含的交互指标和技术指标：
   - 可转换为产品/业务指标的（点击率→功能使用率、转化率→任务完成率等），转换后写入
   - 无对应产品/业务指标的（加载时间、缓存命中率等），丢弃不同步
   （详见 [references/requirement-sync-contract.md](references/requirement-sync-contract.md) 中的"指标过滤规则"）
12. 不要假设 PRD 里有固定的 `Feature List` 模块。应先按 [references/requirement-sync-contract.md](references/requirement-sync-contract.md) 识别本次 prototype 最应该回填到哪些现有需求章节：
   - 已有模块 / 页面功能说明小节
   - 已有操作流程小节
   - 已有业务约束 / 流程小节
   - 已有待确认事项 / 开放问题小节
13. 如果 PRD 已经有对应页面或模块的小节，不是整段重写，而是先对比：
   - 新增了哪些功能
   - 更新了哪些功能描述
   - 删除或不再体现哪些内容
14. 把差异整理成”本次修订摘要”，用于修订记录。

### 阶段 3：回写 PRD 与追加修订记录

15. 直接更新目标 PRD：
   - 在最匹配的功能说明章节中新增或更新该 prototype 对应内容
   - 同步 prototype 链接
   - 将标注内容沉淀为结构化需求描述（已过滤交互/技术指标，转换为产品/业务指标）
16. 如果 PRD 没有”修订记录”区域，则创建：
   - 优先放在标题和正文之间
   - 标题使用 `## 修订记录`
17. 按 [references/revision-log-template.md](references/revision-log-template.md) 追加一条修订记录，至少包含：
   - 修订日期
   - 修订人
   - 修订明细
   - 修订明细中需包含来源 prototype、prototype 链接与本次差异摘要
18. 为 PRD 创建 checkpoint 记录本次同步：
   - 运行 `prdkit prd checkpoint create “<PRD路径>” --message “同步 prototype「<原型名称>」— <纯产品语言描述变更>”`
   - checkpoint message 只描述业务功能变化，不出现”标注”、”mark”、”整理了 N 条标注”等工具语言
   - 示例：`同步 prototype「门店知识库」— 补充筛选区与任务列表的功能说明，细化操作流程与约束条件`
19. 修改完成后，向用户汇报：
   - 更新了哪个 PRD
   - 使用了哪个 prototype
   - 沉淀了多少条标注内容
   - 本次修订的功能差异摘要

## 约束规则

- 必须先通过 CLI 定位 PRD 和 prototype，再读文件
- 必须使用 `mark list` + `mark get`，不要跳过标注明细
- 不要把标注原文生硬拼接进 PRD，必须先归纳
- 必须生成或更新 prototype 链接，使用云端 release URL（从 `prototype release link list` 获取）
- 必须对比旧内容和新内容，再写修订记录
- 必须把修订记录写进 PRD，而不是只在回复里说明
- 不要预设固定的 `Feature List` 区块，优先复用 PRD 里现有的具体功能描述结构
- 写入 PRD 的内容必须使用纯产品语言，标注原文若含 UI 组件名称、样式属性、技术术语，必须在写入前转换为功能描述
- 标注中的交互指标（点击率、加载时间等）必须转换为产品/业务指标后写入；无法转换的丢弃不同步
- checkpoint message 必须使用产品语言描述业务功能变化，不得出现内部工具术语
- 如果同一个 PRD 对应多个 prototype，默认一次只同步一个 prototype，除非用户明确要求批量同步

## 产品语言红线

以下词汇在写入 PRD 的内容以及本技能的输出中**禁止出现**：

| 类别 | 禁止词汇 | 应替换为 |
|------|----------|----------|
| UI 组件名 | 按钮、输入框、弹窗、抽屉、标签页、卡片、列表、下拉框、单选、复选、开关、滑块、分页器、面包屑、步骤条、树形控件、日期选择器、穿梭框、上传组件 | 用功能描述代替，如"在此区域…"、"点击此处可以…" |
| 样式属性 | 颜色名（红色、橙色、蓝色、白色等）、宽度、高度、间距、边距、字体、字号、行高、圆角、阴影、边框、背景色、透明度 | 去掉，不描述视觉样式 |
| 技术实现 | CSS 选择器、DOM 路径、API 调用、前端框架、组件库、Vue、React、HTML、class、id、div、span、flex、grid、z-index、数据结构、缓存策略 | 完全禁止出现 |
| 交互指标 | 点击率、转化率、加载时间、渲染时间、响应时长、PV、UV | 转换为产品/业务指标：功能使用率、任务完成率、用户满意度、成功提交率；无法转换的丢弃 |
| 内部标识 | 标注 ID、标注文件名、mark-xxx、mark 数量、文件路径、workspace/prototypes | 完全禁止出现；说"标注内容"而非"marks" |
| 工具术语 | 命令、命令行、参数、终端、bash、`$` 符号、CLI | 完全禁止出现 |

### 内容转换规则

当读取标注的原始内容时，如果原文包含上述禁止词汇，**必须在写入 PRD 前自动转换**：

- ❌ "点击黄色按钮后右侧出现 drawer" → ✅ "点击确认后，右侧展开详情面板"
- ❌ "首屏顶部 tab 栏有 3 个标签页" → ✅ "首屏顶部提供三个切换入口"
- ❌ "列表每行右侧有操作按钮" → ✅ "每条数据配有对应的操作入口"
- ❌ "点击率提升 5%" → ✅ "功能使用率提升 5%（可转换的指标）"
- ❌ "页面加载时间控制在 2 秒内" → ❌ 丢弃（无对应产品/业务指标）

### 描述编写规范

- **只写"做什么"和"为什么"**，不写"怎么做"
  - ✅ "审批通过后，系统自动通知下一节点处理人"
  - ❌ "点击绿色按钮调用审批接口，通过后发送通知"
- **用功能描述代替组件名称**
  - ✅ "用户在此处查看订单状态和物流信息"
  - ❌ "卡片列表展示订单信息和物流状态"
- **关注交互目的而非交互形式**
  - ✅ "从备选列表中选中需要分配的人员"
  - ❌ "左边是待选列表右边是已选列表，中间有穿梭箭头"
- **指标转换示例**
  - ✅ "任务完成率提升至 85%以上"
  - ❌ "点击率提升至 5%以上"
