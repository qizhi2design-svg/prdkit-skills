---
name: prdkit-mark-create
description: 当用户从 viewer 复制页面元素信息，要求加标注、创建需求标注、记录这个区域的功能规则或交互要求时使用。只要出现 viewer 复制的元素信息，即使用户没有明确说“标注”，也应主动判断是否适合用此 skill 创建标注。
---

# 创建需求标注

为原型中的页面区域创建标注，记录功能目标、交互行为或数据展示规则。创建动作使用当前内置 prototype mark tools。

## 当前工具分工

- `prototype_mark_list`：检查该页面已有标注
- `prototype_mark_get`：查看已存在标注的详情
- `prototype_mark_create`：创建新标注

## 核心原则

- 全程使用产品语言，只描述用户能做什么、系统如何响应
- 不把 selector、domPath、rect 直接暴露给用户，除非在内部构造 tool 入参时需要
- 创建前把标题、描述、原型路径和定位信息一次确认到位

## 工作流程

### 1. 解析元素信息

从 viewer 复制内容中提取：

- `prototypePath`
- 页面区域的功能描述
- 可能存在的 `selector`
- 可能存在的 `domPath`
- 可能存在的 `rect` / `position`

原型路径应使用相对于 `workspace/prototypes/` 的页面路径。

### 2. 判断是新增还是已有标注延伸

如果用户没有明确说是新增，先用 `prototype_mark_list` 查看该页面现有标注。  
如果看到明显重复的标注主题，再决定是新增还是建议改用 `prdkit-mark-update`。

### 3. 收集标注内容

每次只确认一个主题：

- 标注类型：功能说明 / 交互行为 / 数据展示
- 标注标题：5-15 字，聚焦业务目的
- 标注描述：根据类型组织结构

可按需使用以下模板帮助组织内容：

- [references/templates/prd-feature.md](references/templates/prd-feature.md)
- [references/templates/interaction.md](references/templates/interaction.md)
- [references/templates/data-display.md](references/templates/data-display.md)

### 4. 调用 `prototype_mark_create`

至少传入：

- `projectRoot`
- `prototypePath`
- `title`
- `description`

如果元素信息里有可靠定位，再按需补充：

- `selector`
- `domPath`
- `position`
- `rect`

不要为了凑字段硬填不确定的数据。没有就留空，让标注以业务内容为主。

### 5. 告知结果

用产品语言汇报：

- 哪个页面区域创建了标注
- 标注标题是什么
- 这是功能说明、交互行为，还是数据展示类标注

不需要汇报内部字段名或存储位置。

## 关键约束

- 不再使用参数式表述来组织创建动作
- 多行 Markdown 描述直接组织成 `description` 字段内容即可
- 如果定位信息不可靠，优先保证标题和描述准确
- 若用户贴来的元素信息已足够完整，不要重复追问显而易见的内容
