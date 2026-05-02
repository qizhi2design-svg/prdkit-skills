# prdkit Skills

Claude Code skills 集合，用于增强 prdkit 产品管理工具的使用体验。这些 skills 让 Claude 能够更智能地协助产品经理完成 PRD 编写、原型创建、标注管理等日常工作。

## 📦 包含的 Skills

### 文档管理

#### prdkit-project-init
初始化产品项目，引导产品经理完成项目配置。

**使用场景**: 
- 创建新的产品项目
- 初始化 prdkit 工作空间

#### prdkit-prd-create
创建产品需求文档（PRD），支持高/中/低复杂度需求。

**使用场景**:
- 编写新的 PRD 文档
- 生成需求文档初稿
- 整理产品方案

**特点**:
- 两阶段流程：先生成方案稿，确认后生成正式 PRD
- 自动完成产品定型与复杂度判断
- 结构化提问补齐信息

#### prdkit-prd-check
审查 PRD 文档质量，按 14 个维度输出改进建议。

**使用场景**:
- Review PRD 文档
- 检查需求完整性
- 发现潜在问题和风险

**检查维度**:
- 需求背景、目标用户、功能描述
- 交互流程、数据模型、异常处理
- 性能要求、安全性、可测试性等

### 原型管理

#### prdkit-page-create
创建原型页面，支持移动端和 PC 端。

**使用场景**:
- 搭建移动端原型
- 创建 PC 后台原型
- 生成页面原型

**特点**:
- 智能判断需求复杂度
- 明确需求直接创建，复杂需求先生成方案
- 支持快速模式

#### prdkit-page-update
修改原型页面，支持样式、交互、数据修改。

**使用场景**:
- 修改页面元素
- 更新交互逻辑
- 调整页面样式

**特点**:
- 两阶段流程：解析元素 → 执行修改
- 自动创建 checkpoint 版本
- 引导预览修改效果

### 标注管理

#### prdkit-mark-create
为原型元素创建标注说明。

**使用场景**:
- 从 viewer 复制元素后创建标注
- 记录交互逻辑和功能说明
- 补充设计规范

**特点**:
- 分析元素上下文
- 结构化提问明确标注内容
- 自动调用 prdkit CLI 创建标注

#### prdkit-mark-update
修改原型标注内容，记录需求变更。

**使用场景**:
- 更新标注说明
- 修正标注错误
- 补充标注细节

### 同步管理

#### prdkit-prototype-sync
将原型更新同步回 PRD 文档。

**使用场景**:
- 原型完成后反哺 PRD
- 同步标注内容到需求文档
- 生成 PRD 修订记录

**特点**:
- 自动定位 PRD 和原型
- 读取 marks 并识别对应章节
- 对比差异后更新 PRD

#### prdkit-viewer-publish
同步 viewer 代码到发布版本。

**使用场景**:
- 同步 UI/样式更新
- 更新共享组件
- 刷新发布版本

## 🚀 快速开始

### 安装 Skills

1. 克隆仓库到本地：
```bash
git clone <repository-url>
cd prdkit/skills
```

2. 将 skills 目录添加到 Claude Code 的 skills 路径：
```bash
# 方法 1: 复制到 Claude Code 的 skills 目录
cp -r prdkit-* ~/.claude/skills/

# 方法 2: 创建符号链接
ln -s $(pwd)/prdkit-* ~/.claude/skills/
```

3. 重启 Claude Code 或重新加载 skills

### 使用 Skills

Skills 会根据你的对话内容自动触发。例如：

```
你: 帮我写一个用户登录功能的 PRD
Claude: [自动使用 prdkit-prd-create skill]

你: 我从 viewer 复制了这个按钮的信息：<button class="submit">提交</button>
Claude: [自动使用 prdkit-mark-create skill]

你: 帮我 review 一下这个 PRD
Claude: [自动使用 prdkit-prd-check skill]
```

## 📖 Skill 详细说明

每个 skill 目录包含：
- `SKILL.md` - Skill 的详细说明和使用指南
- `references/` - 参考文档（如果有）
- `scripts/` - 辅助脚本（如果有）

查看具体 skill 的使用方法：
```bash
cat prdkit-prd-create/SKILL.md
```

## 🛠️ 开发

### 项目结构

```
prdkit/skills/
├── prdkit-project-init/     # 项目初始化
├── prdkit-prd-create/       # PRD 创建
├── prdkit-prd-check/        # PRD 审查
├── prdkit-page-create/      # 原型创建
├── prdkit-page-update/      # 原型修改
├── prdkit-mark-create/      # 标注创建
├── prdkit-mark-update/      # 标注修改
├── prdkit-prototype-sync/   # 原型同步
└── prdkit-viewer-publish/   # Viewer 发布
```

### 修改 Skills

1. 编辑对应的 `SKILL.md` 文件
2. 测试修改后的 skill
3. 提交更改

### 测试 Skills

使用 skill-creator 进行评测：
```bash
# 在 Claude Code 中
/skill-creator evaluate <skill-name>
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

- [prdkit CLI](../cli) - prdkit 命令行工具
- [prdkit Templates](../template) - PRD 和原型模板
- [prdkit Scaffold](../scaffold) - 项目脚手架

## 📮 反馈

如有问题或建议，请提交 [Issue](../../issues)。
