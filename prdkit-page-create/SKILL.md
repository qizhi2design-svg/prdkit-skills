---
name: prdkit-page-create
description: 当用户要创建原型页面、起页面草稿、生成后台页/移动端页/业务页面原型时使用。遇到“做个页面原型”“起一个后台页面”“根据需求做页面”“按参考图搭一个原型”等请求时应主动触发，并按“先方案、后创建”的两阶段流程完成。
---

# 创建页面原型

使用当前桌面端内置 tools 规划并创建新的 prototype 页面。默认遵循“两阶段”：先写方案，再创建页面骨架并补充内容。

## 当前工具分工

- `project_info`：确认当前目录是否是有效项目，读取项目概况
- `prototype_list`：查看现有页面，避免重复创建
- `prototype_create`：创建新的 prototype 页面骨架
- 通用读写工具：补充方案稿、编辑创建后的页面文件

## 工作流程

### 第一阶段：生成方案文档

1. 先用 `project_info` 确认当前项目可用
2. 再用 `prototype_list` 了解现有页面，避免同名或重复功能
3. 读取项目上下文：
   - `context/`
   - `draft/`
   - `workspace/prototypes/`
   - 相关 `workspace/prds/` 或 `workspace/discussions/`
4. 判断需求来源：
   - 纯文字描述
   - 参考图 / 参考页面
   - 明确要求高度还原
5. 参考 [references/phase-1-requirements.md](references/phase-1-requirements.md) 提 3-4 个高信息密度问题，优先确认：
   - 页面目标
   - 使用平台：`mobile` / `admin` / `web`
   - 核心模块与信息层级
   - 是否需要高度还原参考图
6. 生成方案稿到 `draft/reference/<title>-prototype-plan.md`

方案稿必须包含：

- 任务清单
- 已确认信息
- 当前假设
- 待确认项
- ASCII 线框图
- 关键交互说明
- 页面结构与内容层级

如果是高度还原场景，还要补充：

- 页面元素顺序
- 文案约束
- 布局与视觉要点

如果是参考设计场景，还要补充：

- 从参考中抽取的结构规律
- 需要保留与允许调整的部分

第一阶段结束后必须停下，等待用户确认方案。

### 第二阶段：创建页面并补充内容

只有用户明确确认方案稿后，才能进入第二阶段。

1. 用 `prototype_create` 创建页面骨架
2. `prototype_create` 至少传入：
   - `projectRoot`
   - `title`
   - `template`
3. `template` 根据阶段一结论选择：
   - `mobile`
   - `admin`
   - `web`
4. 页面创建后，再用通用读写工具按方案稿补充页面结构、文案、脚本和示例数据
5. 如需补充实现细节，可按需加载：
   - [references/phase-2-wireframes.md](references/phase-2-wireframes.md)
   - [references/phase-3-implementation.md](references/phase-3-implementation.md)

## 关键约束

- 不要再写额外安装步骤、预览启动或整目录重建
- 创建动作必须通过 `prototype_create` 描述
- 页面骨架创建与页面内容补全是两件事：前者靠内置 tool，后者靠通用编辑工具
- 如果发现已有页面高度重合，先建议复用或修改，不要直接再起一个重复页面

## 用户沟通方式

- 先让用户确认页面目标，再确认平台和关键区域
- 如果参考图很多，只抓最影响页面结构的差异，不要把问题问碎
- 输出结果时要说明：
  - 方案稿路径
  - 页面是否已创建
  - 下一步是补内容、联动 PRD，还是继续拆更多页面
