# 甲木公众号排版组件库 —— 青石板极简风

> **使用说明**：本组件库为「青石板极简风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：极简主义、冷静克制、高级灰、建筑感、无彩色系的高端质感。以石板灰（Slate）为主色，去除一切多余装饰，用留白与线条构建秩序。
>
> **与其他色系的差异**：
> - 天蓝色系 → 轻盈、清透、散文感
> - 红黑色系 → 沉稳、力量、高级感
> - 绿色科技风 → 结构化、杂志感、产品评测风
> - **青石板极简风** → **极简克制、建筑感、冷灰高级、无彩色系质感**
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
主色调：       #475569（石板灰/青石板）
主色调深：     #334155（深石板）
主色调浅：     #94A3B8（浅石板）
主色调极浅：   #E2E8F0（淡灰蓝）
主色调背景：   #F8FAFC（极淡灰底）
标题色：       #0F172A（极深蓝黑）
正文色：       #374151（深灰）
辅助文字色：   #9CA3AF（中灰）
分割线色：     #E2E8F0
边框色：       #F1F5F9
正文字号：     15px
行高：         1.8
字间距：       0.5px
```

---

## 组件 1️⃣ 全局容器（页面包裹层）

> 所有内容都放在这个最外层容器内。极淡灰底色营造纸感。

```html
<section style="max-width:677px;margin:0 auto;background:#F8FAFC;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2️⃣ 开头引言卡片（白底 + 石板灰左边框 + 引号 + 标签高亮 + 署名）

> 白底卡片 + 3px 石板灰左边框 + 大号浅灰引号 + 实底标签高亮 + 右下署名。极简克制，冷灰基调。

```html
<section style="margin:0 0 32px;background:#ffffff;border-left:3px solid #475569;border-radius:2px 12px 12px 2px;box-shadow:0 2px 12px -4px rgba(71,85,105,0.08);padding:28px 24px 22px;overflow:hidden;">
  <p style="font-size:36px;color:#E2E8F0;font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:700;color:#0F172A;margin:12px 0 8px;line-height:1.75;padding-left:4px;">
    <span leaf="">金句的前半部分，引出核心概念</span>
    <span style="background:#475569;color:#FFFFFF;padding:2px 8px;border-radius:3px;"><span leaf="">标签高亮</span></span>
    <span leaf=""> ，金句的后半部分延续阐述。</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#9CA3AF;margin:8px 0 0;letter-spacing:1px;">
    <span leaf="">—— 甲木</span>
  </p>
</section>
```

**效果说明**：白底干净，3px 石板灰左边框是唯一装饰线，大号淡灰引号作为视觉锚点，石板灰实底标签做关键词高亮，整体冷静克制。

---

## 组件 3️⃣ 三列目录卡片

> 白底卡片 + 石板灰编号 + 淡灰竖线分隔。极简线条感。

```html
<section style="padding:0 10px 32px;">
  <p style="font-size:13px;color:#9CA3AF;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;text-align:center;">
    <section style="flex:1;">
      <p style="font-size:20px;font-weight:900;color:#475569;margin:0 0 4px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="width:1px;background:linear-gradient(to bottom,transparent,#E2E8F0,transparent);flex-shrink:0;"></section>
    <section style="flex:1;">
      <p style="font-size:20px;font-weight:900;color:#475569;margin:0 0 4px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="width:1px;background:linear-gradient(to bottom,transparent,#E2E8F0,transparent);flex-shrink:0;"></section>
    <section style="flex:1;">
      <p style="font-size:20px;font-weight:900;color:#475569;margin:0 0 4px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

**效果说明**：三列等宽布局，石板灰编号加粗突出，淡灰渐变竖线分隔，整体干净利落。

---

## 组件 4️⃣ 章节分割线

> 章节之间的渐变分割线，两端透明渐隐，中间淡灰蓝。

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #E2E8F0, transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5️⃣ 章节标题（石板灰编号标签 + 标题 + 3px 主色底线）

> 石板灰实底编号标签 + 英文小标签 + 中文标题，底部 3px 主色调线条。建筑感结构。

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #475569;">
    <section style="display:flex;align-items:center;">
      <!-- 石板灰编号标签 -->
      <span style="display:inline-block;background:#475569;color:#FFFFFF;font-size:16px;font-weight:900;padding:4px 14px;border-radius:4px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#94A3B8;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#0F172A;margin:0;letter-spacing:0.5px;">
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
<span style="display:inline-block;background:#475569;color:#FFFFFF;font-size:16px;font-weight:900;padding:4px 14px;border-radius:4px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6️⃣ 正文段落

> **⚠️ 关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**石板灰下划线**进行标记（`border-bottom:2px solid #475569;font-weight:600;`）。让读者快速扫到每段的重点。

**基础段落**（无标记时）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。极简风格下正文保持克制、干净的阅读体验。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

**示例一**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">真正的极简，不是没有设计，而是</span>
  <span style="border-bottom:2px solid #475569;font-weight:600;"><span leaf="">每一处留白都有意义</span></span>
  <span leaf="">。好的排版让内容自己说话，而不是被装饰淹没。</span>
</p>
```

**示例二**（多关键词标记）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">AI 领域的竞争已经从</span>
  <span style="border-bottom:2px solid #475569;font-weight:600;"><span leaf="">模型能力</span></span>
  <span leaf="">的比拼，转向了</span>
  <span style="border-bottom:2px solid #475569;font-weight:600;"><span leaf="">场景落地</span></span>
  <span leaf="">与</span>
  <span style="border-bottom:2px solid #475569;font-weight:600;"><span leaf="">用户体验</span></span>
  <span leaf="">的全面较量。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标

---

## 组件 7️⃣ 正文高亮样式（6 种变体）

> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 石板灰下划线** ⭐ — 正文默认标记方式，每段都应考虑使用
> 2. **7a 石板灰加粗** — 关键结论句
> 3. **7b 石板灰实底标签** — 极少数最核心概念（每篇 2~4 个）
> 4. **7c 浅灰蓝背景** — 次要关键词
> 5. **7e 荧光笔效果** — 偶尔用于长句强调
> 6. **7f 粗下划线（三像素）** — 全文最重要的一句话

### 7a. 石板灰加粗强调

> 用于关键观点、重要结论

```html
<strong style="color:#475569;"><span leaf="">石板灰加粗强调文字</span></strong>
```

### 7b. 石板灰实底标签高亮

> 白字灰底，像标签贴纸一样醒目，仅用于最核心概念（每篇 2~4 个）

```html
<span style="background:#475569;color:#FFFFFF;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅灰蓝背景高亮

> 柔和的背景标注，适用于次要关键词

```html
<span style="background:#E2E8F0;padding:1px 6px;border-radius:3px;font-weight:600;color:#334155;"><span leaf="">浅灰蓝背景关键词</span></span>
```

### 7d. 石板灰下划线 ⭐ 最常用

> **本风格的标志性标记方式**。每个正文段落都应主动找出关键词/关键句，用石板灰下划线标出。

```html
<span style="border-bottom:2px solid #475569;font-weight:600;"><span leaf="">石板灰下划线标记的关键词</span></span>
```

### 7e. 荧光笔效果（底部半高亮）

> 底部 40% 淡灰蓝高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg, transparent 60%, #E2E8F0 60%);font-weight:700;color:#0F172A;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 粗下划线（三像素）

> 全文最重要的一句话才使用

```html
<span style="border-bottom:3px solid #475569;font-weight:600;"><span leaf="">三像素粗下划线，全文最强调</span></span>
```

---

## 组件 8️⃣ 引用高亮块（3 种变体）

### 8a. 石板灰左边线引用块（视觉焦点最强）

> 左边线 + 极淡灰底 + 加粗金句

```html
<section style="background:#F8FAFC;border-radius:2px 8px 8px 2px;padding:20px 22px;margin-bottom:24px;border-left:3px solid #475569;">
  <p style="font-size:16px;font-weight:800;color:#0F172A;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 淡灰蓝背景引用块

> 柔和背景块，适合段落性引用

```html
<section style="background:#F1F5F9;border-radius:8px;padding:18px 20px;margin-bottom:24px;border:1px solid #E2E8F0;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">引用内容，可以包含</span>
    <span style="border-bottom:2px solid #475569;font-weight:600;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

### 8c. 极简左边线引用（简约版）

> 最轻量的引用样式，仅一条细线

```html
<section style="border-left:3px solid #E2E8F0;padding:14px 20px;margin-bottom:24px;background:#FAFBFC;border-radius:0 6px 6px 0;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">左边线引用内容，极简有力</span>
  </p>
</section>
```

---

## 组件 9️⃣ 提示条

> 石板灰渐变背景条，白色文字，用于重要提醒或核心结论

```html
<section style="background:linear-gradient(135deg,#475569 0%,#334155 100%);border-radius:6px;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#FFFFFF;margin:0;line-height:1.8;">
    <span leaf="">💡 这里是重要提示或核心结论，石板灰渐变底白字，克制而醒目</span>
  </p>
</section>
```

---

## 组件 🔟 图片容器

> 白底卡片包裹，极细边框，微阴影。配合说明文字时 margin-bottom 改为 8px。

**单独使用**：

```html
<section style="background:#FFF;border-radius:10px;padding:5px;border:1px solid #F1F5F9;box-shadow:0 2px 8px -2px rgba(71,85,105,0.06);margin-bottom:24px;">
  <section style="margin:0;border-radius:6px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

**图片 + 说明文字**：

```html
<section style="background:#FFF;border-radius:10px;padding:5px;border:1px solid #F1F5F9;box-shadow:0 2px 8px -2px rgba(71,85,105,0.06);margin-bottom:8px;">
  <section style="margin:0;border-radius:6px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 1️⃣1️⃣ 加粗段落

> 用于总结性、结论性的短句

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#0F172A;">
  <span leaf="">这是加粗的结论性短句</span>
</p>
```

结合下划线的变体：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#0F172A;">
  <span style="border-bottom:3px solid #E2E8F0;"><span leaf="">加粗 + 下划线的最强调短句</span></span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#0F172A;">
  <span style="background:linear-gradient(180deg, transparent 60%, #E2E8F0 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

---

## 组件 1️⃣2️⃣ 数据卡片组

> 数据展示卡片，石板灰大号数据 + 灰色描述。适合展示关键数据指标。

### 两列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F8FAFC;border-radius:8px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #E2E8F0;">
    <p style="font-size:28px;font-weight:900;color:#475569;margin:0 0 4px;line-height:1;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#F8FAFC;border-radius:8px;padding:18px 16px;text-align:center;border:1px solid #E2E8F0;">
    <p style="font-size:28px;font-weight:900;color:#475569;margin:0 0 4px;line-height:1;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F8FAFC;border-radius:8px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #E2E8F0;">
    <p style="font-size:24px;font-weight:900;color:#475569;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#F8FAFC;border-radius:8px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #E2E8F0;">
    <p style="font-size:24px;font-weight:900;color:#475569;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#F8FAFC;border-radius:8px;padding:16px 10px;text-align:center;border:1px solid #E2E8F0;">
    <p style="font-size:24px;font-weight:900;color:#475569;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
</section>
```

---

## 组件 1️⃣3️⃣ 标签胶囊（3 种变体）

> 行内标签，用于标注类别、状态、工具名等

### 石板灰实底（强调）

```html
<span style="display:inline-block;background:#475569;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 石板灰描边（轻量）

```html
<span style="display:inline-block;border:1px solid #94A3B8;color:#475569;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 深石板底（信息）

```html
<span style="display:inline-block;background:#334155;color:#FFFFFF;font-size:12px;font-weight:600;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 1️⃣4️⃣ END 分割线

> 正文结束与尾部区域之间的装饰性分割。石板灰渐变线 + END 文字。

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:60px;background:linear-gradient(to right,transparent,#94A3B8);margin-right:12px;"></span>
      <span style="font-size:10px;color:#94A3B8;letter-spacing:3px;font-weight:600;"><span leaf="">END</span></span>
      <span style="height:1px;width:60px;background:linear-gradient(to left,transparent,#94A3B8);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 1️⃣5️⃣ 尾部签名区

> 文章底部的作者介绍和互动引导

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin-bottom:24px;border-radius:10px;overflow:hidden;">
    <span leaf=""><img src="个人名片或引导图URL" style="max-width:100%;"></span>
  </section>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察， AI 干货内容</span>
  </p>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#475569;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 📐 完整文章模板骨架

> 将以上组件按顺序组装，即可生成完整文章

```html
<section style="max-width:677px;margin:0 auto;background:#F8FAFC;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- ① 开头引言卡片（白底 + 石板灰左边框） -->
  <!-- 组件2 -->

  <!-- ② 前言正文（开场白） -->
  <section style="padding:0 10px 20px;">
    <!-- 组件6 正文段落 × N -->
  </section>

  <!-- ③ 三列目录导航 -->
  <!-- 组件3 -->

  <!-- ④ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑤ 第一章 -->
  <!-- 组件5（石板灰编号标签 01 + 标题） -->
  <!--   组件6正文 + 组件7高亮 + 组件8引用 + 组件9提示条 + 组件10图片 + 组件12数据卡片 -->

  <!-- ⑥ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑦ 第二章 -->
  <!-- 组件5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- ⑧ 章节分割线 -->
  <!-- 组件4 -->

  <!-- ⑨ 结语章节 -->
  <!-- 组件5（∞ 变体 / FINAL THOUGHTS / 结语） -->

  <!-- ⑩ END 分割线 -->
  <!-- 组件14 -->

  <!-- ⑪ 尾部签名 -->
  <!-- 组件15 -->

</section>
```

---

## 🔧 Markdown → 青石板极简风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 引言卡片 | 白底 + 石板灰左边框 + 标签高亮 |
| `## 章节标题` | 组件 5 章节标题 | 石板灰编号标签 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认带关键词下划线标记 |
| `**加粗文字**` | 组件 7a 石板灰加粗 | 石板灰色 #475569 |
| `==高亮文字==` | 组件 7b 石板灰实底标签 | 白字灰底最强高亮 |
| `<u>下划线</u>` | 组件 7d 石板灰下划线 | 2px 石板灰 + font-weight:600 |
| `> 引用段落` | 组件 8a/8b/8c | 左边线/淡灰蓝底/极简线 三选一 |
| `!> 提示文字` | 组件 9 提示条 | 石板灰渐变全宽条 |
| `![](图片)` | 组件 10 图片容器 | 白底圆角卡片 + 说明 |
| 数据展示 | 组件 12 数据卡片组 | 石板灰大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 三种风格可选 |
| `---` | 组件 4 章节分割线 | 淡灰蓝渐变线 |
| 文末 | 组件 14 + 15 | END线 + 签名 |

---

## 🆚 四套主题风格对照

| 设计元素 | 天蓝色系 | 红黑色系 | 绿色科技风 | **青石板极简风** |
|---|---|---|---|---|
| 主色 | `#0EA5E9` | `#DC2626` | `#10B981` | **`#475569`** |
| 设计气质 | 轻盈、散文 | 沉稳、力量 | 杂志、产品感 | **极简、建筑感、高级灰** |
| 引言卡片 | 浅蓝渐变 + 引号 | 白底 + 红色左边框 | Hero 封面大卡 | **白底 + 石板灰左边框 + 灰底标签** |
| 目录导航 | 三列编号文字 | 红底白字卡片 | 三列彩色卡片 | **三列灰色编号 + 渐变竖线** |
| 章节标题 | 英文标签 + 水印编号 | 红底编号标签 + 3px底线 | 大号编号 + 竖线 | **石板灰编号标签 + 3px底线** |
| 关键词标记 | 蓝色下划线 | 红色下划线+加粗 | 绿色下划线 | **石板灰下划线+加粗** |
| 引用块 | 浅蓝渐变 | 暗底/浅红/左边线 | 灰底居中/黑底 | **极淡灰底 + 石板灰左边线** |
| 高亮标签 | 蓝色渐变背景 | 红底白字 | 绿色徽章 | **石板灰实底白字** |
| 荧光笔 | 蓝色底 | 红色底 | 黄色底 | **淡灰蓝底** |
| END 线 | 浅蓝渐变 | 红色渐变+红字 | — | **浅石板渐变** |
| 整体色温 | 冷蓝 | 暖红 | 中性绿 | **无彩灰/冷中性** |
