# 甲木公众号排版组件库 —— 焦糖棕知性风

> **使用说明**：本组件库为「焦糖棕知性风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：焦糖棕/琥珀色系、知性书卷气、温润沉稳、深度思考、咖啡馆氛围。
>
> **与其他色系的差异**：
> - 天蓝色系 → 轻盈、清透、散文感
> - 红黑色系 → 沉稳、力量、高级感
> - 绿色科技风 → 结构化、杂志感、产品评测风
> - **焦糖棕知性风** → **知性、书卷气、温润沉稳、深度思考、咖啡馆氛围**
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
主色调：       #B45309（焦糖棕/琥珀）
主色调深：     #92400E（深棕）
主色调浅：     #FCD34D（暖金黄）
主色调极浅：   #FEF3C7（淡暖黄）
主色调背景：   #FFFBEB（极淡暖底）
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

> 所有内容都放在这个最外层容器内，极淡暖底色营造纸质书页感

```html
<section style="max-width: 677px;margin: 0 auto;background: #FFFBEB;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

**效果说明**：极淡暖黄底色（#FFFBEB），模拟咖啡馆灯光下的纸质阅读感，温润不刺眼。

---

## 组件 2️⃣ 开头引言卡片（白底焦糖棕左边框）

> 白底 + 焦糖棕粗左边框 + 大号引号 + 棕色实底关键词高亮 + 右下署名

```html
<section style="margin:0 0 32px;background:#ffffff;border-left:5px solid #B45309;border-radius:4px 16px 16px 4px;box-shadow:0 4px 20px -4px rgba(180,83,9,0.12);padding:28px 24px 22px;overflow:hidden;">
  <p style="font-size:42px;color:#FCD34D;font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:800;color:#1C1917;margin:12px 0 8px;line-height:1.75;padding-left:4px;">
    <span leaf="">真正决定未来的，不是技术本身，而是</span>
    <span style="background:#B45309;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">驾驭技术</span></span>
    <span leaf=""> 的思维方式与</span>
    <span style="background:#B45309;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">认知深度</span></span>
    <span leaf="">。</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#9CA3AF;margin:8px 0 0;letter-spacing:1px;">
    <span leaf="">—— 甲木</span>
  </p>
</section>
```

**效果**：白底干净温润，焦糖棕左边框 + 暖金引号 + 棕色实底标签做点睛，书卷气十足。

---

## 组件 3️⃣ 三列目录卡片

> 三列目录导航，淡暖黄背景 + 棕色实底编号标签 + 深色标题

```html
<section style="padding: 0 10px 32px;">
  <p style="font-size: 14px;color: #9CA3AF;margin: 0 0 14px;letter-spacing:1px;">
    <span leaf="">📖 本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FEF3C7;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #FCD34D;">
      <p style="display:inline-block;background:#B45309;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex:1;background:#FEF3C7;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #FCD34D;">
      <p style="display:inline-block;background:#B45309;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex:1;background:#FEF3C7;border-radius:10px;padding:16px 12px;text-align:center;border:1px solid #FCD34D;">
      <p style="display:inline-block;background:#B45309;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

**效果说明**：淡暖黄底色卡片 + 焦糖棕编号标签，如同咖啡馆菜单的章节导引。

---

## 组件 4️⃣ 章节分割线

> 焦糖棕渐变分割线，两端渐隐，温润优雅

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #FCD34D, #B45309, #FCD34D, transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5️⃣ 章节标题（棕色编号标签 + 标题 + 3px主色底线）

> 棕色实底编号标签 + 英文小标签 + 中文大标题，底部 3px 焦糖棕底线

```html
<section style="margin-top: 48px;margin-bottom: 28px;padding: 0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #B45309;">
    <section style="display:flex;align-items:center;">
      <!-- 棕底编号标签 -->
      <span style="display:inline-block;background:#B45309;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#B45309;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
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
<span style="display:inline-block;background:#B45309;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

**效果说明**：焦糖棕编号标签沉稳有力，3px 底线强化章节分隔感，结语用 ∞ 收束全文。

---

## 组件 6️⃣ 正文段落

> **⚠️ 关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**焦糖棕下划线**进行标记（`border-bottom:2px solid #B45309;font-weight:600;`）。让读者快速扫到每段的重点。

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
  <span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**示例1 —— 思考类段落**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">我们正在经历一个深刻的范式转换：过去十年的技术红利来自</span>
  <span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">信息的数字化</span></span>
  <span leaf="">，而未来十年的真正机会，在于</span>
  <span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">决策的智能化</span></span>
  <span leaf="">。这不是渐进式的改良，而是底层逻辑的重写。</span>
</p>
```

**示例2 —— 分析类段落**：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;">
  <span leaf="">大多数人对 AI 的理解停留在工具层面，但真正值得关注的是它正在重塑</span>
  <span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">人与知识的关系</span></span>
  <span leaf="">。当获取答案的成本趋近于零，</span>
  <span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">提出好问题的能力</span></span>
  <span leaf="">反而成了最稀缺的资源。</span>
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
> 1. **7d 焦糖棕下划线** ⭐ — 正文默认标记方式，每段都应考虑使用
> 2. **7a 焦糖棕加粗** — 关键结论句
> 3. **7b 棕底白字标签** — 极少数最核心的概念（每篇 2~4 个）
> 4. **7c 浅暖黄背景** — 次要关键词补充
> 5. **7e 荧光笔** — 偶尔用于长句强调
> 6. **7f 粗下划线** — 全文最重要的一句话

### 7a. 焦糖棕加粗强调

> 用于关键观点、重要结论

```html
<strong style="color:#B45309;"><span leaf="">焦糖棕加粗强调的文字</span></strong>
```

### 7b. 棕底白字标签高亮

> 白字棕底，像标签贴纸一样醒目，仅用于最核心的概念（每篇 2~4 个）

```html
<span style="background:#B45309;color:#FFFFFF;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅暖黄背景高亮

> 柔和的暖黄背景标注，适用于次要关键词

```html
<span style="background:#FEF3C7;padding:1px 6px;border-radius:3px;font-weight:600;color:#92400E;"><span leaf="">浅暖黄背景关键词</span></span>
```

### 7d. 焦糖棕下划线 ⭐ 最常用

> **本风格的标志性标记方式**。每个正文段落都应主动找出关键词/关键句，用焦糖棕下划线标出。

```html
<span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">焦糖棕下划线标记的关键词</span></span>
```

### 7e. 荧光笔效果（底部半高亮）

> 底部 40% 暖黄高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg, transparent 60%, #FEF3C7 60%);font-weight:700;color:#1C1917;"><span leaf="">荧光笔效果的重要长句，底部 40% 暖黄高亮</span></span>
```

### 7f. 粗下划线（三像素）

> 全文最重要的一句话才使用

```html
<span style="border-bottom:3px solid #B45309;font-weight:600;"><span leaf="">三像素粗下划线，全文最强调</span></span>
```

---

## 组件 8️⃣ 引用高亮块（3 种变体）

### 8a. 焦糖棕左边线引用块（视觉焦点最强）

> 暖黄底 + 4px 焦糖棕左边线，用于核心观点

```html
<section style="background:#FFFBEB;border-radius:4px 10px 10px 4px;padding:20px 22px;margin-bottom:24px;border-left:4px solid #B45309;">
  <p style="font-size:16px;font-weight:800;color:#92400E;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 浅暖黄背景引用块

> 淡暖黄底 + 金黄边框，用于补充说明或引述

```html
<section style="background:#FEF3C7;border-radius:10px;padding:18px 20px;margin-bottom:24px;border:1px solid #FCD34D;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">浅暖黄引用内容，可以包含</span>
    <span style="border-bottom:2px solid #B45309;font-weight:600;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

### 8c. 焦糖棕左边线引用（简约版）

> 极简左边线 + 浅灰底，适用于轻量引述

```html
<section style="border-left:4px solid #B45309;padding:14px 20px;margin-bottom:24px;background:#F9FAFB;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">左边线引用内容，简洁温润</span>
  </p>
</section>
```

---

## 组件 9️⃣ 提示条

> 焦糖棕渐变背景条，用于重要提醒、核心结论

```html
<section style="background:linear-gradient(135deg,#B45309 0%,#92400E 100%);border-radius:8px;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#FFFFFF;margin:0;line-height:1.8;">
    <span leaf="">💡 这里是重要提示或核心结论，焦糖棕渐变底白字温润而醒目</span>
  </p>
</section>
```

---

## 组件 🔟 图片容器

> 图片的标准展示容器，带圆角、边框和暖色调阴影

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #E5E7EB;box-shadow: 0 4px 12px -2px rgba(180,83,9,0.08);margin-bottom: 10px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

```html
<section style="background: #FFF;border-radius: 12px;padding: 6px;border: 1px solid #E5E7EB;box-shadow: 0 4px 12px -2px rgba(180,83,9,0.08);margin-bottom: 8px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
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
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1C1917;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1C1917;">
  <span style="background:linear-gradient(180deg, transparent 60%, #FEF3C7 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

结合粗下划线的变体：

```html
<p style="margin-bottom: 20px;font-size: 15px;line-height: 1.8;text-align: justify;font-weight:700;color:#1C1917;">
  <span style="border-bottom:3px solid #B45309;"><span leaf="">加粗 + 下划线的最强调短句</span></span>
</p>
```

---

## 组件 1️⃣2️⃣ 数据卡片组

> 两列或三列的数据展示卡片，焦糖棕大号数字 + 灰色描述

### 两列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#FFFBEB;border-radius:10px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #FCD34D;">
    <p style="font-size:28px;font-weight:900;color:#B45309;margin:0 0 4px;line-height:1;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#FFFBEB;border-radius:10px;padding:18px 16px;text-align:center;border:1px solid #FCD34D;">
    <p style="font-size:28px;font-weight:900;color:#B45309;margin:0 0 4px;line-height:1;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#FFFBEB;border-radius:10px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #FCD34D;">
    <p style="font-size:24px;font-weight:900;color:#B45309;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#FFFBEB;border-radius:10px;padding:16px 10px;margin-right:6px;text-align:center;border:1px solid #FCD34D;">
    <p style="font-size:24px;font-weight:900;color:#B45309;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
  <section style="flex:1;background:#FFFBEB;border-radius:10px;padding:16px 10px;text-align:center;border:1px solid #FCD34D;">
    <p style="font-size:24px;font-weight:900;color:#B45309;margin:0 0 4px;line-height:1;"><span leaf="">数据</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">描述文字</span></p>
  </section>
</section>
```

---

## 组件 1️⃣3️⃣ 标签胶囊（3 种变体）

> 行内标签，用于标注类别、状态、工具名等

### 棕底白字（强调）

```html
<span style="display:inline-block;background:#B45309;color:#FFFFFF;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 焦糖棕描边（轻量）

```html
<span style="display:inline-block;border:1px solid #B45309;color:#B45309;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 深棕底（信息）

```html
<span style="display:inline-block;background:#92400E;color:#FFFFFF;font-size:12px;font-weight:600;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 1️⃣4️⃣ END 分割线

> 正文结束与尾部区域之间的装饰性分割

```html
<section style="padding: 0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:2px;width:60px;background:linear-gradient(to right,transparent,#B45309);margin-right:12px;"></span>
      <span style="font-size:11px;color:#B45309;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:2px;width:60px;background:linear-gradient(to left,transparent,#B45309);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 1️⃣5️⃣ 尾部签名区

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
    <strong style="color:#B45309;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 📐 完整文章模板骨架

```html
<section style="max-width: 677px;margin: 0 auto;background: #FFFBEB;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #374151;line-height: 1.75;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- ① 开头引言卡片（白底焦糖棕左边框） -->
  <!-- 组件2 -->

  <!-- ② 前言正文（开场白） -->
  <section style="padding: 0 10px 20px;">
    <!-- 组件6 正文段落 × N -->
  </section>

  <!-- ③ 目录导航 -->
  <!-- 组件3 三列目录卡片 -->

  <!-- ④ 章节分割线 -->
  <!-- 组件4 焦糖棕渐变分割线 -->

  <!-- ⑤ 第一章 -->
  <!-- 组件5（棕底编号标签 01 + 标题） -->
  <!--   组件6正文 + 组件7高亮 + 组件8引用 + 组件9提示条 + 组件10图片 + 组件12数据卡片 -->

  <!-- ⑥ 章节分割线 -->

  <!-- ⑦ 第二章 -->
  <!-- 组件5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- ⑧ 章节分割线 -->

  <!-- ⑨ 结语章节 -->
  <!-- 组件5（∞ 棕底标签变体） -->

  <!-- ⑩ END 分割线 -->
  <!-- 组件14 -->

  <!-- ⑪ 尾部签名 -->
  <!-- 组件15 -->

</section>
```

---

## 🔧 Markdown → 焦糖棕知性风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 白底焦糖棕引言卡片 | 文章开头的引用 |
| `## 章节标题` | 组件 5 章节标题 | 棕底编号标签 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，每段标注 1~3 个关键词下划线 |
| `**加粗文字**` | 组件 7a 焦糖棕加粗 | 焦糖棕 #B45309 |
| `==高亮文字==` | 组件 7b 棕底白字标签 | 最强高亮 |
| `<u>下划线</u>` | 组件 7d 焦糖棕下划线 | 2px 焦糖棕 |
| `> 引用段落` | 组件 8a/8b/8c | 左边线/浅暖黄/简约版三选一 |
| `!> 提示文字` | 组件 9 提示条 | 焦糖棕渐变全宽条 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 说明 |
| 加粗段落 | 组件 11 加粗段落 | 结论性短句 |
| 数据展示 | 组件 12 数据卡片组 | 焦糖棕大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 三种风格可选 |
| `---` | 组件 4 章节分割线 | 焦糖棕渐变 |
| 文末 | 组件 14 + 15 | END线 + 签名 |

---

## 🆚 四套主题风格对照

| 设计元素 | 天蓝色系 | 红黑色系 | 绿色科技风 | **焦糖棕知性风** |
|---|---|---|---|---|
| 主色 | `#0EA5E9` | `#DC2626` | `#10B981` | **`#B45309`** |
| 页面底色 | 白色 | 白色 | 白色 | **极淡暖黄 `#FFFBEB`** |
| 文章开头 | 引号金句卡片 | 白底红色左边框 | Hero 封面大卡片 | **白底焦糖棕左边框 + 暖金引号** |
| 目录导航 | 三列编号文字 | 红底白字编号卡片 | 三列彩色卡片 | **暖黄底 + 棕底编号标签** |
| 分割线 | 灰色渐变 | 红色渐变 | 灰色实线 | **焦糖棕渐变（暖金→棕→暖金）** |
| 章节标题 | 英文标签 + 水印编号 | 红底编号标签 | 大号编号 + 竖线 | **棕底编号标签 + 3px 底线** |
| 关键词标记 | 蓝色下划线 | 红色下划线 | 绿色下划线 | **焦糖棕下划线** |
| 引用块 | 浅蓝渐变 | 暗底/浅红/左边线 | 灰底居中/黑底 | **暖黄底 + 棕色左边线** |
| 荧光笔 | 蓝色底 | 红色底 | 黄色底 | **暖黄底** |
| 文章结尾 | END 渐变线 + 签名 | END 渐变线 + 签名 | CTA 互动卡片 | **焦糖棕 END 线 + 签名** |
| 整体气质 | 散文、轻盈 | 沉稳、力量 | 杂志、结构 | **知性、书卷气、咖啡馆** |
