---
name: prdkit-prd-check
description: 当用户要审查 PRD、检查需求文档、挑问题、补漏洞、给改进建议时使用。遇到“review 这份 PRD”“检查方案有没有问题”“帮我审一下需求稿”这类请求应主动触发，并先通过 prd_check 或 prd_list 定位目标文档，再按 14 个维度输出 findings。
---

# 审查 PRD

为当前项目中的 PRD 提供结构化评审。文档定位依赖当前内置 PRD tools，评审框架依赖 skill 自带 references。

## 当前工具分工

- `prd_check`：当用户已给出标题、路径或目标文档线索时，优先定位单份 PRD
- `prd_list`：当用户没说清楚是哪份 PRD 时，先列出现有文档再选择
- 通用读取工具：读取被评审 PRD 正文

## 渐进加载原则

不要一次性读取所有参考资料。按阶段加载：

1. 阶段 0：
   - [references/framework/review-path.md](references/framework/review-path.md)
2. 阶段 1：
   - 只读取当前正在评审的维度文件
3. 阶段 2：
   - [references/appendices/veto-checklist.md](references/appendices/veto-checklist.md)
   - [references/appendices/report-template.md](references/appendices/report-template.md)

## 工作流程

### 阶段 0：定位目标 PRD

1. 如果用户给了标题、文件名或路径，优先用 `prd_check`
2. 如果用户只说“帮我看下这个项目的 PRD”，先用 `prd_list`
3. 明确本次评审对象后，再读取正文内容

### 阶段 1：做产品定型与适用性判断

按 [references/framework/review-path.md](references/framework/review-path.md) 先判断：

- 产品类型
- 需求所处阶段
- 本次评审更偏结构问题、范围问题，还是可落地性问题

### 阶段 2：按 14 个维度输出 findings

逐项评审，优先输出：

- 严重缺口
- 高风险假设
- 行为回归或歧义
- 缺失的验收与边界条件

评审结果应以 findings 为主，不要先写大段总评。

### 阶段 3：收束为决策建议

最后再汇总：

- 重大风险
- 优先级最高的问题清单
- Top 改进建议

## 输出约束

- 先 findings，后总结
- 结论要落到文档内容，而不是泛泛讲“建议完善”
- 不把历史写法当成评审主体；当前 tool 只负责定位文档
