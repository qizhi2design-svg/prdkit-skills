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

## 样式框架

### 使用 Tailwind CSS

**在 HTML 的 `<head>` 中引入 Tailwind CSS CDN：**

```html
<script src="https://cdn.tailwindcss.com"></script>
```

**配置自定义主题（可选）：**

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: '#4f46e5',
          secondary: '#06b6d4',
        }
      }
    }
  }
</script>
```

**使用 Tailwind 工具类：**

```html
<!-- 按钮示例 -->
<button class="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-lg transition-colors">
  提交
</button>

<!-- 卡片示例 -->
<div class="bg-white rounded-lg shadow-md p-6 space-y-4">
  <h3 class="text-lg font-semibold text-gray-900">标题</h3>
  <p class="text-gray-600">内容描述</p>
</div>

<!-- 响应式布局示例 -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <!-- 网格项 -->
</div>
```

### 常用 Tailwind 类映射

| 功能 | Tailwind 类 |
|------|------------|
| 容器居中 | `mx-auto` |
| 内边距 | `p-4` (16px), `p-6` (24px), `p-8` (32px) |
| 外边距 | `m-4`, `mt-4`, `mb-4`, `mx-4`, `my-4` |
| 圆角 | `rounded` (4px), `rounded-lg` (8px), `rounded-xl` (12px) |
| 阴影 | `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg` |
| 文字大小 | `text-sm`, `text-base`, `text-lg`, `text-xl` |
| 文字颜色 | `text-gray-900`, `text-blue-500`, `text-white` |
| 背景色 | `bg-white`, `bg-gray-100`, `bg-blue-500` |
| Flex 布局 | `flex`, `flex-col`, `items-center`, `justify-between` |
| Grid 布局 | `grid`, `grid-cols-3`, `gap-4` |

## 画布规范

### PC 页面
- 基准：`1440 x 900`
- 容器：`<div class="w-[1440px] min-h-[900px] mx-auto">`
- 导航高度：`h-14` (56px) 或 `h-16` (64px)
- 左右留白：`px-6` (24px) 或 `px-8` (32px)
- 模块间距：`space-y-4` (16px) 或 `space-y-6` (24px)

### 移动端页面
- 基准：`390 x 844`
- 容器：`<div class="w-[390px] min-h-[844px]">`
- 左右留白：`px-4` (16px) 或 `px-5` (20px)
- 模块间距：`space-y-4` (16px) 或 `space-y-6` (24px)
- 底部操作条/tab：`h-14` (56px) 或 `h-16` (64px)

## 图标规范

### 使用 Font Awesome

**在 HTML 的 `<head>` 中引入 Font Awesome CDN：**

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
```

**使用图标：**

```html
<!-- 实心图标 (Solid) -->
<i class="fas fa-search"></i>
<i class="fas fa-plus"></i>
<i class="fas fa-user"></i>

<!-- 常规图标 (Regular) -->
<i class="far fa-heart"></i>
<i class="far fa-star"></i>

<!-- 品牌图标 (Brands) -->
<i class="fab fa-github"></i>
<i class="fab fa-twitter"></i>
```

**结合 Tailwind 控制尺寸和颜色：**

```html
<!-- 小图标 (14px) -->
<i class="fas fa-search text-sm text-gray-500"></i>

<!-- 常规图标 (16px) -->
<i class="fas fa-plus text-base text-blue-500"></i>

<!-- 大图标 (24px) -->
<i class="fas fa-image text-2xl text-gray-400"></i>

<!-- 带背景的图标按钮 -->
<button class="w-10 h-10 flex items-center justify-center bg-blue-500 text-white rounded-lg hover:bg-blue-600">
  <i class="fas fa-plus"></i>
</button>
```

### 尺寸规范
- 小 (14px)：`text-sm` - 表格、列表
- 常规 (16px)：`text-base` - 按钮、导航
- 大 (24px)：`text-2xl` - 空状态、引导页
- 超大 (32px)：`text-4xl` - 特殊强调

### 常用图标映射

| 功能 | Font Awesome 类 |
|------|----------------|
| 搜索 | `fas fa-search` |
| 添加 | `fas fa-plus` |
| 删除 | `fas fa-trash` |
| 编辑 | `fas fa-edit` |
| 设置 | `fas fa-cog` |
| 用户 | `fas fa-user` |
| 首页 | `fas fa-home` |
| 菜单 | `fas fa-bars` |
| 关闭 | `fas fa-times` |
| 勾选 | `fas fa-check` |
| 箭头右 | `fas fa-arrow-right` |
| 箭头下 | `fas fa-chevron-down` |
| 心形 | `far fa-heart` / `fas fa-heart` |
| 星星 | `far fa-star` / `fas fa-star` |
| 图片 | `fas fa-image` |
| 文件 | `fas fa-file` |
| 下载 | `fas fa-download` |
| 上传 | `fas fa-upload` |

### 注意事项
- 禁止使用 emoji
- 优先使用 Solid 样式 (`fas`)，需要轮廓样式时使用 Regular (`far`)
- 图标与文字混排时注意垂直对齐：`inline-flex items-center`

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

### 使用 Tailwind 实现图片占位

```html
<!-- 封面 -->
<div class="w-full h-[200px] bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white text-sm rounded-lg">
  封面图片
</div>

<!-- 头像 -->
<div class="w-12 h-12 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 text-xs">
  头像
</div>

<!-- 商品图 -->
<div class="w-20 h-20 bg-gray-100 rounded flex items-center justify-center text-gray-400 text-xs">
  图片
</div>

<!-- Logo -->
<div class="w-16 h-16 bg-amber-100 rounded-lg flex items-center justify-center text-amber-500 text-xs font-medium">
  Logo
</div>
```

## 实现要点

- 以 prdkit 模板为基线
- **优先使用 Tailwind CSS 工具类**，避免编写自定义 CSS
- **使用 Font Awesome 图标**，不使用其他图标库
- 先搭 HTML 结构和交互，再细化视觉
- 页面内部不使用 `z-index: 9999`（预留给 viewer）
- 需求不完整时使用稳妥默认值，并记录假设
