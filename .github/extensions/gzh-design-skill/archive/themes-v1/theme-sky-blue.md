# 甲木公众号排版组件库

> **使用说明**：本组件库从甲木公众号文章中抽取，所有组件均使用**内联样式**，确保在微信公众号编辑器中直接复制粘贴即可使用。
>
> **设计风格**：天蓝色系（#0EA5E9 主色调）、简约克制、留白充足、信息层次分明。
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
主色调：      #0EA5E9（天蓝色）
主色调浅：    #BAE6FD
主色调极浅：  #BFDBFE
标题色：      #111827（近黑）
正文色：      #374151（深灰）
辅助文字色：  #9CA3AF（浅灰）
分割线色：    #E5E7EB
边框色：      #F3F4F6
正文字号：    15px
行高：        1.8
字间距：      0.5px
```

---

## 组件 1️⃣ 全局容器（页面包裹层）

> 所有内容都放在这个最外层容器内

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2️⃣ 开头引言卡片（一句话总结）

> 文章顶部的金句卡片，带引号装饰、渐变背景、关键词高亮

```html
<section style="margin:0 0 32px;background:linear-gradient(135deg,#ffffff 0%,#F0F9FF 50%,#E0F2FE 100%);border:1px solid rgba(14,165,233,0.08);border-radius:16px;box-shadow:0 4px 20px -4px rgba(14,165,233,0.1);padding:24px;overflow:hidden;">
  <p style="font-size:36px;color:#BAE6FD;font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:800;color:#111827;margin:8px 0 6px;line-height:1.7;padding-left:4px;">
    <span leaf="">这里写金句的前半部分</span>
    <span style="background:linear-gradient(120deg,#BFDBFE 0%,rgba(255,255,255,0) 100%);padding:1px 4px;border-radius:3px;"><span leaf="">高亮关键词</span></span>
    <span leaf="">，金句的后半部分</span>
    <span style="border-bottom:2px solid #0EA5E9;"><span leaf="">下划线强调内容</span></span>
  </p>
  <p style="text-align:right;font-size:11px;color:#9CA3AF;margin:4px 0 0;letter-spacing:1px;">
    <span leaf="">—— 署名或出处</span>
  </p>
</section>
```

**效果说明**：大号浅蓝引号 + 加粗金句 + 右下角署名，营造「开篇定调」的仪式感。

---

## 组件 3️⃣ 前言导读区域（目录/核心观点概览）

> 文章前言结束后，展示本文核心看点的目录导航

```html
<section style="padding: 0 10px 24px;">
  <p style="font-size: 14px;color: #374151;margin: 0 0 16px;">
    <span leaf="">以下是本文的核心看点：</span>
  </p>
  <section style="display:flex;justify-content:space-between;text-align:center;">
    <section style="flex:1;">
      <p style="font-size:18px;font-weight:800;color:#0EA5E9;margin:0 0 4px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:600;color:#111827;margin:0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="width:1px;background:linear-gradient(to bottom,transparent,#E5E7EB,transparent);flex-shrink:0;"></section>
    <section style="flex:1;">
      <p style="font-size:18px;font-weight:800;color:#0EA5E9;margin:0 0 4px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:600;color:#111827;margin:0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="width:1px;background:linear-gradient(to bottom,transparent,#E5E7EB,transparent);flex-shrink:0;"></section>
    <section style="flex:1;">
      <p style="font-size:18px;font-weight:800;color:#0EA5E9;margin:0 0 4px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:600;color:#111827;margin:0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

**效果说明**：三列等宽布局，编号 + 标题，中间用渐变竖线分隔，一目了然。

---

## 组件 4️⃣ 章节分割线

> 章节之间的渐变分割线，从两端透明到中间灰色

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #E5E7EB, transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5️⃣ 章节标题组件

> 带英文小标签 + 中文标题 + 大号编号的章节头

```html
<section style="margin-top: 48px;margin-bottom: 32px;padding: 0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;border-bottom:1px solid #E5E7EB;padding-bottom:12px;">
    <section>
      <p style="font-size:10px;color:#0EA5E9;font-weight:700;letter-spacing:3px;margin:0 0 4px;text-transform:uppercase;">
        <span leaf="">ENGLISH TAG</span>
      </p>
      <h3 style="font-size:17px;font-weight:800;color:#111827;margin:0;letter-spacing:0.5px;">
        <span leaf="">中文章节标题</span>
      </h3>
    </section>
    <span style="font-size:36px;font-weight:900;color:rgba(14,165,233,0.12);line-height:1;"><span leaf="">01</span></span>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**效果说明**：左侧英文小标签（大写、稀疏字距）+ 中文大标题，右侧大号水印编号，底部细线分隔。

**结语章节变体**（编号用 ∞ 替代数字）：

```html
<span style="font-size:36px;font-weight:900;color:rgba(14,165,233,0.12);line-height:1;"><span leaf="">∞</span></span>
```

---

## 组件 6️⃣ 正文段落

> **⚠️ 关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**蓝色下划线（7c）**进行标记。让读者快速扫到每段的重点。

**基础段落**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">这里是正文内容，每段之间留 20px 间距，两端对齐，15px 字号，1.8 倍行高。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #0EA5E9;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

---

## 组件 7️⃣ 正文高亮样式（4 种变体）

### 7a. 蓝色加粗强调

> 用于关键观点、重要结论

```html
<strong style="color:#0EA5E9;"><span leaf="">这是蓝色加粗强调的文字</span></strong>
```

### 7b. 渐变背景高亮

> 用于关键词、核心概念

```html
<span style="background:linear-gradient(120deg,#BFDBFE 0%,rgba(255,255,255,0) 100%);padding:0 4px;border-radius:2px;font-weight:600;color:#111827;"><span leaf="">高亮关键词</span></span>
```

### 7c. 下划线强调

> 用于轻度强调、术语标注

```html
<span style="border-bottom:2px solid #BAE6FD;"><span leaf="">下划线强调文字</span></span>
```

### 7d. 荧光笔效果（底部半高亮）

> 用于重要长句的高亮，模拟荧光笔标记效果

```html
<span style="background:linear-gradient(180deg, transparent 60%, #BFDBFE 60%);font-weight:700;color:#111827;"><span leaf="">荧光笔效果的重要长句，底部 40% 高亮</span></span>
```

### 7e. 加粗下划线（三像素）

> 用于最高级别的正文强调

```html
<span style="border-bottom:3px solid #BFDBFE;"><span leaf="">三像素粗下划线强调</span></span>
```

---

## 组件 8️⃣ 引用高亮块（渐变背景块）

> 用于提炼核心观点、关键问题、重要引述

### 8a. 加粗版（标题性引用）

```html
<section style="background:linear-gradient(135deg,#E0F2FE 0%,#F0F9FF 50%,#FAFEFF 100%);border-radius:8px;padding:16px 18px;margin-bottom:24px;">
  <p style="font-size:15px;font-weight:800;color:#111827;margin:0;line-height:1.8;">
    <span leaf="">这里是加粗的核心提问或关键观点？</span>
  </p>
</section>
```

### 8b. 正文版（段落性引用）

```html
<section style="background:linear-gradient(135deg,#E0F2FE 0%,#F0F9FF 50%,#FAFEFF 100%);border-radius:8px;padding:16px 18px;margin-bottom:24px;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">这里是引用的正文内容，可以包含</span>
    <span style="border-bottom:2px solid #BAE6FD;font-weight:600;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

---

## 组件 9️⃣ 图片容器

> 图片的标准展示容器，带圆角、边框和阴影

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #F3F4F6;box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);margin-bottom: 10px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

---

## 组件 🔟 图片说明文字

> 图片下方的居中灰色说明文字

```html
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

**注意**：当图片 + 说明文字配合使用时，图片容器的 `margin-bottom` 改为 `8px`：

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #F3F4F6;box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);margin-bottom: 8px;">
  <!-- 图片内容 -->
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明</span>
</p>
```

---

## 组件 1️⃣1️⃣ 加粗正文段落

> 用于总结性、结论性的短句

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:600;color:#111827;">
  <span leaf="">这是加粗的结论性短句</span>
</p>
```

也可以结合下划线：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:600;color:#111827;">
  <span style="border-bottom:3px solid #BFDBFE;"><span leaf="">加粗 + 下划线的最强调短句</span></span>
</p>
```

---

## 组件 1️⃣2️⃣ END 结尾分割线

> 正文结束与尾部区域之间的装饰性分割

```html
<section style="padding: 0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:60px;background:linear-gradient(to right,transparent,#BAE6FD);margin-right:12px;"></span>
      <span style="font-size:10px;color:#9CA3AF;letter-spacing:2px;font-weight:600;"><span leaf="">END</span></span>
      <span style="height:1px;width:60px;background:linear-gradient(to left,transparent,#BAE6FD);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 1️⃣3️⃣ 尾部作者签名区

> 文章底部的作者介绍和互动引导

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
    <strong style="color:#0EA5E9;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 📐 完整文章模板骨架

> 将以上组件按顺序组装，即可生成完整文章

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- ① 开头引言卡片 -->
  <!-- 组件2 -->

  <!-- ② 前言正文（开场白） -->
  <section style="padding: 0 10px 20px;">
    <!-- 组件6 正文段落 × N -->
  </section>

  <!-- ③ 目录导航 -->
  <!-- 组件3 -->

  <!-- ④ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑤ 第一章 -->
  <!-- 组件5（章节标题 01） -->
  <!--   内部使用：组件6正文 + 组件7高亮 + 组件8引用 + 组件9图片 -->

  <!-- ⑥ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑦ 第二章 -->
  <!-- 组件5（章节标题 02） -->

  <!-- ... 更多章节 ... -->

  <!-- ⑧ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑨ 结语章节 -->
  <!-- 组件5（FINAL THOUGHTS / 结语 / ∞） -->

  <!-- ⑩ END 分割线 -->
  <!-- 组件12 -->

  <!-- ⑪ 尾部签名 -->
  <!-- 组件13 -->

</section>
```

---

## 🔧 Markdown → 公众号排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 引言卡片 | 文章开头的引用 |
| `## 章节标题` | 组件 5 章节标题 | 自动编号 01/02/03... |
| 普通段落 | 组件 6 正文段落 | 默认样式 |
| `**加粗文字**` | 组件 7a 蓝色加粗 | 变为蓝色 #0EA5E9 |
| `==高亮文字==` | 组件 7b 渐变背景 | 蓝色渐变背景 |
| `<u>下划线</u>` | 组件 7c 下划线 | 浅蓝下划线 |
| `> 引用段落` | 组件 8 引用高亮块 | 渐变蓝背景块 |
| `![](图片)` | 组件 9 + 10 | 圆角卡片 + 说明文字 |
| `---` | 组件 4 章节分割线 | 渐变线 |
| 文末 | 组件 12 + 13 | END线 + 签名 |
