---
name: prdkit-prototype-sync
description: 当用户要把 prototype 反哺到 PRD、把原型更新同步回需求文档、根据标注修订正式需求、补原型链接或生成修订记录时使用。遇到“把原型同步到 PRD”“根据页面更新需求稿”“把标注沉淀回文档”这类请求应主动触发，并用 prd_check、prototype_list、prototype_mark_*、prototype_release_link_* 与 prd_checkpoint_create 完成闭环。
---

# 将 Prototype 反哺到 PRD

把指定 prototype 的最新结构与标注内容沉淀回 PRD，并留下清晰的修订记录。定位、查询和留痕依赖当前内置 tools；PRD 正文改写通过通用编辑工具完成。

## 当前工具分工

- `prd_check` / `prd_list`：定位目标 PRD
- `prototype_list`：定位目标 prototype
- `prototype_mark_list` / `prototype_mark_get`：读取标注内容
- `prototype_release_link_list` / `prototype_release_link_resolve`：获取或解析原型链接
- `prd_checkpoint_create`：为本次同步创建 PRD checkpoint
- 通用编辑工具：把归纳后的内容写回 PRD

## 渐进加载原则

按阶段加载参考资料：

1. 阶段 0：
   - [references/workflow.md](references/workflow.md)
2. 阶段 1：
   - [references/requirement-sync-contract.md](references/requirement-sync-contract.md)
3. 阶段 2：
   - [references/revision-log-template.md](references/revision-log-template.md)

## 工作流程

### 阶段 0：定位 PRD 与 Prototype

1. 若用户已提供 PRD 标题、路径或文件名，优先用 `prd_check`
2. 若没有说清楚，先用 `prd_list`
3. 定位 prototype 时：
   - 若用户提供 release URL，优先用 `prototype_release_link_resolve`
   - 若用户提供本地页面路径，直接使用
   - 否则先用 `prototype_list`
4. 若定位结果带推断成分，要在输出中明确说明这是“当前假设”还是“已确认事实”

### 阶段 1：收集原型与标注信息

1. 用 `prototype_mark_list` 读取页面下所有标注
2. 对需要沉淀的标注，再用 `prototype_mark_get` 读取详情
3. 用 `prototype_release_link_list` 查询该页面是否已有可回写到 PRD 的 release 链接
4. 读取目标 PRD 全文，关注：
   - 页面 / 模块功能说明
   - 操作流程
   - 业务约束
   - 待确认事项
   - 修订记录

### 阶段 2：归纳可回写内容

不要把标注原文整段机械贴进 PRD，要先归纳成：

- 功能说明
- 操作流程
- 业务约束
- 待确认事项

如果标注里混有技术指标或实现细节，按 [references/requirement-sync-contract.md](references/requirement-sync-contract.md) 过滤或转写为产品语言。

### 阶段 3：回写 PRD 并追加修订记录

1. 用通用编辑工具把整理后的内容写回最匹配的 PRD 小节
2. 同步 prototype 链接
3. 如果 PRD 没有“修订记录”，创建 `## 修订记录`
4. 按 [references/revision-log-template.md](references/revision-log-template.md) 追加本次修订摘要
5. 修改完成后，用 `prd_checkpoint_create` 为本次同步创建 checkpoint

checkpoint message 要用产品语言描述业务变化，例如：

- `同步门店知识库原型，补充筛选区与任务列表说明`

不要写成工具或操作日志。

## 关键约束

- 不再使用历史 release link 或 checkpoint 写法组织流程
- 标注读取必须通过 `prototype_mark_list` + `prototype_mark_get` 组合完成
- PRD 内容改写与链接定位是两套职责：前者靠编辑工具，后者靠内置 tools
- 默认一次只同步一个 prototype，除非用户明确要求批量同步
