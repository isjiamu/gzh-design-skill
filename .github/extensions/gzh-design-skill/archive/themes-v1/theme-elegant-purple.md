# 甲木公众号排版组件库 —— 紫色优雅风

> **使用说明**：本组件库为「紫色优雅风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：优雅、创意、神秘感、高端品味。以紫色为主色调，白底为主基调，留白充足，强调细腻的视觉美感与优雅的阅读节奏。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>` 标签、`<script>` 标签、CSS class
> - ❌ 不支持 `position: fixed/absolute`、`float`
> - ❌ 不支持 `@media` 媒体查询、`@keyframes` 动画
> - ❌ 不支持 `display: grid`
> - ✅ 支持内联 `style` 属性
> - ✅ 支持 `display: flex`（有限支持）
> - ✅ 支持 `linear-gradient`
> - ✅ 支持 `border-radius`、`box-shadow`
> - ✅ 支持 `<section>`、`<p>`、`<span>`、`<strong>`、`<img>` 等基础标签

---

## 🎨 设计变量速查表

```
主色调：       #7C3AED（紫色）
主色调深：     #5B21B6（深紫）
主色调浅：     #C4B5FD（浅紫）
主色调极浅：   #EDE9FE（淡紫）
主色调背景：   #F5F3FF（极淡紫底）
标题色：       #1E1B4B（深紫蓝）
正文色：       #374151（深灰）
辅助文字色：   #9CA3AF（中灰）
分割线色：     #E5E7EB
边框色：       #F3F4F6
正文字号：     15px
行高：         1.8
字间距：       0.5px
```

---

## 组件 1️⃣ 全局容器

> 最外层包裹，定义字体、颜色、行高等全局样式。背景白色，整体风格优雅精致。

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.8;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2️⃣ 开头引言卡片

> 白底 + 紫色左边框 5px + 大号紫色引号 + 金句正文（关键词用主色实底白字标签高亮）+ 右下署名。优雅开场，灵感与品味并存。

```html
<section style="margin:0 0 32px;background:#ffffff;border-left:5px solid #7C3AED;border-radius:4px 16px 16px 4px;box-shadow:0 4px 20px -4px rgba(124,58,237,0.10);padding:28px 24px 22px;overflow:hidden;">
  <p style="font-size:42px;color:#7C3AED;font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:800;color:#1E1B4B;margin:12px 0 8px;line-height:1.75;padding-left:4px;">
    <span leaf="">创意的本质，不在于灵光一现的 </span>
    <span style="background:#7C3AED;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">天赋</span></span>
    <span leaf=""> ，而在于持续打磨 </span>
    <span style="background:#7C3AED;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">审美直觉</span></span>
    <span leaf=""> 的过程。</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#9CA3AF;margin:8px 0 0;letter-spacing:1px;">
    <span leaf="">—— 甲木</span>
  </p>
</section>
```

**效果**：白底干净雅致，紫色左边框优雅有力，紫底白字标签做精准点睛，整体透出高端品味。

---

## 组件 3️⃣ 前言导读区域（三列目录卡片）

> 三列 flex 布局。每列有：主色实底白字编号标签(01/02/03) + 深色标题。背景用极浅紫色，传递优雅的阅读路径。

```html
<section style="padding: 0 10px 32px;">
  <p style="font-size: 14px;color: #9CA3AF;margin: 0 0 14px;letter-spacing:1px;">
    <span leaf="">📌 本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #EDE9FE;">
      <p style="display:inline-block;background:#7C3AED;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#1E1B4B;margin:0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #EDE9FE;">
      <p style="display:inline-block;background:#7C3AED;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#1E1B4B;margin:0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:16px 12px;text-align:center;border:1px solid #EDE9FE;">
      <p style="display:inline-block;background:#7C3AED;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#1E1B4B;margin:0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4️⃣ 章节分割线

> 紫色渐变分割线：transparent → 浅紫 → 紫色 → 浅紫 → transparent。两端渐隐，优雅而精致。

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #C4B5FD, #7C3AED, #C4B5FD, transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5️⃣ 章节标题

> 左侧主色实底白字编号标签 + 英文小标签(紫色) + 中文大标题(深紫蓝)。底部 3px 紫色线。风格优雅大气。

```html
<section style="margin-top: 48px;margin-bottom: 28px;padding: 0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #7C3AED;">
    <section style="display:flex;align-items:center;">
      <!-- 紫色底编号标签 -->
      <span style="display:inline-block;background:#7C3AED;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#7C3AED;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#1E1B4B;margin:0;letter-spacing:0.5px;">
          <span leaf="">中文章节标题</span>
        </h3>
      </section>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（编号用 ∞ 替代数字）：

```html
<span style="display:inline-block;background:#7C3AED;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6️⃣ 正文段落

> **⚠️ 关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**紫色下划线（7d）**进行标记。这是本风格的核心视觉特征——让读者快速扫到每段的重点。

**基础段落**（无标记时）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。保持优雅细腻的阅读节奏。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #7C3AED;font-weight:600;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。整体保持</span>
  <span style="border-bottom:2px solid #7C3AED;font-weight:600;"><span leaf="">优雅细腻</span></span>
  <span leaf="">的表达节奏。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标

---

## 组件 7️⃣ 正文高亮样式（6 种变体 + 使用优先级）

> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 紫色下划线** ⭐ — 正文默认标记方式，每段都应考虑使用
> 2. **7a 紫色加粗** — 关键结论句
> 3. **7b 紫色实底白字标签** — 极少数最核心的概念（每篇 2~4 个）
> 4. **7c 淡紫背景** — 次要关键词补充
> 5. **7e 荧光笔** — 偶尔用于长句强调
> 6. **7f 粗下划线** — 全文最重要的一句话

### 7a. 紫色加粗强调

```html
<strong style="color:#7C3AED;"><span leaf="">紫色加粗强调</span></strong>
```

### 7b. 紫色实底白字标签高亮

> 白字紫底，像标签贴纸一样醒目，仅用于最核心的概念（每篇 2~4 个）

```html
<span style="background:#7C3AED;color:#FFFFFF;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 淡紫背景高亮

> 柔和的背景标注，适用于次要关键词

```html
<span style="background:#EDE9FE;padding:1px 6px;border-radius:3px;font-weight:600;color:#5B21B6;"><span leaf="">淡紫背景关键词</span></span>
```

### 7d. 紫色下划线 ⭐ 最常用

> **本风格的标志性标记方式**。每个正文段落都应主动找出关键词/关键句，用紫色下划线标出。

```html
<span style="border-bottom:2px solid #7C3AED;font-weight:600;"><span leaf="">紫色下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">品牌叙事的核心不在营销手段，而在于</span>
  <span style="border-bottom:2px solid #7C3AED;font-weight:600;"><span leaf="">情感共鸣的构建</span></span>
  <span leaf="">。真正打动人心的故事，往往源于</span>
  <span style="border-bottom:2px solid #7C3AED;font-weight:600;"><span leaf="">真实的洞察</span></span>
  <span leaf="">与持续的表达。</span>
</p>
```

### 7e. 荧光笔效果

> 底部 40% 淡紫高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg, transparent 60%, #EDE9FE 60%);font-weight:700;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 粗下划线（三像素）

> 全文最重要的一句话才使用

```html
<span style="border-bottom:3px solid #7C3AED;font-weight:600;"><span leaf="">三像素粗下划线，全文最强调</span></span>
```

---

## 组件 8️⃣ 引用高亮块（3 种变体）

### 8a. 紫色左边线 + 极浅色背景（视觉最强）

> 极淡紫底 + 紫色粗左边线，用于核心观点与关键金句

```html
<section style="background:#F5F3FF;border-radius:4px 10px 10px 4px;padding:20px 22px;margin-bottom:24px;border-left:4px solid #7C3AED;">
  <p style="font-size:16px;font-weight:800;color:#5B21B6;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 浅色背景引用块 + 边框

> 淡紫底 + 边框，适用于补充说明、附注引用

```html
<section style="background:#F5F3FF;border-radius:10px;padding:18px 20px;margin-bottom:24px;border:1px solid #EDE9FE;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">浅紫引用内容，可以包含</span>
    <span style="border-bottom:2px solid #7C3AED;font-weight:600;"><span leaf="">下划线加粗的关键句</span></span>
    <span leaf="">，整体柔和优雅。</span>
  </p>
</section>
```

### 8c. 简约左边线引用

> 极简风格，适用于普通引用、旁注

```html
<section style="border-left:4px solid #7C3AED;padding:14px 20px;margin-bottom:24px;background:#FAFAFA;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">左边线引用内容，简洁有力，适合旁注和补充信息</span>
  </p>
</section>
```

---

## 组件 9️⃣ 提示条

> 紫色渐变背景（紫色→深紫）+ 白字，全宽圆角条。用于重要提醒、核心结论。

```html
<section style="background:linear-gradient(135deg,#7C3AED 0%,#5B21B6 100%);border-radius:8px;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#FFFFFF;margin:0;line-height:1.8;">
    <span leaf="">💡 这里是重要提示或核心结论，紫色渐变底白字清晰醒目</span>
  </p>
</section>
```

---

## 组件 🔟 图片容器

> 白底 + 圆角 12px + 边框 + 阴影。干净利落的图片展示框。

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #E5E7EB;box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom: 10px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

**带图片说明文字变体**（图片 `margin-bottom` 改为 `8px`）：

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #E5E7EB;box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom: 8px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 1️⃣1️⃣ 加粗正文段落

> 结论性短句，加粗突出。适用于章节小结、论点归纳。

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1E1B4B;">
  <span leaf="">加粗的结论性短句，优雅而坚定</span>
</p>
```

**结合荧光笔的变体**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1E1B4B;">
  <span style="background:linear-gradient(180deg, transparent 60%, #EDE9FE 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

---

## 组件 1️⃣2️⃣ 数据/要点卡片组

> 极浅紫色背景 + 紫色大号数据 + 灰色描述。适用于数据展示、要点罗列。

### 两列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #EDE9FE;">
    <p style="font-size:28px;font-weight:900;color:#7C3AED;margin:0 0 4px;line-height:1;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:18px 16px;text-align:center;border:1px solid #EDE9FE;">
    <p style="font-size:28px;font-weight:900;color:#7C3AED;margin:0 0 4px;line-height:1;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #EDE9FE;">
    <p style="font-size:24px;font-weight:900;color:#7C3AED;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #EDE9FE;">
    <p style="font-size:24px;font-weight:900;color:#7C3AED;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#F5F3FF;border-radius:10px;padding:16px 10px;text-align:center;border:1px solid #EDE9FE;">
    <p style="font-size:24px;font-weight:900;color:#7C3AED;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
</section>
```

---

## 组件 1️⃣3️⃣ 标签胶囊（3 种变体）

> 行内标签，用于标注类别、状态、工具名等。

### 紫色实底白字（强调）

```html
<span style="display:inline-block;background:#7C3AED;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 紫色描边（轻量）

```html
<span style="display:inline-block;border:1px solid #7C3AED;color:#7C3AED;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 深紫底白字（信息）

```html
<span style="display:inline-block;background:#5B21B6;color:#FFFFFF;font-size:12px;font-weight:600;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 1️⃣4️⃣ END 结尾分割线

> 紫色渐变线 + 紫色 END 文字，收束全文。

```html
<section style="padding: 0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:2px;width:60px;background:linear-gradient(to right,transparent,#7C3AED);margin-right:12px;"></span>
      <span style="font-size:11px;color:#7C3AED;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:2px;width:60px;background:linear-gradient(to left,transparent,#7C3AED);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 1️⃣5️⃣ 尾部作者签名区

> 固定内容："我是甲木..." + "点赞、在看、转发"三连（紫色加粗）。

```html
<section style="padding: 0 10px;">
  <section style="text-align: center;margin-bottom: 10px;border-radius: 12px;overflow: hidden;">
    <span leaf=""><img src="个人名片或引导图URL" style="max-width:100%;"></span>
  </section>
  <p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察， AI 干货内容</span>
  </p>
  <p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#7C3AED;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 📐 完整文章模板骨架

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.8;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- ① 开头引言卡片（白底紫色点睛） -->
  <!-- 组件2 -->

  <!-- ② 前言正文（开场白） -->
  <section style="padding: 0 10px 20px;">
    <!-- 组件6 正文段落 × N -->
  </section>

  <!-- ③ 目录导航 -->
  <!-- 组件3 三列目录卡片 -->

  <!-- ④ 章节分割线 -->
  <!-- 组件4 紫色渐变分割线 -->

  <!-- ⑤ 第一章 -->
  <!-- 组件5（紫色底编号标签 01 + 标题） -->
  <!--   组件6正文 + 组件7高亮 + 组件8引用 + 组件9提示条 + 组件10图片 + 组件12数据卡片 -->

  <!-- ⑥ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑦ 第二章 -->
  <!-- 组件5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- ⑧ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑨ 结语章节 -->
  <!-- 组件5（∞ 紫色底标签变体） -->

  <!-- ⑩ END 分割线 -->
  <!-- 组件14 -->

  <!-- ⑪ 尾部签名 -->
  <!-- 组件15 -->

</section>
```

---

## 🔧 Markdown → 紫色优雅排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 白底紫色引言卡片 | 文章开头的引用 |
| `## 章节标题` | 组件 5 章节标题 | 紫色底编号标签 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，记得标记关键词 |
| `**加粗文字**` | 组件 7a 紫色加粗 | 紫色 #7C3AED |
| `==高亮文字==` | 组件 7b 紫色实底白字标签 | 最强高亮 |
| `<u>下划线</u>` | 组件 7d 紫色下划线 | 2px 紫色，最常用 |
| `> 引用段落` | 组件 8a/8b/8c | 三种引用块可选 |
| `!> 提示文字` | 组件 9 紫色提示条 | 紫色渐变全宽条 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 说明 |
| 数据展示 | 组件 12 数据卡片组 | 紫色大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 三种风格可选 |
| `---` | 组件 4 章节分割线 | 紫色渐变 |
| 文末 | 组件 14 + 15 | END线 + 签名 |
