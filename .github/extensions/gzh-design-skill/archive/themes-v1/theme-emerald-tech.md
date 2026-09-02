# 甲木公众号排版组件库 —— 绿色科技风

> **使用说明**：本组件库复刻自「龙虾住进微信聊天列表」文章的排版风格，使用**内联样式**，直接复制粘贴到微信公众号编辑器即可。
>
> **设计风格**：翡翠绿 + 编辑器/科技杂志风、卡片化布局、信息结构感强、标签化导航。
>
> **与天蓝/红黑色系的差异**：
> - 天蓝色系 → 轻盈、清透、散文感
> - 红黑色系 → 沉稳、力量、高级感
> - **绿色科技风** → **结构化、杂志感、产品评测风、信息密度高**

---

## 🎨 设计变量速查表

```
主色调：       #10B981（翡翠绿）
主色调深：     #059669
主色调浅：     #D1FAE5
主色调极浅：   #ECFDF5
标题色：       #1A1A1A（纯黑）
正文色：       #374151（深灰）
副文字色：     #9CA3AF（中灰）
极淡文字色：   #D1D5DB（浅灰，用于虚化副标题）
标签暗底：     #1A1A1A（近黑）
引用块背景：   #F5F5F5（极浅灰）
卡片边框：     #E5E7EB
分割线色：     #E5E7EB
荧光笔：       #FEF9C3（浅黄底）
正文字号：     15px
行高：         1.8
字间距：       0.5px
```

---

## 组件 1️⃣ 全局容器

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2️⃣ Hero 封面大卡片（本风格核心特色）

> 文章顶部的产品 Hero 卡片：主题标签 + 日期 + 标题（双色）+ 短横线 + 副标题 + 右侧图片 + 底部绿色 Banner

```html
<section style="margin:0 0 32px;border:1px solid #E5E7EB;border-radius:16px;overflow:hidden;box-shadow:0 2px 16px -4px rgba(0,0,0,0.06);">
  <!-- 顶部主题标签行 -->
  <section style="padding:20px 24px 0;">
    <section style="display:flex;align-items:center;justify-content:space-between;">
      <section style="display:flex;align-items:center;">
        <span style="display:inline-block;width:8px;height:8px;background:#10B981;border-radius:50%;margin-right:10px;vertical-align:middle;font-size:0;overflow:hidden;">.</span>
        <span style="font-size:12px;font-weight:700;color:#10B981;letter-spacing:4px;">WECHAT × AGENT</span>
      </section>
      <span style="font-size:13px;color:#D1D5DB;letter-spacing:1px;"><span leaf="">2026.03</span></span>
    </section>
    <!-- 绿色连接线 -->
    <section style="height:1px;background:linear-gradient(to right,#10B981 30%,#E5E7EB 30%);margin:10px 0 0;"></section>
  </section>
  <!-- 主内容区：标题 + 右侧图片 -->
  <section style="padding:20px 24px 24px;display:flex;justify-content:space-between;align-items:center;">
    <section style="flex:1;">
      <p style="font-size:14px;color:#D1D5DB;margin:0 0 8px;font-weight:400;">
        <span leaf="">AI 还要再装一个 App？</span>
      </p>
      <p style="font-size:28px;font-weight:900;color:#1A1A1A;margin:0;line-height:1.3;">
        <span leaf="">龙虾住进</span>
      </p>
      <p style="font-size:28px;font-weight:900;color:#10B981;margin:0 0 0;line-height:1.3;">
        <span leaf="">微信聊天列表</span>
      </p>
      <section style="width:40px;height:3px;background:#10B981;border-radius:2px;margin:16px 0;"></section>
      <p style="font-size:15px;color:#9CA3AF;margin:0;">
        <span leaf="">14亿用户的超级入口</span>
      </p>
    </section>
    <section style="flex-shrink:0;margin-left:16px;">
      <img src="图片URL" style="width:120px;height:120px;border-radius:16px;">
    </section>
  </section>
  <!-- 底部绿色 Banner 条 -->
  <section style="background:#10B981;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-size:14px;font-weight:700;color:#FFFFFF;"><span leaf="">官方原生插件</span></span>
    <section style="display:flex;">
      <span style="background:#1A1A1A;color:#FFFFFF;font-size:12px;font-weight:600;padding:4px 14px;border-radius:4px;margin-left:8px;"><span leaf="">ClawBot</span></span>
      <span style="background:#1A1A1A;color:#FFFFFF;font-size:12px;font-weight:600;padding:4px 14px;border-radius:4px;margin-left:8px;"><span leaf="">OpenClaw</span></span>
    </section>
  </section>
</section>
```

**简化版 Hero 卡片**（无右侧图片、无底部Banner，适用于一般文章）：

```html
<section style="margin:0 0 32px;border:1px solid #E5E7EB;border-radius:16px;overflow:hidden;box-shadow:0 2px 16px -4px rgba(0,0,0,0.06);padding:24px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <section style="display:flex;align-items:center;">
      <span style="display:inline-block;width:8px;height:8px;background:#10B981;border-radius:50%;margin-right:10px;vertical-align:middle;font-size:0;overflow:hidden;">.</span>
      <span style="font-size:12px;font-weight:700;color:#10B981;letter-spacing:4px;">TOPIC TAG</span>
    </section>
    <span style="font-size:13px;color:#D1D5DB;letter-spacing:1px;"><span leaf="">2026.03</span></span>
  </section>
  <p style="font-size:14px;color:#D1D5DB;margin:0 0 8px;">
    <span leaf="">副标题提问句</span>
  </p>
  <p style="font-size:26px;font-weight:900;color:#1A1A1A;margin:0;line-height:1.3;">
    <span leaf="">主标题前半</span>
  </p>
  <p style="font-size:26px;font-weight:900;color:#10B981;margin:0;line-height:1.3;">
    <span leaf="">主标题后半（绿色）</span>
  </p>
  <section style="width:40px;height:3px;background:#10B981;border-radius:2px;margin:16px 0;"></section>
  <p style="font-size:15px;color:#9CA3AF;margin:0;">
    <span leaf="">一句话概括</span>
  </p>
</section>
```

---

## 组件 3️⃣ 横向目录导航卡片

> Hero 卡片下方的结构化目录，三列卡片，第一个高亮绿色

```html
<!-- 面包屑索引行 -->
<section style="padding:0 10px;margin-bottom:12px;">
  <section style="display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:13px;color:#9CA3AF;margin:0;">
      <span leaf="">📋 01 实测 · 02 接入 · 最后</span>
    </p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;">
      <span leaf="">👉 横向滑动</span>
    </p>
  </section>
</section>
<!-- 三列目录卡片 -->
<section style="padding:0 10px 32px;display:flex;">
  <!-- 卡片1：绿色激活态 -->
  <section style="flex:1;background:#10B981;border-radius:12px;padding:16px;margin-right:8px;">
    <p style="font-size:11px;font-weight:700;color:rgba(255,255,255,0.7);letter-spacing:2px;margin:0 0 6px;">
      <span leaf="">PART 01</span>
    </p>
    <p style="font-size:16px;font-weight:800;color:#FFFFFF;margin:0 0 4px;">
      <span leaf="">实测案例</span>
    </p>
    <p style="font-size:12px;color:rgba(255,255,255,0.7);margin:0;">
      <span leaf="">5 场景 · AI 有多爽</span>
    </p>
  </section>
  <!-- 卡片2：白色默认态 -->
  <section style="flex:1;background:#FFFFFF;border:1px solid #E5E7EB;border-radius:12px;padding:16px;margin-right:8px;">
    <p style="font-size:11px;font-weight:700;color:#9CA3AF;letter-spacing:2px;margin:0 0 6px;">
      <span leaf="">PART 02</span>
    </p>
    <p style="font-size:16px;font-weight:800;color:#1A1A1A;margin:0 0 4px;">
      <span leaf="">接入教程</span>
    </p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;">
      <span leaf="">3 步搞定 · iOS</span>
    </p>
  </section>
  <!-- 卡片3：白色默认态 -->
  <section style="flex:1;background:#FFFFFF;border:1px solid #E5E7EB;border-radius:12px;padding:16px;">
    <p style="font-size:11px;font-weight:700;color:#9CA3AF;letter-spacing:2px;margin:0 0 6px;">
      <span leaf="">PART ///</span>
    </p>
    <p style="font-size:16px;font-weight:800;color:#1A1A1A;margin:0 0 4px;">
      <span leaf="">写在最后</span>
    </p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;">
      <span leaf="">Agent 入口之争</span>
    </p>
  </section>
</section>
```

---

## 组件 4️⃣ 章节标题（大号编号 + 竖线 + 标题）

> 左侧大号绿色编号 + PART 标签，竖线分隔，右侧标题 + 英文副标签

```html
<section style="padding:48px 20px 24px;">
  <section style="display:flex;align-items:flex-start;">
    <!-- 左侧编号区 -->
    <section style="margin-right:16px;flex-shrink:0;text-align:center;">
      <p style="font-size:36px;font-weight:900;color:#10B981;margin:0;line-height:1;">
        <span leaf="">01</span>
      </p>
      <p style="font-size:10px;font-weight:700;color:#10B981;letter-spacing:3px;margin:4px 0 0;">
        <span leaf="">PART</span>
      </p>
    </section>
    <!-- 竖线分隔 -->
    <section style="width:3px;background:#10B981;border-radius:2px;margin-right:16px;flex-shrink:0;min-height:50px;"></section>
    <!-- 右侧标题区 -->
    <section>
      <h3 style="font-size:18px;font-weight:800;color:#1A1A1A;margin:0 0 4px;letter-spacing:0.5px;">
        <span leaf="">实测：微信里的 AI 有多爽？</span>
      </h3>
      <p style="font-size:11px;color:#9CA3AF;margin:0;letter-spacing:2px;">
        <span style="font-weight:700;color:#10B981;"><span leaf="">CASES</span></span>
        <span leaf=""> · 5 场景实测</span>
      </p>
    </section>
  </section>
</section>
```

**结语章节变体**（用 `///` 替代数字编号）：

```html
<section style="padding:48px 20px 24px;">
  <section style="display:flex;align-items:flex-start;">
    <!-- 左侧 /// 标记 -->
    <section style="margin-right:16px;flex-shrink:0;text-align:center;">
      <p style="font-size:32px;font-weight:900;color:#10B981;margin:0;line-height:1;letter-spacing:-2px;">
        <span leaf="">///</span>
      </p>
      <p style="font-size:10px;font-weight:700;color:#10B981;letter-spacing:3px;margin:4px 0 0;">
        <span leaf="">LAST</span>
      </p>
    </section>
    <!-- 竖线分隔 -->
    <section style="width:3px;background:#10B981;border-radius:2px;margin-right:16px;flex-shrink:0;min-height:50px;"></section>
    <!-- 右侧标题区 -->
    <section>
      <h3 style="font-size:18px;font-weight:800;color:#1A1A1A;margin:0 0 4px;letter-spacing:0.5px;">
        <span leaf="">写在最后：Agent 入口之争</span>
      </h3>
      <p style="font-size:11px;color:#9CA3AF;margin:0;letter-spacing:2px;">
        <span style="font-weight:700;color:#10B981;"><span leaf="">INSIGHT</span></span>
        <span leaf=""> · 模型之外是分发</span>
      </p>
    </section>
  </section>
</section>
```

---

## 组件 5️⃣ 正文段落

> **⚠️ 关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**绿色下划线（6c）**进行标记。让读者快速扫到每段的重点。

**基础段落**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;padding:0 10px;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;padding:0 10px;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #10B981;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

---

## 组件 6️⃣ 正文高亮样式（5 种变体）

### 6a. 绿色加粗强调

```html
<strong style="color:#10B981;"><span leaf="">绿色加粗强调的关键句</span></strong>
```

### 6b. 黄色荧光笔高亮（本风格特色）

> 模拟黄色荧光笔标记效果，底部 40% 高亮

```html
<span style="background:linear-gradient(180deg, transparent 60%, #FEF9C3 60%);font-weight:700;color:#1A1A1A;"><span leaf="">荧光笔高亮的重要文字</span></span>
```

### 6c. 绿色下划线

```html
<span style="border-bottom:2px solid #10B981;"><span leaf="">下划线强调文字</span></span>
```

### 6d. 绿色渐变背景高亮

```html
<span style="background:linear-gradient(120deg,#D1FAE5 0%,rgba(255,255,255,0) 100%);padding:0 4px;border-radius:2px;font-weight:600;color:#1A1A1A;"><span leaf="">渐变背景关键词</span></span>
```

### 6e. 加粗正文段落

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;padding:0 10px;font-weight:700;color:#1A1A1A;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

---

## 组件 7️⃣ Case 子章节标题（标签式）

> 用于实测案例、步骤教程等子项目。绿色圆点 + 暗底编号标签 + 标题

```html
<section style="padding:0 10px;margin-bottom:8px;">
  <section style="display:flex;align-items:center;">
    <!-- 绿色空心圆 -->
    <span style="display:inline-block;width:12px;height:12px;border:2px solid #10B981;border-radius:50%;margin-right:12px;flex-shrink:0;font-size:0;overflow:hidden;">.</span>
    <!-- 暗底编号标签 -->
    <span style="background:#1A1A1A;color:#FFFFFF;font-size:11px;font-weight:700;padding:3px 10px;border-radius:4px;margin-right:10px;letter-spacing:1px;"><span leaf="">CASE 01</span></span>
    <!-- 标题 -->
    <span style="font-size:16px;font-weight:700;color:#1A1A1A;"><span leaf="">📎 微信原生文件，龙虾秒读</span></span>
  </section>
</section>
```

**Case 副标签**（标题下方的小字描述）：

```html
<section style="padding:0 10px;margin-bottom:16px;margin-left:24px;">
  <p style="font-size:12px;color:#10B981;margin:0;letter-spacing:1px;">
    <span leaf="">FILE · PDF 提案不打断心流</span>
  </p>
</section>
```

**场景描述**（绿色加粗的引导句）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;padding:0 10px;font-weight:600;color:#10B981;">
  <span leaf="">客户在微信上发了份 PDF 提案，你正在忙没空看</span>
</p>
```

---

## 组件 8️⃣ 暗色引用块（居中金句）

> 深灰底色 + 居中加粗金句，用于核心观点、引述

```html
<section style="padding:0 10px;margin-bottom:24px;">
  <section style="background:#F5F5F5;border-radius:12px;padding:24px 20px;">
    <p style="font-size:17px;font-weight:800;color:#1A1A1A;margin:0;line-height:1.8;text-align:center;">
      <span leaf="">「你不做，别人就会做。」</span>
    </p>
  </section>
</section>
```

**深色变体**（更强调）：

```html
<section style="padding:0 10px;margin-bottom:24px;">
  <section style="background:#1A1A1A;border-radius:12px;padding:24px 20px;">
    <p style="font-size:17px;font-weight:800;color:#FFFFFF;margin:0;line-height:1.8;text-align:center;">
      <span leaf="">「你不做，别人就会做。」</span>
    </p>
  </section>
</section>
```

---

## 组件 9️⃣ 产品/工具徽章列表

> 绿色圆点 + 绿色产品名（带浅绿色边框标签）+ 下方描述

```html
<section style="padding:0 10px;margin-bottom:20px;">
  <!-- 产品徽章 -->
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#ECFDF5;border:1px solid #D1FAE5;border-radius:6px;padding:2px 12px;font-size:14px;font-weight:700;color:#10B981;">
      <span leaf="">● QClaw</span>
    </span>
  </p>
  <!-- 产品描述 -->
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;">
    <span leaf="">本地 AI 助手，一键部署</span>
  </p>
</section>
```

多个产品连续排列：

```html
<section style="padding:0 10px;margin-bottom:20px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#ECFDF5;border:1px solid #D1FAE5;border-radius:6px;padding:2px 12px;font-size:14px;font-weight:700;color:#10B981;"><span leaf="">● QClaw</span></span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0 0 20px;line-height:1.8;">
    <span leaf="">本地 AI 助手，一键部署</span>
  </p>
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#ECFDF5;border:1px solid #D1FAE5;border-radius:6px;padding:2px 12px;font-size:14px;font-weight:700;color:#10B981;"><span leaf="">● WorkBuddy</span></span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0 0 20px;line-height:1.8;">
    <span leaf="">企业级 AI 工作平台</span>
  </p>
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#ECFDF5;border:1px solid #D1FAE5;border-radius:6px;padding:2px 12px;font-size:14px;font-weight:700;color:#10B981;"><span leaf="">● 腾讯云龙虾</span></span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;">
    <span leaf="">云端快捷配置</span>
  </p>
</section>
```

---

## 组件 🔟 绿色居中高亮句

> 用于章节结束前的点睛之笔，绿色加粗居中

```html
<p style="font-size:16px;font-weight:700;color:#10B981;text-align:center;margin:32px 20px;line-height:1.8;">
  <span leaf="">Agent 的日常化，可能就从这里开始</span>
</p>
```

---

## 组件 1️⃣1️⃣ 图片容器

```html
<section style="padding:0 10px;margin-bottom:24px;">
  <section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #F3F4F6;box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">
    <section style="margin:0;border-radius:8px;overflow:hidden;">
      <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
    </section>
  </section>
</section>
```

图片 + 说明文字：

```html
<section style="padding:0 10px;margin-bottom:8px;">
  <section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #F3F4F6;box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">
    <section style="margin:0;border-radius:8px;overflow:hidden;">
      <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
    </section>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

**多图并排**（手机截图场景）：

```html
<section style="padding:0 10px;margin-bottom:24px;display:flex;">
  <section style="flex:1;border-radius:12px;overflow:hidden;border:1px solid #F3F4F6;margin-right:6px;">
    <img src="截图1URL" style="max-width:100%;">
  </section>
  <section style="flex:1;border-radius:12px;overflow:hidden;border:1px solid #F3F4F6;margin-right:6px;">
    <img src="截图2URL" style="max-width:100%;">
  </section>
  <section style="flex:1;border-radius:12px;overflow:hidden;border:1px solid #F3F4F6;">
    <img src="截图3URL" style="max-width:100%;">
  </section>
</section>
```

---

## 组件 1️⃣2️⃣ 分割线

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:#E5E7EB;margin:8px 0;"></section>
</section>
```

渐变版本：

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #E5E7EB, transparent);margin:8px 0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 1️⃣3️⃣ 尾部 CTA 互动卡片（本风格特色）

> 圆角大卡片，居中文案 + 三个图标按钮 + THANKS FOR READING

```html
<section style="padding:0 10px;margin-top:32px;">
  <!-- 分割线 -->
  <section style="height:1px;background:#E5E7EB;margin:0 0 32px;"></section>
  <!-- CTA 卡片 -->
  <section style="border:1px solid #E5E7EB;border-radius:20px;padding:32px 24px;text-align:center;margin-bottom:32px;">
    <p style="font-size:17px;font-weight:700;color:#1A1A1A;margin:0 0 24px;line-height:1.6;">
      <span leaf="">觉得有用，随手点个赞、在看、转发三连吧</span>
    </p>
    <!-- 三个按钮 -->
    <section style="display:flex;justify-content:center;margin-bottom:8px;">
      <!-- 点赞 -->
      <section style="text-align:center;margin:0 16px;">
        <section style="width:48px;height:48px;background:#F5F5F5;border-radius:12px;margin:0 auto 6px;line-height:48px;font-size:22px;">
          <span leaf="">👍</span>
        </section>
        <p style="font-size:12px;color:#374151;margin:0;"><span leaf="">点赞</span></p>
      </section>
      <!-- 在看 -->
      <section style="text-align:center;margin:0 16px;">
        <section style="width:48px;height:48px;background:#F5F5F5;border-radius:12px;margin:0 auto 6px;line-height:48px;font-size:22px;">
          <span leaf="">👀</span>
        </section>
        <p style="font-size:12px;color:#374151;margin:0;"><span leaf="">在看</span></p>
      </section>
      <!-- 转发（绿色高亮） -->
      <section style="text-align:center;margin:0 16px;">
        <section style="width:48px;height:48px;background:#ECFDF5;border:1px solid #D1FAE5;border-radius:12px;margin:0 auto 6px;line-height:48px;font-size:22px;">
          <span leaf="">↗</span>
        </section>
        <p style="font-size:12px;color:#10B981;font-weight:600;margin:0;"><span leaf="">转发</span></p>
      </section>
    </section>
    <!-- THANKS FOR READING -->
    <p style="font-size:11px;color:#9CA3AF;letter-spacing:3px;margin:16px 0 0;">
      <span leaf="">THANKS FOR READING</span>
    </p>
  </section>
</section>
```

---

## 📐 完整文章模板骨架

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- ① Hero 封面大卡片 -->
  <!-- 组件2 -->

  <!-- ② 横向目录导航 -->
  <!-- 组件3 -->

  <!-- ③ 第一章 -->
  <!-- 组件4（章节标题 01 / PART） -->
  <!--   内部使用：
         - 组件5 正文段落
         - 组件6 高亮样式
         - 组件7 Case 子章节
         - 组件8 引用块
         - 组件11 图片
  -->

  <!-- ④ 第二章 -->
  <!-- 组件4（章节标题 02 / PART） -->

  <!-- ... 更多章节 ... -->

  <!-- ⑤ 结语章节 -->
  <!-- 组件4 结语变体（/// / LAST） -->
  <!--   内部使用：
         - 组件9 产品徽章列表
         - 组件8 暗色引用块
         - 组件10 绿色居中高亮句
  -->

  <!-- ⑥ 分割线 -->
  <!-- 组件12 -->

  <!-- ⑦ 绿色居中高亮句（结尾点睛） -->
  <!-- 组件10 -->

  <!-- ⑧ 分割线 -->
  <!-- 组件12 -->

  <!-- ⑨ 尾部 CTA 互动卡片 -->
  <!-- 组件13 -->

</section>
```

---

## 🔧 Markdown → 绿色科技风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| YAML frontmatter `title` / `subtitle` | 组件 2 Hero 卡片 | 提取标题拆分双色 |
| `## 章节标题` | 组件 4 章节标题 | 自动编号 01/02... 最后用 /// |
| `### Case 标题` | 组件 7 Case 子章节 | 带暗底编号标签 |
| 普通段落 | 组件 5 正文段落 | 默认样式 |
| `**加粗文字**` | 组件 6a 绿色加粗 | 变为绿色 #10B981 |
| `==高亮文字==` | 组件 6b 黄色荧光笔 | 底部黄色标记 |
| `> 引用段落` | 组件 8 暗色引用块 | 灰底居中金句 |
| `![](图片)` | 组件 11 图片容器 | 圆角卡片 |
| 产品列表 `- ● 名称` | 组件 9 产品徽章 | 绿色徽章标签 |
| `---` | 组件 12 分割线 | 实线或渐变 |
| 文末 | 组件 13 CTA 卡片 | 三连互动 |

---

## 🆚 三套主题风格对照

| 设计元素 | 天蓝色系 | 红黑色系 | **绿色科技风** |
|---|---|---|---|
| 主色 | `#0EA5E9` | `#DC2626` | **`#10B981`** |
| 文章开头 | 引号金句卡片 | 暗底金句卡片 | **Hero 封面大卡片** |
| 目录导航 | 三列编号文字 | 三列编号文字 | **三列彩色卡片** |
| 章节标题 | 英文标签 + 水印编号 | 英文标签 + 水印编号 | **大号编号 + 竖线 + 双行标题** |
| 子章节 | 无 | 无 | **Case 标签式标题** |
| 引用块 | 浅蓝渐变 | 暗底/浅红/左边线 | **灰底居中金句 / 黑底白字** |
| 产品列表 | 无 | 无 | **绿色徽章标签** |
| 荧光笔 | 蓝色底 | 红色底 | **黄色底** |
| 文章结尾 | END 渐变线 + 签名 | END 渐变线 + 签名 | **CTA 互动卡片 + 三连按钮** |
| 整体气质 | 散文、轻盈 | 沉稳、力量 | **杂志、结构、产品感** |
