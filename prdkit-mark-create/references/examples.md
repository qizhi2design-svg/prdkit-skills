# 使用示例

本文档提供实际使用场景的示例，帮助理解如何使用 prdkit-prototype-create-mark skill。

## 示例 1：为导航菜单创建 PRD Feature 标注

### 场景描述
用户在 viewer 中点击了侧边栏的导航菜单，希望添加功能说明。

### 用户输入
```
项目: 电商后台管理系统
文件路径: /Users/alice/workspace/prototypes/admin-dashboard
DOM 路径: body > div.app-container > aside.sidebar > nav.main-nav
```

### Skill 提问
```
关于这个导航菜单的标注：

1. 标注类型：
   - A) PRD feature 说明
   - B) 交互行为说明
   - C) 数据展示说明
   - D) 其他

2. 标注标题（一句话概括）：

3. 标注描述（详细说明）：
   提示：如果是 PRD feature，建议包含：
   - 功能说明（核心价值、目标用户）
   - 交互流程
   - 验收标准
```

### 用户回答
- **类型**: A) PRD feature 说明
- **标题**: 主导航菜单
- **描述**: 
  ```
  提供快速访问各功能模块的导航入口，支持一级和二级菜单展开收起
  ```

### 执行命令
```bash
prdkit mark create \
  --prototype "admin-dashboard" \
  --title "主导航菜单" \
  --selector "body > div.app-container > aside.sidebar > nav.main-nav" \
  --dom-path "body > div.app-container > aside.sidebar > nav.main-nav" \
  --desc "## 功能说明
提供快速访问各功能模块的导航入口，支持一级和二级菜单

## 交互流程
1. 点击一级菜单展开/收起二级菜单
2. 点击二级菜单跳转到对应页面
3. 当前页面菜单项高亮显示

## 验收标准
- [ ] 支持一级和二级菜单
- [ ] 当前页面菜单项高亮
- [ ] 无权限的菜单项不显示"
```

### 输出结果
```
✓ 已创建标记：mark-1777520000001
ℹ 原型：admin-dashboard
ℹ 文件：workspace/prototypes/admin-dashboard/marks/mark-1777520000001.md
ℹ 已创建 checkpoint：ckpt-1777520000002
```

---

## 示例 2：为表单创建交互行为标注

### 场景描述
设计师希望详细说明表单的交互行为。

### 用户输入
```
项目: 用户注册系统
文件路径: /Users/dave/workspace/prototypes/register
DOM 路径: body > div.container > form.register-form
```

### Skill 提问
```
关于这个注册表单的标注：

1. 标注类型：
   - A) PRD feature 说明
   - B) 交互行为说明
   - C) 数据展示说明

2. 标注标题：

3. 标注描述（详细说明交互细节）：
```

### 用户回答
- **类型**: B) 交互行为说明
- **标题**: 注册表单交互规则
- **描述**: 详细说明表单的校验、提示、提交等交互行为

### 执行命令
```bash
prdkit mark create \
  --prototype "register" \
  --title "注册表单交互规则" \
  --selector "body > div.container > form.register-form" \
  --dom-path "body > div.container > form.register-form" \
  --desc "## 交互说明
用户填写表单时实时校验，失焦时显示错误提示

## 校验规则
- **手机号**: 11位数字，失焦时校验
- **验证码**: 6位数字，60秒倒计时
- **密码**: 6-20位，包含字母和数字，显示强度提示
- **确认密码**: 与密码一致

## 提交流程
1. 点击提交按钮
2. 按钮显示加载状态，禁用所有输入
3. 提交成功跳转，失败显示错误提示

## 边界情况
- 网络异常: 显示「网络异常，请稍后重试」
- 手机号已注册: 显示「该手机号已注册，请直接登录」"
```

---

## 示例 3：为数据列表创建数据展示标注

### 场景描述
开发者希望明确数据列表的展示规则。

### 用户输入
```
项目: 订单管理系统
文件路径: /Users/eve/workspace/prototypes/order-list
DOM 路径: body > div.page > div.content > table.order-table
```

### Skill 提问
```
关于这个订单列表的标注：

1. 标注类型：
   - A) PRD feature 说明
   - B) 交互行为说明
   - C) 数据展示说明

2. 标注标题：

3. 标注描述（详细说明数据来源、格式、异常处理）：
```

### 用户回答
- **类型**: C) 数据展示说明
- **标题**: 订单列表数据展示规则
- **描述**: 说明订单数据的来源、格式化、排序、异常处理等

### 执行命令
```bash
prdkit mark create \
  --prototype "order-list" \
  --title "订单列表数据展示规则" \
  --selector "body > div.page > div.content > table.order-table" \
  --dom-path "body > div.page > div.content > table.order-table" \
  --desc "## 数据说明
来源: GET /api/orders，每次进入页面重新加载

## 展示规则
- 下单时间: YYYY-MM-DD HH:mm 格式
- 金额: ¥xxx.xx，千分位分隔
- 商品名称: 超过20字截断
- 状态: 标签样式（待支付/已支付/已发货/已完成/已取消）

## 排序和分页
- 默认按下单时间倒序
- 支持点击列头排序（时间、金额）
- 每页20条，底部分页器

## 异常处理
- 数据为空: 显示「暂无订单」
- 加载失败: 显示错误提示 + 重试按钮
- 字段为空: 显示「--」"
```

---

## 总结

这些示例展示了三种核心标注类型的使用场景：

1. **PRD Feature 标注**: 详细说明功能需求、交互流程、验收标准
2. **交互行为标注**: 详细描述交互细节、状态变化、边界情况
3. **数据展示标注**: 说明数据来源、格式化规则、异常处理

关键要点：
- 根据标注类型选择合适的内容结构
- 提供具体、可操作的信息
- 使用 Markdown 格式组织内容
- 考虑边界情况和异常处理
- 提供验收标准或成功标准
