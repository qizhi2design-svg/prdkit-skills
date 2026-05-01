---
name: prdkit-page-create
description: 当用户提出创建原型、起原型、生成页面原型、搭建移动端原型、搭建 PC 后台原型，或提到旧称 `create-prototype` 时使用。该 skill 采用两阶段流程：第一阶段只检查 `prdkit` 与项目状态、扫描上下文、提出 3-4 个高信息密度问题、生成任务清单与 ASCII 线框图，并写入 `draft/reference/<title>-prototype-plan.md`；第二阶段只有在用户明确确认方案文档后，才执行 `prdkit prototype create` 并补齐页面代码、交互骨架与 `mock.js` 数据。
allowed-tools:
  - Read
  - Grep
  - Glob
  - LS
  - AskQuestion
  - Bash(command -v prdkit)
  - Bash(prdkit info*)
  - Bash(prdkit init*)
  - Bash(prdkit prototype create*)
  - Bash(prdkit prototype list*)
  - Bash(prdkit serve*)
  - Bash(npm install -g @huangqz/prdkit-cli*)
  - Edit
  - MultiEdit
  - Write
---

# 创建页面原型

## 工作流程

### 第一阶段：生成方案文档

1. 从目标项目根目录开始。
2. 先检查命令行工具和项目状态：
   - 运行 `command -v prdkit`
   - 运行 `prdkit info`
3. 如果缺少 `prdkit` 命令，先执行安装：

```bash
npm install -g @huangqz/prdkit-cli
```

4. 如果 `prdkit info` 提示当前目录不是 `prdkit` 项目：
   - 先引导用户完成项目初始化
   - 如果项目名和作者已知，优先执行：

```bash
prdkit init . --name "<project-name>" --author "<author>"
```

   - 如果初始化所需关键信息缺失，只补问缺失字段后再继续
5. 在决定布局和交互前，先读取项目上下文：
   - `context/`
   - `draft/`
   - 已有 `workspace/prototypes/`
   - 相关的 `workspace/prds/` 或 `workspace/discussions/`
6. 使用 `AskQuestion` 工具与用户确认需求，参考 [references/phase-1-requirements.md](references/phase-1-requirements.md) 提出 3-4 个高信息密度问题：
   - 优先确认平台类型：`mobile` / `admin` / `web`（只有明确不是移动端和后台时才用 `web`）
   - 用户未明确确认前，不得执行 `prdkit prototype create`
   - 信息不足时继续补问，不能跳过确认阶段
7. 将确认产物保存到 `draft/reference/<title>-prototype-plan.md`（参考 references 中的格式），内容包括：
   - 任务清单、已确认信息、当前假设、待确认项
   - ASCII 线框图、交互说明
   - 视觉样式参数、画布规格、层级规则
   - 第二阶段执行命令
   - 明确标注”当前处于第一阶段，尚未创建页面”
8. 第一阶段结束后必须停止，等待用户确认。

### 第二阶段：创建页面

9. 只有在用户明确确认方案后，才能进入第二阶段。
10. 执行 `prdkit prototype create` 命令，按方案文档补齐页面结构、交互逻辑与 mock 数据：
   - 默认按 [references/phase-3-implementation.md](references/phase-3-implementation.md) 的画布规格生成
   - mock 数据统一写入页面目录下的 `mock.js`
11. 页面修改完成后，使用 `prdkit checkpoint create` 记录变更。
12. 检查预览服务器状态并引导用户预览：
   - 运行 `prdkit serve status` 检查是否有服务在运行
   - 如果有服务运行：提示用户直接在浏览器中访问显示的地址
   - 如果没有服务运行：
     - 运行 `prdkit serve` 启动预览服务器
     - 提示用户点击终端中显示的链接或访问 `http://localhost:<port>`

## 命令映射

- 移动端 App / H5：

```bash
prdkit prototype create "<title>" --template mobile --dir ./workspace/prototypes
```

- PC 后台 / 工作台 / 仪表盘：

```bash
prdkit prototype create "<title>" --template admin --dir ./workspace/prototypes
```

- 通用 Web 页面：

```bash
prdkit prototype create "<title>" --template web --dir ./workspace/prototypes
```

可选补充命令：

```bash
prdkit prototype list
prdkit serve
```

## 方案文档格式

第一阶段的方案记录保存到 `draft/reference/<title>-prototype-plan.md`，复用 references 中的格式模板。

## 约束规则

**流程控制**
- 平台类型模糊时，不得进入页面实现
- 第一阶段必须落盘方案文档并暂停，等用户确认后再继续
- 项目未初始化时，先完成初始化再执行原型命令

**交互要求**
- 必须使用 `AskQuestion` 工具提问，不允许跳过
- 任务计划使用 `TodoWrite` 工具呈现
- 问题应短、准、高信息密度，避免宽泛开放式提问
- 用户回答不完整时，可做少量假设但必须记录到方案文档

**技术规范**
- 显式指定模板，不依赖默认值
- 默认尺寸：`mobile` 用 `390 x 844`，`admin/web` 用 `1440 x 900`
- 参考 `phase-3-implementation.md` 的画布、圆角、弹窗和 `z-index` 规则
- 页面内部不使用 `z-index: 9999`（预留给 viewer）
- 数据结构：每页一个 `mock.js`，`script.js` 只消费数据
- ASCII 线框图只确认结构，保持简洁易读
- **图片占位**：禁止使用真实图片链接（unsplash、placeholder.com 等），统一使用纯色背景 + 文字标注的方式占位

## 资源说明

### references/

- `phase-1-requirements.md`：需求澄清阶段的提问模板和确认记录格式
- `phase-2-wireframes.md`：结构确认阶段的 ASCII 线框图模板和交互说明要求
- `phase-3-implementation.md`：实现阶段的视觉参数、画布规范、图片占位和 CSS 基准
