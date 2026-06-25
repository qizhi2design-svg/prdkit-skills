---
name: prdkit-mark-update
description: 当用户要修改原型上的已有标注，调整标题、说明内容、适用范围或定位信息时使用。遇到“改一下这个标注”“更新标注说明”“这条标注内容变了”这类请求时应主动触发，并通过 prototype_mark_list、prototype_mark_get、prototype_mark_edit 完成更新。
---

# 更新需求标注

更新原型上已有标注的标题、描述或定位信息。标注查询与更新依赖当前内置 prototype mark tools。

## 当前工具分工

- `prototype_mark_list`：列出某页面的所有标注
- `prototype_mark_get`：读取指定标注详情
- `prototype_mark_edit`：更新标注内容

## 工作流程

### 1. 确定原型和目标标注

如果用户没有明确给出页面路径，先确认原型页面。  
然后用 `prototype_mark_list` 列出该页面标注，按产品语言展示标题和一句话概括，让用户选中要修改的那条。

### 2. 读取当前内容

用 `prototype_mark_get` 获取详情，先把可能出现的技术表述转换成产品语言，再展示给用户确认当前状态。

目标是让用户明确知道：

- 当前标题是什么
- 当前说明写了什么
- 哪部分需要调整

### 3. 收集修改内容

优先确认用户要改的是哪一类：

- 只改标题
- 只改说明
- 两者都改
- 顺带调整定位信息

如果改的是说明内容，直接确认“修改后的完整版本”或“明确替换规则”，不要让实现阶段自己猜。

### 4. 调用 `prototype_mark_edit`

`prototype_mark_edit` 以 `markId` + patch 方式更新。  
至少要有：

- `projectRoot`
- `prototypePath`
- `markId`

根据实际修改内容按需传入：

- `title`
- `description`
- `selector`
- `domPath`
- `position`
- `rect`

没有变化的字段不要重写。

### 5. 告知结果

结果汇报只需说明：

- 哪条标注更新了
- 标题是否变化
- 说明内容是否更新

不需要输出内部字段、文件名或技术定位信息。

## 关键约束

- 不再使用参数描述来组织更新流程
- 不把修改动作拆成“写临时文件再传参”的旧心智
- 如果标注已经不适合继续修改，而应该拆成新标注，要明确建议使用 `prdkit-mark-create`
- 用户可见输出继续保持产品语言
