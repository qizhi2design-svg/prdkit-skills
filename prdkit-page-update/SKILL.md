---
name: prdkit-page-update
description: 当用户提供 viewer 复制的元素信息、HTML 片段、页面路径，要求修改已有原型页面时使用。遇到“改这个区域”“调整这个页面”“把这块交互补上”“更新原型里的某个模块”等请求时应主动触发，并结合元素定位、文件编辑与 prototype checkpoint 留痕完成修改。
---

# 修改页面原型

基于用户提供的页面元素信息，定位原型文件、澄清修改意图、编辑页面代码，并在需要时用 prototype checkpoint 记录本次变更。

## 当前工具分工

- `prototype_checkpoint_create`：为这次修改创建版本留痕
- 通用读取工具：定位 `index.html`、相关 `script.js`、`mock.js`、样式文件
- 通用编辑工具：完成页面实现修改

## 工作流程

### 第一阶段：解析元素信息并定位文件

1. 解析用户提供的信息，通常包括：
   - 项目名称
   - 文件路径
   - 元素选择器
   - HTML 片段
   - 文本内容
2. 根据文件路径找到对应页面目录
3. 优先读取：
   - `index.html`
   - 同目录 `script.js`
   - 同目录 `mock.js`
   - 相关样式文件
4. 分析当前实现：
   - 这个区域的 HTML 结构
   - 相关交互逻辑
   - 关联的数据来源
   - 是否已有相近功能可复用

### 第二阶段：澄清修改意图

参考 [references/clarify-intent.md](references/clarify-intent.md)，把修改意图归类为：

- 数据调整
- 交互调整
- 功能新增
- 内容修正
- 结构重组

如果用户描述不完整，追问最关键的缺口，不要泛泛而谈。  
目标是能明确回答这三个问题：

1. 改哪里
2. 改成什么
3. 为什么要这样改

### 第三阶段：制定更新方案并执行

参考 [references/update-plan-template.md](references/update-plan-template.md) 组织修改方案。

执行时遵循：

- 页面代码由通用编辑工具直接修改
- 如涉及数据展示变化，同时更新 `mock.js`
- 如涉及交互变化，同时更新脚本逻辑
- 尽量局部修改，不做无关重构

### 第四阶段：为重要修改留痕

当修改影响页面行为、信息结构或关键业务流程时，在代码改动完成后用 `prototype_checkpoint_create` 创建版本记录。

checkpoint message 要用产品语言描述业务变化，例如：

- `补充门店筛选与结果联动`
- `调整工单详情页的操作流程说明`

不要把 message 写成技术变更说明。

## 关键约束

- 不再引用历史的 checkpoint 或预览启动写法
- 不把 checkpoint 当成替代编辑动作；checkpoint 只负责留痕
- 如果用户给的是局部元素信息，也要先读完整页面上下文再改
- 修改完成后要检查是否波及同页的脚本、数据与文本

## 参考资料

- [references/clarify-intent.md](references/clarify-intent.md)
- [references/modification-examples.md](references/modification-examples.md)
- [references/update-plan-template.md](references/update-plan-template.md)
