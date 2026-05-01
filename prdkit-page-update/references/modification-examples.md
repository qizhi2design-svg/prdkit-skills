# 常见修改场景示例

本文档提供常见修改场景的最佳实践和代码示例。

## 场景分类

### 1. 文案和样式修改
### 2. 数据展示修改
### 3. 交互行为修改
### 4. 新增功能模块
### 5. 状态管理修改

---

## 场景 1：文案和样式修改

### 1.1 修改按钮文字

**用户需求**：将「立即体验」改为「开始使用」

**影响文件**：`index.html`

**修改步骤**：
```html
<!-- 修改前 -->
<button class="primary-cta" id="heroAction">立即体验</button>

<!-- 修改后 -->
<button class="primary-cta" id="heroAction">开始使用</button>
```

**注意事项**：
- 如果文字来自 mock.js，应该修改数据源而非 HTML
- 检查是否有其他地方引用了这个文字

### 1.2 修改按钮样式

**用户需求**：将按钮改为红色，增大尺寸

**影响文件**：`index.html`（内联样式）

**修改步骤**：
```html
<!-- 修改前 -->
<button class="primary-cta" id="heroAction">开始使用</button>

<!-- 修改后 -->
<button class="primary-cta" id="heroAction" style="
  background: #ef4444;
  padding: 14px 32px;
  font-size: 16px;
">开始使用</button>
```

**最佳实践**：
- 优先使用 class 而非内联样式
- 保持与页面整体风格一致

### 1.3 修改列表项文案

**用户需求**：修改功能列表的标题和描述

**影响文件**：`mock.js`

**修改步骤**：
```javascript
// 修改前
const mockData = {
  features: [
    { title: '快速上手', desc: '简单易用的界面' },
    { title: '功能强大', desc: '满足各种需求' }
  ]
};

// 修改后
const mockData = {
  features: [
    { title: '极速启动', desc: '3 秒完成配置，即刻开始使用' },
    { title: '全面覆盖', desc: '支持 20+ 种业务场景' }
  ]
};
```

**注意事项**：
- 修改数据后，视图会自动更新（如果使用了数据驱动渲染）
- 检查字段名是否在 script.js 中被引用

---

## 场景 2：数据展示修改

### 2.1 添加新的数据字段

**用户需求**：在商品卡片中显示库存数量

**影响文件**：`mock.js`、`index.html`、`script.js`

**修改步骤**：

1. **修改 mock.js**：
```javascript
// 修改前
const mockData = {
  products: [
    { id: 1, name: '商品 A', price: 99 },
    { id: 2, name: '商品 B', price: 199 }
  ]
};

// 修改后
const mockData = {
  products: [
    { id: 1, name: '商品 A', price: 99, stock: 50 },
    { id: 2, name: '商品 B', price: 199, stock: 0 }
  ]
};
```

2. **修改 index.html**（如果是静态渲染）：
```html
<!-- 修改前 -->
<div class="product-card">
  <h3>商品 A</h3>
  <p class="price">¥99</p>
</div>

<!-- 修改后 -->
<div class="product-card">
  <h3>商品 A</h3>
  <p class="price">¥99</p>
  <p class="stock">库存：50</p>
</div>
```

3. **修改 script.js**（如果是动态渲染）：
```javascript
// 修改前
function renderProducts() {
  return mockData.products.map(p => `
    <div class="product-card">
      <h3>${p.name}</h3>
      <p class="price">¥${p.price}</p>
    </div>
  `).join('');
}

// 修改后
function renderProducts() {
  return mockData.products.map(p => `
    <div class="product-card">
      <h3>${p.name}</h3>
      <p class="price">¥${p.price}</p>
      <p class="stock" style="color: ${p.stock > 0 ? '#22c55e' : '#ef4444'}">
        库存：${p.stock > 0 ? p.stock : '缺货'}
      </p>
    </div>
  `).join('');
}
```

### 2.2 修改数据的显示格式

**用户需求**：将价格显示为千分位格式

**影响文件**：`script.js`

**修改步骤**：
```javascript
// 添加格式化函数
function formatPrice(price) {
  return price.toLocaleString('zh-CN');
}

// 修改渲染函数
function renderProducts() {
  return mockData.products.map(p => `
    <div class="product-card">
      <h3>${p.name}</h3>
      <p class="price">¥${formatPrice(p.price)}</p>
    </div>
  `).join('');
}
```

---

## 场景 3：交互行为修改

### 3.1 添加按钮点击事件

**用户需求**：点击按钮显示提示信息

**影响文件**：`script.js`

**修改步骤**：
```javascript
// 1. 定义事件处理函数
function handleButtonClick() {
  alert('按钮被点击了！');
}

// 2. 绑定事件监听器
document.getElementById('myButton').addEventListener('click', handleButtonClick);
```

**最佳实践**：
```javascript
// 更好的方式：添加视觉反馈
function handleButtonClick(event) {
  const button = event.target;
  
  // 添加点击反馈
  button.style.transform = 'scale(0.95)';
  setTimeout(() => {
    button.style.transform = 'scale(1)';
  }, 150);
  
  // 执行业务逻辑
  alert('按钮被点击了！');
}
```

### 3.2 修改点击后的跳转行为

**用户需求**：点击商品卡片跳转到详情页

**影响文件**：`script.js`

**修改步骤**：
```javascript
// 为每个商品卡片添加点击事件
function bindProductClick() {
  document.querySelectorAll('.product-card').forEach((card, index) => {
    card.addEventListener('click', () => {
      const product = mockData.products[index];
      // 原型中模拟跳转
      alert(`即将查看商品详情：${product.name}`);
      // 实际项目中：window.location.href = `/product/${product.id}`;
    });
    
    // 添加鼠标悬停效果
    card.style.cursor = 'pointer';
  });
}

// 在初始化时调用
bindProductClick();
```

### 3.3 添加表单验证

**用户需求**：提交表单前验证输入

**影响文件**：`script.js`

**修改步骤**：
```javascript
function handleFormSubmit(event) {
  event.preventDefault(); // 阻止默认提交
  
  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  
  // 验证用户名
  if (!username || username.length < 3) {
    alert('用户名至少 3 个字符');
    return;
  }
  
  // 验证邮箱
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    alert('请输入有效的邮箱地址');
    return;
  }
  
  // 验证通过
  alert('提交成功！');
  // 实际项目中：提交到服务器
}

document.getElementById('myForm').addEventListener('submit', handleFormSubmit);
```

---

## 场景 4：新增功能模块

### 4.1 添加弹窗

**用户需求**：点击按钮打开弹窗

**影响文件**：`index.html`、`script.js`、`mock.js`

**修改步骤**：

1. **修改 index.html**：
```html
<!-- 添加弹窗 HTML -->
<div id="modal" style="
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.5);
  z-index: 1000;
  align-items: center;
  justify-content: center;
">
  <div style="
    background: white;
    padding: 24px;
    border-radius: 8px;
    max-width: 400px;
    width: 90%;
  ">
    <h3>弹窗标题</h3>
    <p>弹窗内容</p>
    <button id="closeModal">关闭</button>
  </div>
</div>
```

2. **修改 script.js**：
```javascript
// 打开弹窗
function openModal() {
  const modal = document.getElementById('modal');
  modal.style.display = 'flex';
}

// 关闭弹窗
function closeModal() {
  const modal = document.getElementById('modal');
  modal.style.display = 'none';
}

// 绑定事件
document.getElementById('openModalBtn').addEventListener('click', openModal);
document.getElementById('closeModal').addEventListener('click', closeModal);

// 点击遮罩关闭
document.getElementById('modal').addEventListener('click', (e) => {
  if (e.target.id === 'modal') {
    closeModal();
  }
});
```

### 4.2 添加 Tab 切换

**用户需求**：添加 Tab 导航，切换显示不同内容

**影响文件**：`index.html`、`script.js`、`mock.js`

**修改步骤**：

1. **修改 mock.js**：
```javascript
const mockData = {
  state: {
    activeTab: 'tab1'
  },
  tabs: [
    { id: 'tab1', label: '选项一', content: '这是选项一的内容' },
    { id: 'tab2', label: '选项二', content: '这是选项二的内容' },
    { id: 'tab3', label: '选项三', content: '这是选项三的内容' }
  ]
};
```

2. **修改 index.html**：
```html
<div class="tabs">
  <div class="tab-nav" id="tabNav"></div>
  <div class="tab-content" id="tabContent"></div>
</div>
```

3. **修改 script.js**：
```javascript
function renderTabs() {
  const { tabs } = mockData;
  const { activeTab } = mockData.state;
  
  // 渲染 Tab 导航
  const navHTML = tabs.map(tab => `
    <button 
      class="tab-btn ${tab.id === activeTab ? 'active' : ''}"
      data-tab="${tab.id}"
    >
      ${tab.label}
    </button>
  `).join('');
  document.getElementById('tabNav').innerHTML = navHTML;
  
  // 渲染 Tab 内容
  const activeTabData = tabs.find(t => t.id === activeTab);
  document.getElementById('tabContent').innerHTML = `
    <div class="tab-panel">${activeTabData.content}</div>
  `;
  
  // 绑定点击事件
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      mockData.state.activeTab = btn.dataset.tab;
      renderTabs();
    });
  });
}

// 初始化
renderTabs();
```

---

## 场景 5：状态管理修改

### 5.1 添加加载状态

**用户需求**：点击按钮后显示加载状态

**影响文件**：`script.js`、`mock.js`

**修改步骤**：

1. **修改 mock.js**：
```javascript
const mockData = {
  state: {
    loading: false
  }
};
```

2. **修改 script.js**：
```javascript
function handleSubmit() {
  const button = document.getElementById('submitBtn');
  
  // 设置加载状态
  mockData.state.loading = true;
  button.disabled = true;
  button.textContent = '加载中...';
  
  // 模拟异步操作
  setTimeout(() => {
    mockData.state.loading = false;
    button.disabled = false;
    button.textContent = '提交';
    alert('操作完成！');
  }, 2000);
}
```

### 5.2 添加选中状态

**用户需求**：点击列表项高亮选中

**影响文件**：`script.js`、`mock.js`

**修改步骤**：

1. **修改 mock.js**：
```javascript
const mockData = {
  state: {
    selectedId: null
  },
  items: [
    { id: 1, name: '项目 A' },
    { id: 2, name: '项目 B' },
    { id: 3, name: '项目 C' }
  ]
};
```

2. **修改 script.js**：
```javascript
function renderItems() {
  const { items } = mockData;
  const { selectedId } = mockData.state;
  
  const html = items.map(item => `
    <div 
      class="item ${item.id === selectedId ? 'selected' : ''}"
      data-id="${item.id}"
      style="
        padding: 12px;
        cursor: pointer;
        background: ${item.id === selectedId ? '#e0e7ff' : 'white'};
        border: 1px solid ${item.id === selectedId ? '#4f46e5' : '#e5e7eb'};
        margin-bottom: 8px;
        border-radius: 4px;
      "
    >
      ${item.name}
    </div>
  `).join('');
  
  document.getElementById('itemList').innerHTML = html;
  
  // 绑定点击事件
  document.querySelectorAll('.item').forEach(el => {
    el.addEventListener('click', () => {
      mockData.state.selectedId = parseInt(el.dataset.id);
      renderItems();
    });
  });
}

// 初始化
renderItems();
```

---

## 最佳实践总结

### 代码组织
1. **数据驱动**：优先修改 mock.js，让视图自动更新
2. **函数命名**：使用清晰的命名（如 `handleButtonClick`、`renderProducts`）
3. **事件绑定**：集中在初始化函数中绑定事件

### 修改顺序
1. 先修改数据层（mock.js）
2. 再修改逻辑层（script.js）
3. 最后修改视图层（index.html）

### 代码风格
1. 保持与现有代码一致的缩进和命名
2. 添加必要的注释说明修改意图
3. 使用模板字符串而非字符串拼接

### 测试验证
1. 修改后立即在浏览器中测试
2. 检查控制台是否有错误
3. 测试边界情况（空数据、极端值等）

### 版本管理
1. 重要修改前创建备份 checkpoint
2. 修改完成后创建新 checkpoint
3. checkpoint 消息要简短描述修改内容
