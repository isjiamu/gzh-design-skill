# 甲木公众号排版组件库 —— 玫瑰粉色系

> **使用说明**：本组件库为「玫瑰粉色系」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：玫瑰粉色系（#E11D48 主色调）、时尚温暖、柔和而不失力量、现代女性化美学。
>
> **与其他色系的差异**：
> - 天蓝色系 → 轻盈、清透、散文感
> - 红黑色系 → 沉稳、力量、高级感
> - 绿色科技风 → 结构化、杂志感、产品评测风
> - **玫瑰粉色系** → **时尚、温暖、柔和力量、现代女性化**
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
主色调：       #E11D48（玫瑰红/粉）
主色调深：     #BE123C（深玫瑰）
主色调浅：     #FDA4AF（浅粉）
主色调极浅：   #FFE4E6（淡粉）
主色调背景：   #FFF1F2（极淡粉底）
标题色：       #1C1917（近黑）
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

> 所有内容都放在这个最外层容器内

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2️⃣ 开头引言卡片（白底玫瑰色点睛）

> 白底 + 玫瑰色粗左边框 + 大号玫瑰引号 + 玫瑰色实底关键词高亮 + 右下署名

```html
<section style="margin:0 0 32px;background:#ffffff;border-left:5px solid #E11D48;border-radius:4px 16px 16px 4px;box-shadow:0 4px 20px -4px rgba(225,29,72,0.12);padding:28px 24px 22px;overflow:hidden;">
  <p style="font-size:42px;color:#FDA4AF;font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:800;color:#1C1917;margin:12px 0 8px;line-height:1.75;padding-left:4px;">
    <span style="background:#E11D48;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">高亮关键词</span></span>
    <span leaf=""> ，不是工具，而是懂得如何 </span>
    <span style="background:#E11D48;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">热爱</span></span>
    <span leaf=""> 生活的态度。</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#9CA3AF;margin:8px 0 0;letter-spacing:1px;">
    <span leaf="">—— 甲木</span>
  </p>
</section>
```

**效果**：白底干净明快，玫瑰色左边框 + 玫瑰色实底标签做点睛，金句在白底上极清晰，温暖而有力。

---

## 组件 3️⃣ 三列目录卡片（玫瑰色编号）

> 三列目录卡片，玫瑰色背景编号区 + 深色标题，柔和而结构分明

```html
<section style="padding: 0 10px 32px;">
  <p style="font-size: 14px;color: #9CA3AF;margin: 0 0 14px;letter-spacing:1px;">
    <span leaf="">📌 本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #FFE4E6;">
      <p style="display:inline-block;background:#E11D48;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #FFE4E6;">
      <p style="display:inline-block;background:#E11D48;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:16px 12px;text-align:center;border:1px solid #FFE4E6;">
      <p style="display:inline-block;background:#E11D48;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4️⃣ 章节分割线（玫瑰色渐变）

> 玫瑰色渐变分割线，两端渐隐，温柔有存在感

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #FDA4AF, #E11D48, #FDA4AF, transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5️⃣ 章节标题组件（玫瑰色编号标签 + 标题 + 3px主色底线）

> 玫瑰色实底编号标签 + 英文小标签 + 中文大标题，底部 3px 玫瑰色主色线

```html
<section style="margin-top: 48px;margin-bottom: 28px;padding: 0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #E11D48;">
    <section style="display:flex;align-items:center;">
      <!-- 玫瑰色编号标签 -->
      <span style="display:inline-block;background:#E11D48;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#E11D48;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#1C1917;margin:0;letter-spacing:0.5px;">
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
<span style="display:inline-block;background:#E11D48;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6️⃣ 正文段落

> **⚠️ 关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**玫瑰色下划线（7d）**进行标记。这是本风格的核心视觉特征——让读者快速扫到每段的重点。

**基础段落**（无标记时）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标

**示例一**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">好的设计不仅仅是视觉上的美观，更重要的是</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">让用户在每一次交互中感到被尊重</span></span>
  <span leaf="">。真正的用户体验，始于对</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">细节的极致追求</span></span>
  <span leaf="">。</span>
</p>
```

**示例二**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">当我们回顾过去十年的技术演进，会发现</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">真正改变世界的从来不是最强的技术</span></span>
  <span leaf="">，而是那些</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">最懂人心的产品</span></span>
  <span leaf="">。技术只是手段，</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">洞察才是核心竞争力</span></span>
  <span leaf="">。</span>
</p>
```

---

## 组件 7️⃣ 正文高亮样式（6 种变体 + 使用优先级）

> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 玫瑰色下划线** ⭐ — 正文默认标记方式，每段都应考虑使用
> 2. **7a 玫瑰色加粗** — 关键结论句
> 3. **7b 玫瑰色实底标签** — 极少数最核心的概念（每篇 2~4 个）
> 4. **7c 浅粉背景** — 次要关键词补充
> 5. **7e 荧光笔** — 偶尔用于长句强调
> 6. **7f 粗下划线** — 全文最重要的一句话

### 7a. 玫瑰色加粗强调

> 用于关键观点、重要结论

```html
<strong style="color:#E11D48;"><span leaf="">玫瑰色加粗强调</span></strong>
```

### 7b. 玫瑰色实底标签高亮

> 白字玫瑰底，像标签贴纸一样醒目，仅用于最核心的概念（每篇 2~4 个）

```html
<span style="background:#E11D48;color:#FFFFFF;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅粉背景高亮

> 柔和的背景标注，适用于次要关键词

```html
<span style="background:#FFE4E6;padding:1px 6px;border-radius:3px;font-weight:600;color:#BE123C;"><span leaf="">浅粉背景关键词</span></span>
```

### 7d. 玫瑰色下划线 ⭐ 最常用

> **本风格的标志性标记方式**。每个正文段落都应主动找出关键词/关键句，用玫瑰色下划线标出。

```html
<span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">玫瑰色下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">生活的美好不在于拥有多少，而在于</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">感受到多少</span></span>
  <span leaf="">。每一个用心的瞬间，都值得被</span>
  <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">温柔以待</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 荧光笔效果

> 底部 40% 浅粉高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg, transparent 60%, #FFE4E6 60%);font-weight:700;color:#1C1917;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 粗下划线（三像素）

> 全文最重要的一句话才使用

```html
<span style="border-bottom:3px solid #E11D48;font-weight:600;"><span leaf="">三像素粗下划线，全文最强调</span></span>
```

---

## 组件 8️⃣ 引用高亮块（3 种变体）

### 8a. 玫瑰色左边线引用块（视觉焦点最强）

```html
<section style="background:#FFF1F2;border-radius:4px 10px 10px 4px;padding:20px 22px;margin-bottom:24px;border-left:4px solid #E11D48;">
  <p style="font-size:16px;font-weight:800;color:#BE123C;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 浅粉背景引用块

```html
<section style="background:#FFF1F2;border-radius:10px;padding:18px 20px;margin-bottom:24px;border:1px solid #FDA4AF;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">浅粉引用内容，可以包含</span>
    <span style="border-bottom:2px solid #E11D48;font-weight:600;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

### 8c. 玫瑰色左边线引用（简约版）

```html
<section style="border-left:4px solid #E11D48;padding:14px 20px;margin-bottom:24px;background:#FAFAFA;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">左边线引用内容，简洁温暖</span>
  </p>
</section>
```

---

## 组件 9️⃣ 提示条（玫瑰色渐变）

> 全宽玫瑰色渐变背景条，用于重要提醒、核心结论

```html
<section style="background:linear-gradient(135deg,#E11D48 0%,#BE123C 100%);border-radius:8px;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#FFFFFF;margin:0;line-height:1.8;">
    <span leaf="">💡 这里是重要提示或核心结论，玫瑰色渐变底白字极为醒目</span>
  </p>
</section>
```

---

## 组件 🔟 图片容器

> 图片的标准展示容器，带圆角、边框和阴影

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #E5E7EB;box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom: 10px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

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

> 用于总结性、结论性的短句

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1C1917;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1C1917;">
  <span style="background:linear-gradient(180deg, transparent 60%, #FFE4E6 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

结合粗下划线的变体：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1C1917;">
  <span style="border-bottom:3px solid #FDA4AF;"><span leaf="">加粗 + 下划线的最强调短句</span></span>
</p>
```

---

## 组件 1️⃣2️⃣ 数据/要点卡片组

> 两列或三列的数据展示卡片，玫瑰色数字 + 灰色描述

### 两列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #FFE4E6;">
    <p style="font-size:28px;font-weight:900;color:#E11D48;margin:0 0 4px;line-height:1;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:18px 16px;text-align:center;border:1px solid #FFE4E6;">
    <p style="font-size:28px;font-weight:900;color:#E11D48;margin:0 0 4px;line-height:1;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #FFE4E6;">
    <p style="font-size:24px;font-weight:900;color:#E11D48;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #FFE4E6;">
    <p style="font-size:24px;font-weight:900;color:#E11D48;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#FFF1F2;border-radius:10px;padding:16px 10px;text-align:center;border:1px solid #FFE4E6;">
    <p style="font-size:24px;font-weight:900;color:#E11D48;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
</section>
```

---

## 组件 1️⃣3️⃣ 标签胶囊（3 种变体）

> 行内标签，用于标注类别、状态、工具名等

### 玫瑰底白字（强调）

```html
<span style="display:inline-block;background:#E11D48;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 玫瑰色描边（轻量）

```html
<span style="display:inline-block;border:1px solid #E11D48;color:#E11D48;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 深玫瑰底（信息）

```html
<span style="display:inline-block;background:#BE123C;color:#FFFFFF;font-size:12px;font-weight:600;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 1️⃣4️⃣ END 结尾分割线

> 正文结束与尾部区域之间的装饰性分割

```html
<section style="padding: 0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:2px;width:60px;background:linear-gradient(to right,transparent,#E11D48);margin-right:12px;"></span>
      <span style="font-size:11px;color:#E11D48;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:2px;width:60px;background:linear-gradient(to left,transparent,#E11D48);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 1️⃣5️⃣ 尾部作者签名区

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
    <strong style="color:#E11D48;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 📐 完整文章模板骨架

> 将以上组件按顺序组装，即可生成完整文章

```html
<section style="max-width: 677px;margin: 0 auto;background: #ffffff;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- ① 开头引言卡片（白底玫瑰色点睛） -->
  <!-- 组件2 -->

  <!-- ② 前言正文（开场白） -->
  <section style="padding: 0 10px 20px;">
    <!-- 组件6 正文段落 × N -->
  </section>

  <!-- ③ 目录导航 -->
  <!-- 组件3 玫瑰色编号目录卡片 -->

  <!-- ④ 章节分割线 -->
  <!-- 组件4 玫瑰色渐变分割线 -->

  <!-- ⑤ 第一章 -->
  <!-- 组件5（玫瑰色编号标签 01 + 标题） -->
  <!--   组件6正文 + 组件7高亮 + 组件8引用 + 组件9提示条 + 组件10图片 + 组件12数据卡片 -->

  <!-- ⑥ 章节分割线 -->

  <!-- ⑦ 第二章 -->
  <!-- 组件5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- ⑧ 章节分割线 -->

  <!-- ⑨ 结语章节 -->
  <!-- 组件5（∞ 玫瑰色标签变体） -->

  <!-- ⑩ END 分割线 -->
  <!-- 组件14 -->

  <!-- ⑪ 尾部签名 -->
  <!-- 组件15 -->

</section>
```

---

## 🔧 Markdown → 玫瑰粉色系排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 白底玫瑰色引言卡片 | 文章开头的引用 |
| `## 章节标题` | 组件 5 章节标题 | 玫瑰色编号标签 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，每段标记 1~3 个关键词下划线 |
| `**加粗文字**` | 组件 7a 玫瑰色加粗 | 玫瑰色 #E11D48 |
| `==高亮文字==` | 组件 7b 玫瑰色实底标签 | 最强高亮 |
| `<u>下划线</u>` | 组件 7d 玫瑰色下划线 | 2px 玫瑰色 |
| `> 引用段落` | 组件 8a/8b/8c | 左边线/浅粉底/简约左边线三选一 |
| `!> 提示文字` | 组件 9 玫瑰色提示条 | 玫瑰色渐变全宽条 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 说明 |
| 加粗段落 | 组件 11 加粗正文段落 | 结论性短句 |
| 数据展示 | 组件 12 数据卡片组 | 玫瑰色大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 三种风格可选 |
| `---` | 组件 4 章节分割线 | 玫瑰色渐变 |
| 文末 | 组件 14 + 15 | END线 + 签名 |

---

## 🆚 四套主题风格对照

| 设计元素 | 天蓝色系 | 红黑色系 | 绿色科技风 | **玫瑰粉色系** |
|---|---|---|---|---|
| 主色 | `#0EA5E9` | `#DC2626` | `#10B981` | **`#E11D48`** |
| 文章开头 | 引号金句卡片 | 白底红色左边框金句 | Hero 封面大卡片 | **白底 + 玫瑰左边框 + 粉色引号 + 实底标签** |
| 目录导航 | 三列编号文字 | 红底白字编号卡片 | 三列彩色卡片 | **淡粉底卡片 + 玫瑰实底编号** |
| 分割线 | 灰色渐变 | 红色渐变 | 灰色实线 | **玫瑰色渐变（透明→浅粉→玫瑰→浅粉→透明）** |
| 章节标题 | 英文标签 + 水印编号 | 红底编号标签 + 3px红线 | 大号编号 + 竖线 | **玫瑰编号标签 + 3px玫瑰底线** |
| 正文下划线 | 天蓝下划线 | 红色下划线 | 绿色下划线 | **玫瑰色下划线** |
| 引用块 | 浅蓝渐变 | 浅红/左边线三选一 | 灰底居中/黑底 | **浅粉底/玫瑰左边线三选一** |
| 提示条 | 无 | 红色渐变条 | 无 | **玫瑰色渐变条** |
| 数据卡片 | 无 | 红色数据卡片 | 无 | **玫瑰色数据卡片** |
| 标签胶囊 | 无 | 三种红色标签 | 绿色徽章 | **三种玫瑰色标签** |
| END 线 | 1px 浅蓝渐变 | 2px 正红渐变 | 灰色实线 | **2px 玫瑰渐变** |
| 文章结尾 | END线 + 签名 | END线 + 签名 | CTA 互动卡片 | **END线 + 签名** |
| 整体气质 | 散文、轻盈 | 沉稳、力量 | 杂志、结构、产品感 | **时尚、温暖、柔和力量** |
