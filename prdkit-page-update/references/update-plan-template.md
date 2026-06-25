# 改造计划模板

改造计划保存在 `draft/reference/<page-name>-update-plan.md`，用于记录修改意图、影响范围和具体步骤。

## 模板结构

```markdown
# [页面名称] 修改计划

**创建时间**：2026-05-01 14:00  
**目标页面**：workspace/prototypes/mobile-demo/index.html  
**修改类型**：数据修改 / 交互逻辑 / 新增功能

---

## 修改目标

简短描述要达成的效果（1-2 句话）。

示例：
- 将「立即体验」按钮改为「开始使用」，点击后跳转到功能介绍页面
- 为商品列表添加筛选功能，支持按价格和分类筛选
- 修改用户头像显示逻辑，支持默认头像占位

---

## 目标元素信息

### 选中元素
- **选择器**：`button#heroAction.primary-cta`
- **标签**：`<button>`
- **ID**：`heroAction`
- **类名**：`primary-cta`
- **当前文本**：「立即体验」
- **当前 HTML**：
  ```html
  <button class="primary-cta" id="heroAction">立即体验</button>
  ```

### 关联元素
（如果有多个元素或关联元素，在此列出）

---

## 修改意图确认

### 数据修改
- [ ] 需要修改 mock.js
- [ ] 需要新增数据字段
- [ ] 需要调整数据结构

**具体内容**：
- 按钮文字改为「开始使用」
- 无需修改 mock.js 数据

### 交互逻辑
- [x] 需要修改 script.js
- [x] 需要添加事件监听
- [ ] 需要调整状态管理

**具体内容**：
- 添加按钮点击事件监听
- 点击后跳转到功能介绍页面（模拟跳转，显示提示）
- 添加点击反馈动画

### 新增功能
- [ ] 需要添加新的 HTML 元素
- [ ] 需要新增功能模块
- [ ] 需要添加新的交互入口

**具体内容**：
- 无需新增功能

---

## 影响范围

### 涉及文件
- [x] `index.html` - 修改按钮文字
- [x] `script.js` - 添加点击事件处理
- [ ] `mock.js` - 无需修改
- [ ] `style.css` - 可选：添加点击反馈样式

### 影响的代码块
- `index.html` 第 45 行：按钮元素
- `script.js` 新增：`handleHeroAction` 函数
- `script.js` 新增：事件监听器绑定

---

## 修改清单

### 1. 修改 index.html

**位置**：第 45 行

**修改前**：
```html
<button class="primary-cta" id="heroAction">立即体验</button>
```

**修改后**：
```html
<button class="primary-cta" id="heroAction">开始使用</button>
```

### 2. 修改 script.js

**位置**：事件监听器部分（约第 20 行）

**新增代码**：
```javascript
// 处理主按钮点击
function handleHeroAction() {
  const button = document.getElementById('heroAction');
  
  // 添加点击反馈
  button.style.transform = 'scale(0.95)';
  setTimeout(() => {
    button.style.transform = 'scale(1)';
  }, 150);
  
  // 模拟跳转
  setTimeout(() => {
    alert('即将跳转到功能介绍页面');
    // 实际项目中这里应该是：window.location.href = '/features';
  }, 200);
}

// 绑定事件监听器
document.getElementById('heroAction').addEventListener('click', handleHeroAction);
```

### 3. 修改 mock.js（可选）

**位置**：无需修改

---

## 视觉效果说明

### 修改前
- 按钮显示「立即体验」
- 点击无反应

### 修改后
- 按钮显示「开始使用」
- 点击时按钮缩小（scale 0.95）
- 150ms 后恢复原大小
- 200ms 后显示跳转提示

---

## 风险点和注意事项

### 潜在风险
- 如果页面中有多个按钮使用相同的样式，需要确保只影响目标按钮
- 事件监听器需要在 DOM 加载完成后绑定

### 注意事项
- 保持代码风格与现有代码一致
- 点击反馈动画使用 CSS transition 更流畅
- 跳转逻辑在原型中使用 alert 模拟，实际项目需要替换

### 兼容性
- 使用的 API（getElementById、addEventListener）兼容所有现代浏览器
- transform 动画需要添加 transition 样式

---

## 待确认项

- [ ] 跳转动画效果（当前假设：淡入淡出）
- [ ] 是否需要添加加载状态
- [ ] 是否需要在跳转前进行数据验证

---

## 验收标准

- [x] 按钮文字显示为「开始使用」
- [x] 点击按钮有视觉反馈（缩放动画）
- [x] 点击后显示跳转提示
- [ ] 在移动端和桌面端都能正常工作
- [ ] 不影响页面其他功能

---

## 执行步骤

1. 备份当前版本（可选）
   ```bash
   prdkit checkpoint create mobile-demo --message "修改前备份"
   ```

2. 修改 index.html（按钮文字）

3. 修改 script.js（添加事件处理）

4. 测试功能（在浏览器中验证）

5. 创建 checkpoint
   ```bash
   prdkit checkpoint create mobile-demo --message "修改：主按钮改为「开始使用」并添加跳转逻辑"
   ```

6. 预览验证
   ```bash
   prdkit serve status  # 检查服务状态
   prdkit serve         # 如果没有运行则启动
   ```

---

## 备注

- 当前处于第二阶段，尚未执行修改
- 等待用户确认后进入第三阶段
```

## 使用说明

### 何时创建计划
- 在第二阶段，明确修改意图后立即创建
- 在执行修改前必须有计划文档

### 计划的作用
1. **沟通工具**：让用户清楚了解将要进行的修改
2. **执行指南**：第三阶段按计划逐步执行
3. **版本记录**：记录修改的原因和过程

### 计划的粒度
- **简单修改**（如改文字、调样式）：计划可以简化，重点在影响范围
- **复杂修改**（如新增功能、重构逻辑）：计划要详细，包含完整的代码示例
- **批量修改**（如修改多个元素）：按元素分组，每组一个修改清单

### 计划的更新
- 用户提出新的修改需求时，更新现有计划
- 执行过程中发现问题时，在备注中记录调整
- 修改完成后，标记验收标准的完成状态

## 常见场景的计划示例

### 场景 1：纯文案修改

```markdown
## 修改目标
将导航栏的「首页」改为「工作台」

## 影响范围
- `index.html` 第 12 行

## 修改清单
1. 修改 index.html 第 12 行
   - 修改前：`<a href="#home">首页</a>`
   - 修改后：`<a href="#home">工作台</a>`

## 风险点
- 无

## 执行步骤
1. 修改 index.html
2. 创建 checkpoint
```

### 场景 2：添加交互功能

```markdown
## 修改目标
为商品列表添加「加入购物车」按钮，点击后显示成功提示

## 影响范围
- `index.html` - 添加按钮
- `script.js` - 添加点击事件处理
- `mock.js` - 添加购物车数据结构

## 修改清单
1. 修改 mock.js：添加 `cart` 数组
2. 修改 index.html：在每个商品卡片中添加按钮
3. 修改 script.js：添加 `addToCart` 函数和事件监听

## 风险点
- 需要确保购物车数据结构与商品数据结构匹配
- 多次点击需要处理数量累加逻辑
```

### 场景 3：状态切换

```markdown
## 修改目标
为 Tab 导航添加切换功能，点击不同 Tab 显示对应内容

## 影响范围
- `index.html` - 添加内容区域
- `script.js` - 添加 Tab 切换逻辑
- `mock.js` - 添加 `state.activeTab` 状态

## 修改清单
1. 修改 mock.js：添加 `state.activeTab = 'tab1'`
2. 修改 index.html：为每个 Tab 添加 `data-tab` 属性
3. 修改 script.js：添加 `switchTab` 函数和渲染逻辑

## 风险点
- 需要确保初始状态与默认 Tab 一致
- 切换时需要更新 Tab 的激活样式
```
