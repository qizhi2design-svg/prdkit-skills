<div align="center">
  <img src="assets/banner.png" alt="prdkit Skills Banner" width="100%">
  
  # PRDkit Skills
  
  <p>✨ 让 AI 更智能地协助产品经理完成 PRD 编写、原型创建、标注管理等日常工作</p>
  
  <p>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills">
      <img src="https://img.shields.io/github/stars/qizhi2design-svg/prdkit-skills?style=social" alt="GitHub stars">
    </a>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills/fork">
      <img src="https://img.shields.io/github/forks/qizhi2design-svg/prdkit-skills?style=social" alt="GitHub forks">
    </a>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/qizhi2design-svg/prdkit-skills" alt="License">
    </a>
    <a href="#-包含的-skills">
      <img src="https://img.shields.io/badge/Skills-8-blue" alt="Skills count">
    </a>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills/issues">
      <img src="https://img.shields.io/github/issues/qizhi2design-svg/prdkit-skills" alt="GitHub issues">
    </a>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills/pulls">
      <img src="https://img.shields.io/github/issues-pr/qizhi2design-svg/prdkit-skills" alt="GitHub pull requests">
    </a>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills/commits">
      <img src="https://img.shields.io/github/last-commit/qizhi2design-svg/prdkit-skills" alt="Last commit">
    </a>
    <a href="https://github.com/qizhi2design-svg/prdkit-skills/graphs/contributors">
      <img src="https://img.shields.io/github/contributors/qizhi2design-svg/prdkit-skills" alt="Contributors">
    </a>
  </p>
  
  <p>
    <strong>⚡ 快速上手</strong> • 
    <strong>🎯 智能触发</strong> • 
    <strong>🛠️ 开箱即用</strong> • 
    <strong>🔧 高度可定制</strong>
  </p>
</div>

## ✨ 核心特性

- 🤖 **AI 驱动**：基于 Claude 的智能理解和生成能力
- 🎨 **原型设计**：快速创建移动端和 PC 端原型页面
- 📝 **PRD 编写**：自动生成结构化的产品需求文档
- 🏷️ **标注管理**：为原型元素添加详细的功能说明
- 🔄 **双向同步**：原型与 PRD 文档自动同步更新
- ✅ **质量审查**：14 个维度全面检查 PRD 质量
- 🚀 **工作流优化**：从项目初始化到文档审查的完整流程
- 💡 **智能判断**：自动识别需求复杂度，选择最佳处理方式

## 🔄 典型工作流程

```mermaid
graph LR
    A[项目初始化<br/>project-init] --> B[创建原型<br/>page-create]
    B --> C[添加标注<br/>mark-create]
    C --> D{需要修改?}
    D -->|修改页面| E[page-update]
    D -->|修改标注| F[mark-update]
    E --> D
    F --> D
    D -->|完成| H[创建PRD<br/>prd-create]
    H --> G[同步到PRD<br/>prototype-sync]
    G --> I[审查PRD<br/>prd-check]
    I --> J{需要优化?}
    J -->|是| B
    J -->|否| K[完成]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#fff4e1
    style E fill:#fff4e1
    style F fill:#fff4e1
    style H fill:#e8f5e9
    style G fill:#e8f5e9
    style I fill:#f3e5f5
    style K fill:#c8e6c9
```

## 📦 包含的 Skills

| 阶段 | Skill | 功能描述 | 使用场景 |
|------|-------|----------|----------|
| **第一步：项目初始化** | [prdkit-project-init](prdkit-project-init/) | 初始化产品项目，引导产品经理完成项目配置 | 创建新的产品项目、初始化 prdkit 工作空间 |
| **第二步：原型设计** | [prdkit-page-create](prdkit-page-create/) | 创建原型页面，支持移动端和 PC 端<br/>• 智能判断需求复杂度<br/>• 支持快速模式 | 搭建移动端原型、创建 PC 后台原型、生成页面原型 |
| | [prdkit-mark-create](prdkit-mark-create/) | 为原型元素创建标注说明<br/>• 分析元素上下文<br/>• 结构化提问明确标注内容 | 从 viewer 复制元素后创建标注、记录交互逻辑和功能说明 |
| | [prdkit-page-update](prdkit-page-update/) | 修改原型页面，支持样式、交互、数据修改<br/>• 自动创建 checkpoint 版本 | 修改页面元素、更新交互逻辑、调整页面样式 |
| | [prdkit-mark-update](prdkit-mark-update/) | 修改原型标注内容，记录需求变更 | 更新标注说明、修正标注错误、补充标注细节 |
| **第三步：PRD 编写** | [prdkit-prd-create](prdkit-prd-create/) | 创建产品需求文档（PRD），支持高/中/低复杂度需求<br/>• 两阶段流程：先生成方案稿，确认后生成正式 PRD<br/>• 自动完成产品定型与复杂度判断 | 编写新的 PRD 文档、生成需求文档初稿、整理产品方案 |
| | [prdkit-prototype-sync](prdkit-prototype-sync/) | 将原型更新同步回 PRD 文档<br/>• 自动定位 PRD 和原型<br/>• 对比差异后更新 PRD | 原型完成后反哺 PRD、同步标注内容到需求文档 |
| **第四步：审查优化** | [prdkit-prd-check](prdkit-prd-check/) | 审查 PRD 文档质量，按 14 个维度输出改进建议<br/>• 需求背景、目标用户、功能描述<br/>• 交互流程、数据模型、异常处理<br/>• 性能要求、安全性、可测试性等 | Review PRD 文档、检查需求完整性、发现潜在问题和风险 |

## 🚀 快速开始

### 📥 安装 Skills

```bash
# 安装所有 skills（推荐）
npx skills add qizhi2design-svg/prdkit-skills -a claude-code -s '*' -y

# 列出可用的 skills
npx skills add qizhi2design-svg/prdkit-skills --list

# 安装特定 skill
npx skills add qizhi2design-svg/prdkit-skills -a claude-code -s prdkit-prd-create

# 全局安装
npx skills add qizhi2design-svg/prdkit-skills -a claude-code -s '*' -g -y
```

**常用选项**：
- `-a, --agent <name>`: 指定目标平台（`claude-code` 或 `codex`）
- `-s, --skill <name>`: 选择特定 skill（使用 `'*'` 安装全部）
- `-g, --global`: 全局安装到 `~/.claude/skills/`
- `-y, --yes`: 跳过确认提示
- `--list`: 列出仓库中所有可用的 skills

### 🤖 支持的平台

这些 skills 可以安装到以下 AI 编程助手平台：

| 平台 | `--agent` 参数 | Skills 路径 |
|------|---------------|-------------|
| **Claude Code** | `claude-code` | `~/.claude/skills/` |
| **Codex** | `codex` | `~/.codex/skills/` |

### 🔧 手动安装

如果你更喜欢手动管理 skills：

```bash
# 1. 克隆仓库
git clone https://github.com/qizhi2design-svg/prdkit-skills.git
cd prdkit-skills

# 2. 复制到 Claude Code skills 目录
cp -r prdkit-* ~/.claude/skills/

# 或者创建符号链接（推荐，便于更新）
ln -s $(pwd)/prdkit-* ~/.claude/skills/

# 3. 重启 Claude Code
```

### 💡 使用 Skills

Skills 会根据你的对话内容自动触发。例如：

```
你: 帮我写一个用户登录功能的 PRD
Claude: [自动使用 prdkit-prd-create skill]

你: 我从 viewer 复制了这个按钮的信息：<button class="submit">提交</button>
Claude: [自动使用 prdkit-mark-create skill]

你: 帮我 review 一下这个 PRD
Claude: [自动使用 prdkit-prd-check skill]
```

## 📚 命令参考

### `skills add` - 安装 Skills

从 GitHub 仓库安装 skills 到本地或全局目录。

```bash
# 安装所有 skills
npx skills add qizhi2design-svg/prdkit-skills -a claude-code -s '*' -y

# 列出可用的 skills
npx skills add qizhi2design-svg/prdkit-skills --list

# 安装特定 skill
npx skills add qizhi2design-svg/prdkit-skills -a claude-code -s prdkit-prd-create

# 全局安装所有 skills
npx skills add qizhi2design-svg/prdkit-skills --all -g
```

**常用选项**：
- `-g, --global` - 安装到用户目录（`~/.claude/skills/`）
- `-a, --agent <agents...>` - 指定目标平台
- `-s, --skill <skills...>` - 安装特定 skills
- `-l, --list` - 列出仓库中可用的 skills
- `--copy` - 复制文件而非创建符号链接
- `-y, --yes` - 跳过确认提示
- `--all` - 安装所有 skills 且不提示

### `skills list` - 列出已安装的 Skills

查看当前已安装的 skills，支持按平台过滤。

```bash
# 列出所有已安装的 skills
npx skills list

# 列出全局安装的 skills
npx skills ls -g

# 列出特定平台的 skills
npx skills ls -a claude-code
```

**别名**: `ls`

### `skills find` - 搜索 Skills

交互式搜索或按关键词查找可用的 skills。

```bash
# 交互式搜索
npx skills find

# 按关键词搜索
npx skills find prd
npx skills find prototype
```

### `skills update` - 更新 Skills

更新已安装的 skills 到最新版本。

```bash
# 更新所有 skills
npx skills update

# 更新特定 skill
npx skills update prdkit-prd-create

# 仅更新全局 skills
npx skills update -g

# 仅更新项目 skills
npx skills update -p
```

**常用选项**：
- `-g, --global` - 仅更新全局 skills
- `-p, --project` - 仅更新项目 skills
- `-y, --yes` - 自动检测范围并更新

### `skills remove` - 移除 Skills

从指定平台移除 skills。

```bash
# 交互式移除
npx skills remove

# 移除特定 skill
npx skills remove prdkit-prd-create

# 移除所有 prdkit skills
npx skills remove -s 'prdkit-*'

# 从特定平台移除
npx skills remove -a claude-code -s prdkit-prd-create
```

**别名**: `rm`

**常用选项**：
- `-g, --global` - 从全局目录移除
- `-a, --agent <agents...>` - 指定平台
- `-s, --skill <skills...>` - 指定要移除的 skills
- `-y, --yes` - 跳过确认提示
- `--all` - 移除所有 skills

### `skills init` - 创建新 Skill

创建新的 skill 模板文件（SKILL.md）。

```bash
# 交互式创建
npx skills init

# 创建指定名称的 skill
npx skills init my-custom-skill
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-skill`)
3. 提交更改 (`git commit -m 'Add amazing skill'`)
4. 推送到分支 (`git push origin feature/amazing-skill`)
5. 创建 Pull Request

## 📝 License

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🔗 相关项目

- [prdkit CLI](https://github.com/qizhi2design-svg/prdkit) - prdkit 命令行工具
- [create-prd-skill](https://github.com/pmYangKun/create-prd-skill) - B端 PRD 生成工具
- [tapd-skills](https://github.com/qizhi2design-svg/tapd-skills) - TAPD 需求协作 skills

## 📮 反馈

如有问题或建议，请提交 [Issue](https://github.com/qizhi2design-svg/prdkit-skills/issues)。
