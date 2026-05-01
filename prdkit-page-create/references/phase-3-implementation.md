# 第三阶段：实现规范

## 视觉参数

### 必填字段

- 平台类型：`mobile` | `admin` | `web`
- 画布规格：`390 x 844` | `1440 x 900` | 自定义（需写原因）
- 气质方向：高效 | 专业 | 友好 | 鲜明 | 克制
- 信息密度：低 | 中 | 高
- 主色、强调色
- 圆角大小：小 | 中 | 大
- 阴影强度：无 | 轻 | 中

### UX 规则

- 主操作按钮足够突出
- 首屏回答"我在哪"和"下一步做什么"
- 明确空状态、加载态、错误态
- 后台页面保证层级清晰、对齐稳定
- 移动端关键操作落在拇指易触达区域

## 画布规范

### PC 页面
- 基准：`1440 x 900`
- 容器：`width: 1440px; min-height: 900px; margin: 0 auto`
- 导航高度：`56-64px`
- 左右留白：`24-32px`
- 模块间距：`16-24px`

### 移动端页面
- 基准：`390 x 844`
- 容器：`width: 390px; min-height: 844px`
- 左右留白：`16-20px`
- 模块间距：`16-24px`
- 底部操作条/tab：`56-64px`

## 图标规范

### 使用 Lucide Icons

```html
<script src="https://unpkg.com/lucide@latest"></script>
<script>lucide.createIcons();</script>

<!-- 使用 -->
<i data-lucide="search"></i>
<i data-lucide="plus" style="width: 16px; height: 16px;"></i>
```

### 尺寸
- 小 (14px)：表格、列表
- 常规 (16px)：按钮、导航
- 大 (24px)：空状态、引导页

### 注意
- 禁止使用 emoji
- 动态添加后需重新调用 `lucide.createIcons()`

## 图片占位

### 原则
- **禁止使用真实图片链接**（unsplash、placeholder.com 等）
- **统一使用纯色背景 + 文字标注**

### 颜色方案

| 类型 | 背景色 | 文字色 |
|------|--------|--------|
| 封面/Banner | 渐变 `#667eea → #764ba2` | `#ffffff` |
| 头像 | `#e0e7ff` | `#4f46e5` |
| 商品图 | `#f3f4f6` | `#9ca3af` |
| Logo | `#fef3c7` | `#f59e0b` |

### 示例代码

```html
<!-- 封面 -->
<div style="width: 100%; height: 200px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; color: white; font-size: 14px; border-radius: 8px;">封面图片</div>

<!-- 头像 -->
<div style="width: 48px; height: 48px; background: #e0e7ff; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #4f46e5; font-size: 12px;">头像</div>

<!-- 商品图 -->
<div style="width: 80px; height: 80px; background: #f3f4f6; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #9ca3af; font-size: 12px;">图片</div>
```

## 实现要点

- 以 prdkit 模板为基线
- 先搭 HTML 结构和交互，再细化视觉
- 页面内部不使用 `z-index: 9999`（预留给 viewer）
- 需求不完整时使用稳妥默认值，并记录假设
