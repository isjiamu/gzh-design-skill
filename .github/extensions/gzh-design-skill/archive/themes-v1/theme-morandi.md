# 甲木公众号排版组件库 —— 莫兰迪温柔风

> **使用说明**：本组件库为「莫兰迪温柔风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：低饱和莫兰迪色系，柔和、温柔、知性、高级灰调。简洁大方有呼吸感。左竖条 + 浅底为强调容器，无四周虚线框。
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

---

## 设计变量速查表

```
主色（灰玫）：     #B5828C
辅助色·灰蓝：     #8BA3B0
辅助色·灰绿：     #9CAF9C
辅助色·灰杏：     #D4B5A0
标题色：           #4A4A4A
正文色：           #6B6B6B
辅助文字色：       #A8A8A8
浅底色：           #F5F1F0
细线色：           #E3DBD9
灰玫极浅底：       #F2ECEC
灰蓝极浅底：       #EEF3F6
灰绿极浅底：       #EFF4EF
灰杏极浅底：       #FAF4EF
正文字号：         15px
行高：             1.8
字间距：           0.5px
圆角：             12px（卡片）/ 14px（大卡）
内容区边距：       0 10px（左右各 10px）
```

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#F5F1F0;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#6B6B6B;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（灰玫浅底 + 左灰玫竖条）

> 灰玫浅底圆角卡片 + 左侧灰玫竖条 + 大号开引号 + 灰玫关键词高亮 + 右下署名。柔和有质感，无四周边框。

```html
<section style="margin:10px 10px 32px;background:#F2ECEC;border-radius:14px;box-shadow:0 2px 16px -4px rgba(181,130,140,0.12);padding:28px 24px 22px;overflow:hidden;border-left:4px solid #B5828C;">
  <p style="font-size:38px;color:#B5828C;font-weight:900;margin:0;line-height:0.7;opacity:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:700;color:#4A4A4A;margin:14px 0 10px;line-height:1.8;padding-left:2px;">
    <span style="background:#B5828C;color:#FFFFFF;padding:2px 8px;border-radius:4px;font-weight:700;"><span leaf="">高亮关键词</span></span>
    <span leaf="">，不是模型，而是懂得如何</span>
    <span style="background:#B5828C;color:#FFFFFF;padding:2px 8px;border-radius:4px;font-weight:700;"><span leaf="">温柔驾驭</span></span>
    <span leaf="">它们的我们。</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#A8A8A8;margin:10px 0 0;letter-spacing:1px;">
    <span leaf="">—— 作者名（按文章作者/主题而定）</span>
  </p>
</section>
```

**效果**：灰玫浅底 + 左侧灰玫竖条，温柔知性，大号引号半透明增加层次，无四周虚线框。

> **注意**：引言卡内关键词用灰玫底白字（`background:#B5828C;color:#FFFFFF`），这是卡片内专用处理；正文里的关键词标签见组件 7b（用浅底深字）。

---

## 组件 3 前言导读区域（三栏莫兰迪目录卡片）

> 三列目录卡片，每栏用不同莫兰迪色编号区，浅底、圆角，视觉区分但都低饱和不刺眼。

```html
<section style="padding:0 10px 32px;">
  <p style="font-size:13px;color:#A8A8A8;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#F2ECEC;border-radius:12px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E3DBD9;">
      <p style="display:inline-block;background:#B5828C;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:20px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:600;color:#4A4A4A;margin:0;line-height:1.5;"><span leaf="">第一个看点</span></p>
    </section>
    <section style="flex:1;background:#EEF3F6;border-radius:12px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E3DBD9;">
      <p style="display:inline-block;background:#8BA3B0;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:20px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:600;color:#4A4A4A;margin:0;line-height:1.5;"><span leaf="">第二个看点</span></p>
    </section>
    <section style="flex:1;background:#EFF4EF;border-radius:12px;padding:16px 12px;text-align:center;border:1px solid #E3DBD9;">
      <p style="display:inline-block;background:#9CAF9C;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:20px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:600;color:#4A4A4A;margin:0;line-height:1.5;"><span leaf="">第三个看点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（灰玫渐变细线）

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#D4B5A0,#B5828C,#D4B5A0,transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题组件（莫兰迪圆角编号 + 标题）

> 灰玫圆角编号胶囊 + 英文小标签 + 中文大标题，底部灰玫细线。不同章节可换莫兰迪辅色编号。

**默认（灰玫色）**：

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:2px solid #E3DBD9;">
    <section style="display:flex;align-items:center;">
      <span style="display:inline-block;background:#B5828C;color:#FFFFFF;font-size:17px;font-weight:800;padding:5px 16px;border-radius:20px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#B5828C;font-weight:600;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:700;color:#4A4A4A;margin:0;letter-spacing:0.5px;">
          <span leaf="">中文章节标题</span>
        </h3>
      </section>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**第二章变体（灰蓝色）**：

```html
<span style="display:inline-block;background:#8BA3B0;color:#FFFFFF;font-size:17px;font-weight:800;padding:5px 16px;border-radius:20px;margin-right:14px;line-height:1.3;"><span leaf="">02</span></span>
```

**第三章变体（灰绿色）**：

```html
<span style="display:inline-block;background:#9CAF9C;color:#FFFFFF;font-size:17px;font-weight:800;padding:5px 16px;border-radius:20px;margin-right:14px;line-height:1.3;"><span leaf="">03</span></span>
```

**第四章变体（灰杏色）**：

```html
<span style="display:inline-block;background:#D4B5A0;color:#FFFFFF;font-size:17px;font-weight:800;padding:5px 16px;border-radius:20px;margin-right:14px;line-height:1.3;"><span leaf="">04</span></span>
```

**结语章节变体**（编号用 ∞ 替代数字，回归灰玫）：

```html
<span style="display:inline-block;background:#B5828C;color:#FFFFFF;font-size:17px;font-weight:800;padding:5px 16px;border-radius:20px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，主动识别 1~3 个**关键语句或关键词**，用**灰玫下划线（7d）**进行标记。这是本风格的核心视觉特征，温柔不抢戏。

**基础段落**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#6B6B6B;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#6B6B6B;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #D4B5A0;font-weight:600;color:#4A4A4A;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字，太短没意义，太长失去焦点
- 下划线色用灰杏 `#D4B5A0`，柔和温暖，不刺眼

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心设计理念**：低饱和克制用色，莫兰迪色系只在真正需要的锚点出现。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 灰杏下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 灰玫加粗** —— 普通加粗为主，灰玫加粗仅用于极少数锚点
> 3. **7b 浅底深字标签** —— 核心概念标签（每篇 2~4 个）
> 4. **7c 灰玫浅背景** —— 次要关键词补充
> 5. **7e 荧光笔** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**灰玫加粗**仅用于极少数关键锚点（如产品名、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong><span leaf="">普通加粗强调</span></strong>
```

灰玫加粗（仅限关键锚点）：
```html
<strong style="color:#B5828C;"><span leaf="">灰玫加粗，仅用于产品名/步骤/CTA</span></strong>
```

### 7b. 浅底深字标签

> 浅灰玫底 + 深玫文字，柔和知性。用于核心概念（每篇 2~4 个）

```html
<span style="background:#F2ECEC;color:#8A5A63;padding:2px 7px;border-radius:4px;font-weight:600;"><span leaf="">关键词标签</span></span>
```

### 7c. 灰玫浅背景高亮

> 极淡灰玫背景，适用于次要关键词

```html
<span style="background:#F2ECEC;padding:1px 6px;border-radius:4px;font-weight:600;color:#8A5A63;"><span leaf="">浅玫背景关键词</span></span>
```

### 7d. 灰杏下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为灰杏 `#D4B5A0`，温暖柔和，适合高频使用。

```html
<span style="border-bottom:2px solid #D4B5A0;font-weight:600;color:#4A4A4A;"><span leaf="">灰杏下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#6B6B6B;">
  <span leaf="">低饱和度不是设计的妥协，而是</span>
  <span style="border-bottom:2px solid #D4B5A0;font-weight:600;color:#4A4A4A;"><span leaf="">一种更高级的克制</span></span>
  <span leaf="">。莫兰迪色系用灰度过滤了浮躁，让每一种颜色都显得</span>
  <span style="border-bottom:2px solid #D4B5A0;font-weight:600;color:#4A4A4A;"><span leaf="">沉静而有呼吸感</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 荧光笔效果

> 底部 40% 灰杏高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg,transparent 60%,#D4B5A0 60%);font-weight:700;color:#4A4A4A;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 灰玫底左竖条金句引用（视觉焦点最强）

> 灰玫极浅底 + 灰玫左竖条，用于核心金句

```html
<section style="background:#F2ECEC;border-radius:0 12px 12px 0;border-left:4px solid #B5828C;padding:18px 22px;margin-bottom:24px;">
  <p style="font-size:16px;font-weight:700;color:#4A4A4A;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句，低调有力。」</span>
  </p>
</section>
```

### 8b. 灰蓝浅底内容引用块（Prompt / 引用内容）

> 灰蓝极浅底 + 灰蓝左竖条，用于展示 Prompt、引用内容等

```html
<section style="background:#EEF3F6;border-radius:0 12px 12px 0;border-left:4px solid #8BA3B0;padding:18px 20px;margin-bottom:24px;">
  <p style="font-size:15px;color:#6B6B6B;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">引用内容，可以包含</span>
    <span style="border-bottom:2px solid #D4B5A0;font-weight:600;color:#4A4A4A;"><span leaf="">下划线加粗的关键句</span></span>
    <span leaf="">，整体柔和不刺激。</span>
  </p>
</section>
```

### 8c. 浅底细线左竖条旁注（轻量旁注）

> 近白底 + 灰细竖条，用于轻量旁注、补充说明

```html
<section style="border-left:3px solid #E3DBD9;padding:12px 20px;margin-bottom:24px;background:#FAF8F7;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#A8A8A8;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">轻量旁注内容，灰色低调，不抢主文视线。</span>
  </p>
</section>
```

---

## 组件 9 提示/警示条

> 灰绿极浅底 + 灰绿左竖条 + 深字提示，柔和知性，用于重要提醒、核心结论

```html
<section style="background:#EFF4EF;border-left:4px solid #9CAF9C;border-radius:0 10px 10px 0;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:600;color:#4A4A4A;margin:0;line-height:1.8;">
    <span leaf="">这里是重要提示或核心结论，绿色竖条提示「可操作」或「正向」信息。</span>
  </p>
</section>
```

**警示变体**（灰杏底 + 灰杏竖条，提示「注意」）：

```html
<section style="background:#FAF4EF;border-left:4px solid #D4B5A0;border-radius:0 10px 10px 0;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:600;color:#4A4A4A;margin:0;line-height:1.8;">
    <span leaf="">注意事项或需要留心的内容，温暖杏色提示「谨慎/注意」。</span>
  </p>
</section>
```

---

## 组件 10 图片容器

```html
<section style="background:#FFFFFF;border-radius:12px;padding:6px;border:1px solid #E3DBD9;box-shadow:0 2px 12px -2px rgba(181,130,140,0.08);margin-bottom:10px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

```html
<section style="background:#FFFFFF;border-radius:12px;padding:6px;border:1px solid #E3DBD9;box-shadow:0 2px 12px -2px rgba(181,130,140,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
<p style="font-size:12px;color:#A8A8A8;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#4A4A4A;">
  <span leaf="">加粗的结论性短句，色调偏深让其更有分量。</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#4A4A4A;">
  <span style="background:linear-gradient(180deg,transparent 60%,#D4B5A0 60%);"><span leaf="">荧光笔标记的结论句，灰杏底温柔点睛。</span></span>
</p>
```

---

## 组件 12 数据/要点卡片组

### 两列版（双莫兰迪色区分）

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F2ECEC;border-radius:12px;padding:20px 16px;margin-right:8px;text-align:center;border:1px solid #E3DBD9;">
    <p style="font-size:28px;font-weight:800;color:#B5828C;margin:0 0 6px;line-height:1;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#A8A8A8;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#EEF3F6;border-radius:12px;padding:20px 16px;text-align:center;border:1px solid #E3DBD9;">
    <p style="font-size:28px;font-weight:800;color:#8BA3B0;margin:0 0 6px;line-height:1;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#A8A8A8;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版（三莫兰迪色区分）

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F2ECEC;border-radius:12px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #E3DBD9;">
    <p style="font-size:24px;font-weight:800;color:#B5828C;margin:0 0 4px;line-height:1;"><span leaf="">85%</span></p>
    <p style="font-size:12px;color:#A8A8A8;margin:0;line-height:1.4;"><span leaf="">用户满意度</span></p>
  </section>
  <section style="flex:1;background:#EFF4EF;border-radius:12px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #E3DBD9;">
    <p style="font-size:24px;font-weight:800;color:#9CAF9C;margin:0 0 4px;line-height:1;"><span leaf="">2x</span></p>
    <p style="font-size:12px;color:#A8A8A8;margin:0;line-height:1.4;"><span leaf="">效率提升</span></p>
  </section>
  <section style="flex:1;background:#FAF4EF;border-radius:12px;padding:16px 10px;text-align:center;border:1px solid #E3DBD9;">
    <p style="font-size:24px;font-weight:800;color:#D4B5A0;margin:0 0 4px;line-height:1;"><span leaf="">30天</span></p>
    <p style="font-size:12px;color:#A8A8A8;margin:0;line-height:1.4;"><span leaf="">完成周期</span></p>
  </section>
</section>
```

### 要点列表卡片（纵向，带左色标）

```html
<section style="background:#F5F1F0;border-radius:12px;padding:20px 20px;margin-bottom:24px;border:1px solid #E3DBD9;">
  <section style="display:flex;align-items:flex-start;margin-bottom:14px;">
    <span style="display:inline-block;width:4px;height:16px;background:#B5828C;border-radius:2px;margin-right:14px;margin-top:3px;flex-shrink:0;"></span>
    <p style="font-size:15px;color:#4A4A4A;margin:0;line-height:1.7;font-weight:600;"><span leaf="">第一个要点标题</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;margin-bottom:14px;">
    <span style="display:inline-block;width:4px;height:16px;background:#8BA3B0;border-radius:2px;margin-right:14px;margin-top:3px;flex-shrink:0;"></span>
    <p style="font-size:15px;color:#4A4A4A;margin:0;line-height:1.7;font-weight:600;"><span leaf="">第二个要点标题</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;">
    <span style="display:inline-block;width:4px;height:16px;background:#9CAF9C;border-radius:2px;margin-right:14px;margin-top:3px;flex-shrink:0;"></span>
    <p style="font-size:15px;color:#4A4A4A;margin:0;line-height:1.7;font-weight:600;"><span leaf="">第三个要点标题</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 灰玫底深玫字（默认）

```html
<span style="display:inline-block;background:#F2ECEC;color:#8A5A63;font-size:12px;font-weight:600;padding:2px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 灰蓝底深蓝字

```html
<span style="display:inline-block;background:#EEF3F6;color:#5A7A8A;font-size:12px;font-weight:600;padding:2px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 灰绿底深绿字

```html
<span style="display:inline-block;background:#EFF4EF;color:#5A7A5A;font-size:12px;font-weight:600;padding:2px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 灰杏底深棕字（温暖）

```html
<span style="display:inline-block;background:#FAF4EF;color:#8A6A50;font-size:12px;font-weight:600;padding:2px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 描边胶囊（轻量）

```html
<span style="display:inline-block;border:1px solid #B5828C;color:#B5828C;font-size:12px;font-weight:600;padding:1px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 END 结尾分割线

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:60px;background:linear-gradient(to right,transparent,#B5828C);margin-right:14px;"></span>
      <span style="font-size:11px;color:#B5828C;letter-spacing:4px;font-weight:600;"><span leaf="">END</span></span>
      <span style="height:1px;width:60px;background:linear-gradient(to left,transparent,#B5828C);margin-left:14px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding:0 10px;">
  <p style="margin-bottom:16px;font-size:15px;line-height:1.8;text-align:justify;color:#6B6B6B;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容</span>
  </p>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#6B6B6B;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#B5828C;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#F5F1F0;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#6B6B6B;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 开头引言卡片（灰玫浅底 + 左灰玫竖条） -->
  <!-- 组件 2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding:0 10px 20px;">
    <!-- 组件 6 正文段落 x N -->
  </section>

  <!-- 3. 目录导航（三栏莫兰迪色区分） -->
  <!-- 组件 3 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件 4 灰玫渐变细线 -->

  <!-- 5. 第一章（灰玫色编号） -->
  <!-- 组件 5（灰玫圆角编号 01 + 标题） -->
  <!--   组件 6 正文 + 组件 7 高亮 + 组件 8 引用 + 组件 9 提示条 + 组件 10 图片 + 组件 12 数据卡片 -->

  <!-- 6. 章节分割线 -->

  <!-- 7. 第二章（灰蓝色编号） -->
  <!-- 组件 5（灰蓝圆角编号 02 + 标题） -->

  <!-- 8. 章节分割线 -->

  <!-- 9. 第三章（灰绿色编号） -->
  <!-- 组件 5（灰绿圆角编号 03 + 标题） -->

  <!-- ... 更多章节（04 用灰杏色，往后循环莫兰迪色）... -->

  <!-- 10. 章节分割线 -->

  <!-- 11. 结语章节（∞ 变体，回归灰玫） -->
  <!-- 组件 5（∞ 变体） -->

  <!-- 12. END 分割线 -->
  <!-- 组件 14 -->

  <!-- 13. 尾部签名 -->
  <!-- 组件 15 -->

</section>
```

---

## 视觉层级设计（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 灰玫加粗 `color:#B5828C` | 产品名、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 灰杏下划线 `#D4B5A0` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 左竖条 + 莫兰迪浅底 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 灰玫底白字标签（`background:#B5828C`）**仅在开头引言卡片内使用**，正文中用浅底深字替代
- 灰玫加粗全文不超过 5 处
- 引用/提示统一用左竖条 + 浅底，不用四周虚线框（dashed）
- 不同章节编号可轮换莫兰迪辅色（灰玫→灰蓝→灰绿→灰杏→循环），增加层次不刺眼
- 全局背景用 `#F5F1F0`（浅米灰），内容卡片用白色或各莫兰迪浅底，形成柔和层次

---

## Markdown → 莫兰迪温柔风排版映射规则表

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 灰玫浅底引言卡片 | 文章开头的引用，左灰玫竖条 |
| `## 章节标题` | 组件 5 章节标题 | 圆角胶囊编号 01/02/03…，不同章节轮换莫兰迪色，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记关键词灰杏下划线 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或灰玫加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅底深字标签 | 核心概念，每篇 2~4 个 |
| `<u>下划线</u>` | 组件 7d 灰杏下划线 | 2px `#D4B5A0` |
| `~~荧光笔~~` | 组件 7e 荧光笔 | 灰杏底部半高亮 |
| `> 引用段落`（金句） | 组件 8a 灰玫底左竖条 | 核心金句 |
| `> 引用段落`（内容/Prompt） | 组件 8b 灰蓝底左竖条 | Prompt、引用内容 |
| `> 引用段落`（旁注） | 组件 8c 细线左竖条旁注 | 轻量旁注 |
| `!> 正向提示` | 组件 9 灰绿底提示条 | 正向提醒、结论 |
| `!> 注意警示` | 组件 9 灰杏底警示变体 | 注意事项 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 可选说明 |
| 数据展示 | 组件 12 数据卡片组 | 莫兰迪色大号数据，多色区分 |
| 要点列表 | 组件 12 要点列表卡片 | 纵向带左色标，多色区分 |
| 行内标签 | 组件 13 标签胶囊 | 灰玫底为默认，多色可选 |
| `---` | 组件 4 章节分割线 | 灰玫渐变细线 |
| 文末 | 组件 14 + 15 | END 线 + 灰玫签名 |
