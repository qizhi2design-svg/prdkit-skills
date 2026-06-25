---
name: prdkit-prd-create
description: 当用户要写 PRD、生成需求文档、整理产品方案、补一份正式需求稿时使用。遇到“起个 PRD”“把需求整理成文档”“输出正式产品方案”这类请求应主动触发，并沿用“先方案稿、后正式稿”的两阶段方法，用 project_info、prd_list、prd_create 与通用编辑工具完成。
---

# 创建复杂度感知 PRD

为当前项目生成一套“先方案稿、后正式稿”的 PRD 工作流。正式 PRD 的初始骨架由 `prd_create` 创建，后续内容补齐通过通用编辑工具完成。

## 当前工具分工

- `project_info`：确认项目状态
- `prd_list`：查看现有 PRD，避免重复
- `prd_create`：创建正式 PRD 初稿骨架
- 通用读写工具：写方案稿、补全文档内容

## 渐进加载原则

不要一开始就把所有参考资料读完。按阶段加载：

1. 阶段 0：
   - [references/framework/complexity-assessment.md](references/framework/complexity-assessment.md)
   - [references/appendices/product-typing.md](references/appendices/product-typing.md)
2. 阶段 1：
   - [references/question-bank.md](references/question-bank.md)
   - [references/plan-template.md](references/plan-template.md)
   - [references/chapters/chapter-generation.md](references/chapters/chapter-generation.md)
3. 阶段 2：
   - [references/final-prd-sections.md](references/final-prd-sections.md)
   - [references/appendices/selfcheck.md](references/appendices/selfcheck.md)

## 工作流程

### 阶段 0：确认项目、产品类型与复杂度

1. 先用 `project_info` 确认当前项目可用
2. 再用 `prd_list` 看现有 PRD，避免重名或重复主题
3. 扫描上下文：
   - `context/`
   - `draft/`
   - `workspace/prds/`
   - `workspace/discussions/`
4. 结合参考资料先判断：
   - 产品定型
   - 需求复杂度等级

### 阶段 1：生成方案稿

参考 [references/question-bank.md](references/question-bank.md) 提 3-4 个高信息密度问题，补齐：

- 背景与业务问题
- 角色与关键场景
- 范围边界
- 数据、依赖、风险、验收

然后按 [references/plan-template.md](references/plan-template.md) 生成方案稿：

- 路径：`draft/reference/<title>-prd-plan.md`

方案稿必须写清：

- 产品定型及原因
- 复杂度等级及原因
- 推荐章节策略
- 已确认信息
- 当前假设
- 待确认 / 开放问题
- 第二阶段的执行方式

阶段一结束后必须等待用户确认。

### 阶段 2：创建正式 PRD 并补全内容

只有在用户确认方案稿后，才能进入第二阶段。

1. 用 `prd_create` 创建正式 PRD 骨架
2. 传入至少：
   - `projectRoot`
   - `title`
3. 创建后的正式文档位于 `workspace/prds/`
4. 再根据方案稿、复杂度等级与产品类型，用通用编辑工具补齐完整内容
5. 对 L3/L4 需求，在输出前执行 [references/appendices/selfcheck.md](references/appendices/selfcheck.md) 的高复杂度自检

## 关键约束

- 不再假设存在“方案稿直接生成正式稿”的单步能力
- `prd_create` 负责“创建初稿骨架”，不是“自动吃掉方案稿并生成完整正式稿”
- 方案稿与正式稿仍然分阶段，不要跳过用户确认
- 正式稿必须根据复杂度和产品类型调整章节深度

## 输出约束

- 方案稿路径固定：`draft/reference/<title>-prd-plan.md`
- 正式 PRD 路径固定：`workspace/prds/`
- 不要跳过产品定型
- 不要跳过复杂度判断
- 不要在用户未确认方案稿前直接写正式 PRD
