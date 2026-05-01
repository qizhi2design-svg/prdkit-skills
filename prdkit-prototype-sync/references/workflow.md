# Prototype 反哺 PRD 工作流

## 输入

- 目标 PRD：标题 / 文件名 / 路径
- 目标 prototype：prototype 路径
- 可选：是否只同步某些 marks

## 输出

- 更新后的 PRD 文件
- 更新过的 `Feature List`
- 同步后的 prototype 链接
- 新增一条修订记录

## 标准步骤

1. 用 `prdkit prd check` 定位 PRD
2. 用 `prdkit prototype list` 和用户输入定位 prototype
3. 用 `prdkit mark list --json` 获取 mark 列表
4. 用 `prdkit mark get --json` 获取 mark 详情
5. 归纳 mark 内容
6. 识别 PRD 中现有的对应需求描述小节
7. 更新 PRD
8. 追加修订记录

## 同步粒度建议

- 默认以单个 prototype 为最小同步单元
- prototype 下每个 mark 是需求描述提炼的证据，不一定一条 mark 对应一条需求点
- 多条 mark 可以合并成一个功能块

## 风险提示

- mark 标题过泛时，不要直接写进 PRD，先看 description
- 如果 mark 内容与 PRD 现有描述冲突，要在修订记录里明确标注“覆盖/替换”
- 如果无法判断该 mark 应归属哪个功能点，放入“待确认项”
