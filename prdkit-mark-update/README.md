# prdkit-prototype-update-mark

修改原型标注的 skill。

## 功能

当用户从 viewer 点击已有标注并希望修改时，该 skill 会：

1. 解析标注信息（包括标记文件路径）
2. 使用 `prdkit mark get` 获取现有标注内容
3. 通过结构化提问明确修改内容
4. 使用 `prdkit mark edit` 命令更新标注

## 使用场景

- 用户从 viewer 复制了包含标记文件路径的元素信息
- 用户想要修改已有标注的标题或描述
- 用户需要更新标注内容以反映最新的需求

## 输入格式

用户通常会提供如下格式的信息：

```
项目名: 测试项目
文件路径: /Users/xxx/workspace/prototypes/admin-demo
DOM 路径: body > div.app-shell > div.content-shell > main.workspace > section.panel
标记文件: /Users/xxx/workspace/prototypes/admin-demo/marks/mark-1777623767763.md
```

关键信息是**标记文件路径**，这表明用户想要修改已有标注。

## 工作流程

### 1. 解析和获取
- 从标记文件路径提取原型路径和 mark ID
- 使用 `prdkit mark get` 获取现有标注内容
- 展示当前的标题和描述

### 2. 明确修改
- 询问用户要修改什么（标题、描述或两者）
- 收集新的内容

### 3. 更新标注
- 使用 `prdkit mark edit` 命令更新标注
- 只传递需要修改的参数
- 提示用户更新成功

## 修改类型

支持三种修改类型：

1. **只修改标题**：使用 `--title` 参数
2. **只修改描述**：使用 `--desc` 参数
3. **同时修改**：同时使用 `--title` 和 `--desc` 参数

## 使用的 CLI 命令

- `prdkit mark get <mark-id> --prototype <path> --json` - 获取现有标注内容
- `prdkit mark edit <mark-id> --prototype <path> [--title <text>] [--desc <markdown>]` - 更新标注

## 文档结构

```
prdkit-prototype-update-mark/
├── SKILL.md          # Skill 主文档
├── README.md         # 本文件
└── references/       # 参考文档（预留）
```

## 注意事项

- 必须先使用 `prdkit mark get` 获取现有内容
- 原型路径必须是相对路径（相对于 workspace/prototypes/）
- 只传递需要修改的参数，避免不必要的更新
- 更新后会自动创建 checkpoint
