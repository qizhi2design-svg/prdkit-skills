# Prototype 反哺 PRD 工作流

## 输入

- 目标 PRD：标题 / 文件名 / 路径
- 目标 prototype：prototype 路径
- 可选：是否只同步某些 marks

## 输出

- 更新后的 PRD 文件
- 同步后的 prototype 链接
- 新增一条修订记录

## 标准步骤

1. 用 `prdkit prd check` 定位 PRD
2. 定位 prototype：
   - 用户有 URL → `prdkit prototype release link resolve <url>`
   - 用户有路径 → 直接使用
   - 其他 → `prdkit prototype list` + 上下文推断
3. 用 `prdkit prototype release link list --json` 获取云端 release URL
4. 用 `prdkit prototype mark list --prototype <路径> --json` 获取标注列表
5. 用 `prdkit prototype mark get <ID> --prototype <路径> --json` 获取标注详情
6. 过滤指标数据：将标注中的交互/技术指标转换为产品/业务指标，无法转换的丢弃
7. 归纳标注内容
8. 识别 PRD 中现有的对应功能说明小节
9. 更新 PRD（附带更新 prototype 链接为云端 URL）
10. 追加修订记录
11. 用 `prdkit prd checkpoint create` 为 PRD 创建 checkpoint，message 使用产品语言描述本次变更

## 同步粒度建议

- 默认以单个 prototype 为最小同步单元
- prototype 下每条标注是需求描述提炼的证据，不一定一条标注对应一条需求点
- 多条标注可以合并成一个功能块

## 风险提示

- 标注标题过泛时，不要直接写进 PRD，先看 description
- 如果标注内容与 PRD 现有描述冲突，要在修订记录里明确标注”覆盖/替换”
- 如果无法判断该标注应归属哪个功能模块，放入”待确认事项”
