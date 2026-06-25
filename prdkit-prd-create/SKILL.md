---
name: prdkit-prd-create
description: 当产品经理需要撰写产品需求文档（PRD）、整理产品方案、输出需求文档时使用。该 skill 采用两阶段工作方式：先与产品经理充分沟通业务背景、产品目标、需求范围，输出方案稿供确认；确认后再生成结构化的正式 PRD 文档。自动适配不同复杂度的需求场景，确保文档内容完整、重点突出。
allowed-tools:
  - Read
  - Grep
  - Glob
  - LS
  - AskQuestion
  - Bash(command -v prdkit)
  - Bash(prdkit info*)
  - Bash(prdkit init*)
  - Bash(prdkit prd create*)
  - Bash(prdkit prd checkpoint*)
  - Bash(prdkit prd list*)
  - Edit
  - MultiEdit
  - Write
---

# 创建复杂度感知 PRD

## 目标

帮助产品经理高效产出高质量 PRD 文档：

1. **先对齐、再落笔**：先梳理业务背景、产品目标和需求范围，确认方向后再生成正式文档，避免方向性返工
2. **复杂度自适应**：简单调整不冗余、大型变更不遗漏，按需匹配文档详略
3. **类型化适配**：按产品类型（商业化产品 / 企业自研 / 业务型 / 工具型 / 交易型 / 基础服务型）调整文档侧重点，确保内容与业务场景匹配

## 核心原则

- **纯产品视角**：全程使用产品经理的语言。描述需求时只关注”用户能做什么”、”系统如何响应”、”解决什么业务问题”。禁止出现 UI 组件名称、样式属性、技术实现词汇。目标、背景等章节只写产品功能和策略目标，不写交互细节和技术方案

  **❌ 反面示例（在需求文档中禁止出现）：**
  ```
  用户点击”品牌厂商”按钮，展开下拉面板（最大高度320px），在树形复选框中勾选品牌
  新增导入弹窗，包含三步弹窗流程：选品牌→选导入方式→确认导入
  穿梭框左侧显示待添加列表，右侧显示已添加列表
  Tab 切换后操作按钮按规则变化
  ```
  **✅ 正确写法（应使用纯产品语言）：**
  ```
  用户可按品牌或厂商筛选车型，品牌与下属厂商互斥，支持跨品牌多选
  门店管理员可通过 Excel 导入预售车型，系统自动校验并入库
  门店可配置在售车型列表，配置结果集成到 AI 回复策略中
  车型区分已上市/待上市两种状态，不同状态的操作权限不同
  ```

  **判断标准：** 删除所有 UI/交互/技术词汇后，描述是否依然完整表达了业务需求？如果”不”，说明描述方式有问题。
- **先方案后正式**：任何 PRD 工作都先输出方案稿供产品经理确认，确认后才生成正式文档，不在确认前直接写正式 PRD
- **结果导向**：不展示命令构造过程，不让用户看到技术实现细节。所有命令在后台执行，用户只看到结果
- **一次成功**：在运行命令前确保所有参数完整准确，不在用户面前试错

## 渐进加载原则

不要预读全部参考资料。按阶段加载：

1. 阶段 0 只加载：
   - [references/framework/complexity-assessment.md](references/framework/complexity-assessment.md)
   - [references/appendices/product-typing.md](references/appendices/product-typing.md)
2. 阶段 1 写方案稿时补充：
   - [references/question-bank.md](references/question-bank.md)
   - [references/plan-template.md](references/plan-template.md)
   - [references/chapters/chapter-generation.md](references/chapters/chapter-generation.md)
3. 阶段 2 写正式稿时补充：
   - [references/final-prd-sections.md](references/final-prd-sections.md)
   - [references/appendices/selfcheck.md](references/appendices/selfcheck.md)

## 工作流程

### 阶段 0：项目准备、产品定型、复杂度判断

1. 确认 prdkit 环境就绪：
   - 检查 `prdkit` 是否可访问
   - 检查当前目录是否为 prdkit 项目
2. 如果环境未就绪，先完成环境和项目初始化。
3. 在提问前先浏览已有上下文：
   - `context/`
   - `draft/`
   - `workspace/prds/`
   - `workspace/discussions/`
4. 结合 [references/appendices/product-typing.md](references/appendices/product-typing.md) 先推断产品定型：
   - 商业属性：商业化产品 / 企业自研系统
   - 功能类型：业务型管理软件 / 工具型软件 / 交易型平台 / 基础服务型
5. 用一句话向用户确认产品定型：
   - `根据目前上下文，我先按【企业自研系统 × 业务型管理软件】理解，后续会据此调整 PRD 章节侧重点。`
6. 再结合 [references/framework/complexity-assessment.md](references/framework/complexity-assessment.md) 做复杂度判断：
   - 先用一句话从用户视角描述变更
   - 再走 L1-L4 决策树
   - 边界模糊时用辅助信号消歧
7. 向用户确认复杂度等级：
   - `根据描述，这是一个 L3（模块级）需求，我会按标准 PRD 体量组织方案稿。`

### 阶段 1：生成 PRD 方案稿

8. 使用 [references/question-bank.md](references/question-bank.md) 提 3-4 个高信息密度问题，优先补齐：
   - 背景和业务问题
   - 角色与关键场景
   - 范围边界
   - 数据、依赖、风险、验收
9. 结合 [references/chapters/chapter-generation.md](references/chapters/chapter-generation.md) 决定章节适配策略：
   - 低复杂度保留核心章节
   - 高复杂度增加流程、依赖、权限、上线与回滚、自检
   - 按产品类型调整内容重心
10. 按 [references/plan-template.md](references/plan-template.md) 生成并保存：
   - `draft/reference/<title>-prd-plan.md`
11. 方案稿里必须写清：
   - 产品定型及原因
   - 复杂度等级及原因
   - 推荐章节与章节策略
   - 已确认信息
   - 当前假设
   - 待确认 / 开放问题
   - 第二阶段执行命令
12. 第一阶段结束后必须停止，等待用户确认。

### 阶段 2：生成正式 PRD

13. 只有在用户明确确认方案稿后，才能进入第二阶段。
14. 执行 PRD 生成命令：

```bash
prdkit prd create "<title>" --from-plan ./draft/reference/<title>-prd-plan.md
```

15. 根据复杂度等级和产品类型，补齐 `workspace/prds/` 下正式 PRD 的内容，将模板骨架填充为完整文档：
   - L1/L2：保持轻量，但必须完整覆盖背景、目标、范围、需求、风险、验收
   - L3/L4：必须完整覆盖角色、流程、依赖、风险、验收、里程碑
   - 商业化产品：补充商业目标、市场/客户视角
   - 企业自研系统：补充 ROI、效率、内部推广与采纳视角
   - 交易型 / 业务型：补充流程、状态、角色权限
   - 基础服务型：补充 API、调用链路、隔离和稳定性
18. 对 L3/L4，正式输出前必须执行 [references/appendices/selfcheck.md](references/appendices/selfcheck.md) 中的高复杂度自检：
   - 边界条件是否清楚
   - 外部依赖是否清楚
   - 异常流是否清楚
   - 验收标准是否可执行
   - 文末是否附待完善清单
19. 完成后向用户说明正式文档路径，以及后续可继续拆原型、补标注、推进评审。

## 输出约束

- **产品语言**：所有与用户沟通的内容必须使用纯产品语言，不出现文件路径、命令调用、组件名称、样式描述、技术实现等非产品词汇。特别禁止以下三类词汇出现在 PRD 正文中：
  1. **UI 组件名**：穿梭框、弹窗、Tab/标签页、卡片、下拉菜单、树形控件、Banner、面包屑、分页器、日期选择器
  2. **交互描述**：点击、展开、收起、弹出、跳转、滚动、悬浮
  3. **技术实现**：API调用、CSS、DOM、前端、后端、数据库、接口、字段、组件
  4. **ASCII 流程图/状态图**：PRD 中使用图表时必须使用 Mermaid 语法（```mermaid），不得使用纯文本/ASCII 字符画流程或状态图（如使用 ├─└│↓→ 等字符绘制流程图）
  （frontmatter 中的技术术语和命令块中的 CLI 命令不受此限）
- 任何 PRD 生成默认先写方案稿，再写正式稿
- 方案稿路径固定为 `draft/reference/<title>-prd-plan.md`
- 正式 PRD 路径固定为 `workspace/prds/`
- 不要跳过产品定型
- 不要跳过复杂度判断
- 不要在用户未确认方案稿前直接写正式 PRD
- PRD 创建后必须创建 checkpoint 记录版本
