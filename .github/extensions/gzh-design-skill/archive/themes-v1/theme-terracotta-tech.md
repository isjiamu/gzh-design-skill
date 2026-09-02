# 甲木公众号排版组件库 —— 黑白灰科技风

> **使用说明**：本组件库基于「绿色科技风」结构，使用暖灰 + 赤陶点缀色调重新演绎。所有组件使用**内联样式**，直接复制粘贴到微信公众号编辑器即可。
>
> **设计风格**：暖灰基底 + 赤陶点缀、科技杂志风、卡片化布局、信息结构感强、标签化导航。追求高端科技期刊的温润质感与排版节奏，不再冰冷工业，而是有温度的克制。
>
> **色彩哲学**：
> - 暖灰色系（stone 色板）取代冷灰，整体氛围从「不锈钢」变为「手工纸」
> - 赤陶 #B05A3C 仅出现在结构地标（圆点、竖线、激活态、CTA），≤5 处点缀
> - 暖墨 #292524 取代纯黑，用于深底卡片和引用，带有微妙暖调
>
> **与其他色系的差异**：
> - 黑白灰色系（红白结构）→ 编号标签 + 虚线框引用，经典编辑风
> - 绿色科技风 → 翡翠绿，产品评测感，杂志风
> - **黑白灰科技风** → **暖灰 + 赤陶的杂志科技感，Hero 大卡片、竖线分隔、Case 子章节、CTA 互动，结构感最强，温度感最佳**

---

## 设计变量速查表

```
点缀色：       #B05A3C（赤陶/砖红 — 圆点、竖线、激活态、CTA）
暖墨（深底）：  #292524（Hero 底栏、黑底引用）
标题色：       #1C1917（深炭）
正文色：       #44403C（炭灰）
副文字色：     #78716C（砂岩灰）
极淡文字色：   #A8A29E（浅砂岩，装饰线/标签用）
下划线标记：   #D6D3D1（暖石下划线）
荧光笔：       #E7E5E4（暖灰底）
卡片背景：     #F5F5F4（米白）
全局背景：     #FAFAF8（暖白）
卡片边框：     #E7E5E4
分割线色：     #E7E5E4
Banner 标签底：#44403C（炭灰）
正文字号：     15px
行高：         1.8
字间距：       0.5px
内容区边距：   0 10px
```

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FAFAF8;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#44403C;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 Hero 封面大卡片（本风格核心特色）

> 文章顶部的 Hero 卡片：主题标签 + 赤陶圆点 + 日期 + 标题（双色调：深炭 + 砂岩灰）+ 赤陶短横线 + 副标题 + 底部暖墨 Banner

**完整版 Hero 卡片**（带底部 Banner）：

```html
<section style="margin:0 0 32px;border:1px solid #E7E5E4;border-radius:16px;overflow:hidden;box-shadow:0 2px 16px -4px rgba(41,37,36,0.08);">
  <!-- 顶部主题标签行 -->
  <section style="padding:20px 24px 0;">
    <section style="display:flex;align-items:center;justify-content:space-between;">
      <section style="display:flex;align-items:center;">
        <span style="display:inline-block;width:8px;height:8px;background:#B05A3C;border-radius:50%;margin-right:10px;vertical-align:middle;font-size:0;overflow:hidden;">.</span>
        <span style="font-size:12px;font-weight:700;color:#78716C;letter-spacing:4px;">TOPIC TAG</span>
      </section>
      <span style="font-size:13px;color:#A8A29E;letter-spacing:1px;"><span leaf="">2026.03</span></span>
    </section>
    <!-- 连接线：赤陶30% + 暖灰 -->
    <section style="height:1px;background:linear-gradient(to right,#B05A3C 30%,#E7E5E4 30%);margin:10px 0 0;"></section>
  </section>
  <!-- 主内容区 -->
  <section style="padding:20px 24px 24px;">
    <p style="font-size:14px;color:#A8A29E;margin:0 0 8px;font-weight:400;">
      <span leaf="">副标题提问句</span>
    </p>
    <p style="font-size:28px;font-weight:900;color:#1C1917;margin:0;line-height:1.3;">
      <span leaf="">主标题前半</span>
    </p>
    <p style="font-size:28px;font-weight:900;color:#78716C;margin:0 0 0;line-height:1.3;">
      <span leaf="">主标题后半（砂岩灰）</span>
    </p>
    <section style="width:40px;height:3px;background:#B05A3C;border-radius:2px;margin:16px 0;"></section>
    <p style="font-size:15px;color:#78716C;margin:0;">
      <span leaf="">一句话概括</span>
    </p>
  </section>
  <!-- 底部暖墨 Banner 条 -->
  <section style="background:#292524;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-size:14px;font-weight:700;color:#FAFAF8;"><span leaf="">Banner 文案</span></span>
    <section style="display:flex;">
      <span style="background:#44403C;color:#FAFAF8;font-size:12px;font-weight:600;padding:4px 14px;border-radius:4px;margin-left:8px;"><span leaf="">标签A</span></span>
      <span style="background:#44403C;color:#FAFAF8;font-size:12px;font-weight:600;padding:4px 14px;border-radius:4px;margin-left:8px;"><span leaf="">标签B</span></span>
    </section>
  </section>
</section>
```

**简化版 Hero 卡片**（无底部 Banner，适用于一般文章）：

```html
<section style="margin:0 0 32px;border:1px solid #E7E5E4;border-radius:16px;overflow:hidden;box-shadow:0 2px 16px -4px rgba(41,37,36,0.08);padding:24px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <section style="display:flex;align-items:center;">
      <span style="display:inline-block;width:8px;height:8px;background:#B05A3C;border-radius:50%;margin-right:10px;vertical-align:middle;font-size:0;overflow:hidden;">.</span>
      <span style="font-size:12px;font-weight:700;color:#78716C;letter-spacing:4px;">TOPIC TAG</span>
    </section>
    <span style="font-size:13px;color:#A8A29E;letter-spacing:1px;"><span leaf="">2026.03</span></span>
  </section>
  <p style="font-size:14px;color:#A8A29E;margin:0 0 8px;">
    <span leaf="">副标题提问句</span>
  </p>
  <p style="font-size:26px;font-weight:900;color:#1C1917;margin:0;line-height:1.3;">
    <span leaf="">主标题前半</span>
  </p>
  <p style="font-size:26px;font-weight:900;color:#78716C;margin:0;line-height:1.3;">
    <span leaf="">主标题后半（砂岩灰）</span>
  </p>
  <section style="width:40px;height:3px;background:#B05A3C;border-radius:2px;margin:16px 0;"></section>
  <p style="font-size:15px;color:#78716C;margin:0;">
    <span leaf="">一句话概括</span>
  </p>
</section>
```

---

## 组件 3 横向目录导航卡片

> Hero 卡片下方的结构化目录，三列卡片，第一个用赤陶色激活

```html
<!-- 面包屑索引行 -->
<section style="padding:0 10px;margin-bottom:12px;">
  <section style="display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:13px;color:#78716C;margin:0;">
      <span leaf="">01 推理范式 · 02 融合之难 · /// 最后</span>
    </p>
    <p style="font-size:12px;color:#A8A29E;margin:0;">
      <span leaf="">INDEX</span>
    </p>
  </section>
</section>
<!-- 三列目录卡片 -->
<section style="padding:0 10px 32px;display:flex;">
  <!-- 卡片1：赤陶激活态 -->
  <section style="flex:1;background:#292524;border-radius:12px;padding:16px;margin-right:8px;">
    <p style="font-size:11px;font-weight:700;color:#B05A3C;letter-spacing:2px;margin:0 0 6px;">
      <span leaf="">PART 01</span>
    </p>
    <p style="font-size:16px;font-weight:800;color:#FAFAF8;margin:0 0 4px;">
      <span leaf="">章节名称</span>
    </p>
    <p style="font-size:12px;color:rgba(250,250,248,0.5);margin:0;">
      <span leaf="">简短描述</span>
    </p>
  </section>
  <!-- 卡片2：米白默认态 -->
  <section style="flex:1;background:#FAFAF8;border:1px solid #E7E5E4;border-radius:12px;padding:16px;margin-right:8px;">
    <p style="font-size:11px;font-weight:700;color:#A8A29E;letter-spacing:2px;margin:0 0 6px;">
      <span leaf="">PART 02</span>
    </p>
    <p style="font-size:16px;font-weight:800;color:#1C1917;margin:0 0 4px;">
      <span leaf="">章节名称</span>
    </p>
    <p style="font-size:12px;color:#78716C;margin:0;">
      <span leaf="">简短描述</span>
    </p>
  </section>
  <!-- 卡片3：米白默认态 -->
  <section style="flex:1;background:#FAFAF8;border:1px solid #E7E5E4;border-radius:12px;padding:16px;">
    <p style="font-size:11px;font-weight:700;color:#A8A29E;letter-spacing:2px;margin:0 0 6px;">
      <span leaf="">PART ///</span>
    </p>
    <p style="font-size:16px;font-weight:800;color:#1C1917;margin:0 0 4px;">
      <span leaf="">写在最后</span>
    </p>
    <p style="font-size:12px;color:#78716C;margin:0;">
      <span leaf="">简短描述</span>
    </p>
  </section>
</section>
```

---

## 组件 4 章节标题（大号编号 + 赤陶竖线 + 标题）

> 左侧大号深炭编号 + PART 标签，赤陶竖线分隔，右侧标题 + 砂岩灰英文副标签

```html
<section style="padding:48px 20px 24px;">
  <section style="display:flex;align-items:flex-start;">
    <!-- 左侧编号区 -->
    <section style="margin-right:16px;flex-shrink:0;text-align:center;">
      <p style="font-size:36px;font-weight:900;color:#1C1917;margin:0;line-height:1;">
        <span leaf="">01</span>
      </p>
      <p style="font-size:10px;font-weight:700;color:#78716C;letter-spacing:3px;margin:4px 0 0;">
        <span leaf="">PART</span>
      </p>
    </section>
    <!-- 赤陶竖线分隔 -->
    <section style="width:3px;background:#B05A3C;border-radius:2px;margin-right:16px;flex-shrink:0;min-height:50px;"></section>
    <!-- 右侧标题区 -->
    <section>
      <h3 style="font-size:18px;font-weight:800;color:#1C1917;margin:0 0 4px;letter-spacing:0.5px;">
        <span leaf="">中文章节标题</span>
      </h3>
      <p style="font-size:11px;color:#A8A29E;margin:0;letter-spacing:2px;">
        <span style="font-weight:700;color:#78716C;"><span leaf="">ENGLISH</span></span>
        <span leaf=""> · 简短描述</span>
      </p>
    </section>
  </section>
</section>
```

**结语章节变体**（用 `///` 替代数字编号）：

```html
<section style="padding:48px 20px 24px;">
  <section style="display:flex;align-items:flex-start;">
    <section style="margin-right:16px;flex-shrink:0;text-align:center;">
      <p style="font-size:32px;font-weight:900;color:#1C1917;margin:0;line-height:1;letter-spacing:-2px;">
        <span leaf="">///</span>
      </p>
      <p style="font-size:10px;font-weight:700;color:#78716C;letter-spacing:3px;margin:4px 0 0;">
        <span leaf="">LAST</span>
      </p>
    </section>
    <section style="width:3px;background:#B05A3C;border-radius:2px;margin-right:16px;flex-shrink:0;min-height:50px;"></section>
    <section>
      <h3 style="font-size:18px;font-weight:800;color:#1C1917;margin:0 0 4px;letter-spacing:0.5px;">
        <span leaf="">写在最后</span>
      </h3>
      <p style="font-size:11px;color:#A8A29E;margin:0;letter-spacing:2px;">
        <span style="font-weight:700;color:#78716C;"><span leaf="">INSIGHT</span></span>
        <span leaf=""> · 简短描述</span>
      </p>
    </section>
  </section>
</section>
```

---

## 组件 5 正文段落

> **关键规则**：每个正文段落中，应主动识别 1~3 个关键语句或关键词，用暖石下划线（6c）进行标记。

**基础段落**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;padding:0 10px;color:#44403C;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;padding:0 10px;color:#44403C;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #D6D3D1;font-weight:600;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

---

## 组件 6 正文高亮样式（5 种变体）

### 6a. 深炭加粗强调

> 用于关键锚点（产品名、步骤编号、CTA），全文不超过 5 处

```html
<strong style="color:#1C1917;"><span leaf="">深炭加粗强调的关键句</span></strong>
```

### 6b. 暖灰荧光笔高亮

> 底部 40% 暖灰高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg,transparent 60%,#E7E5E4 60%);font-weight:700;color:#1C1917;"><span leaf="">荧光笔高亮的重要文字</span></span>
```

### 6c. 暖石下划线 -- 最常用

> 本风格的标志性标记方式，暖石色温和内敛

```html
<span style="border-bottom:2px solid #D6D3D1;font-weight:600;"><span leaf="">下划线强调文字</span></span>
```

### 6d. 米白背景高亮

> 轻量关键词标注

```html
<span style="background:#F5F5F4;border:1px solid #E7E5E4;padding:1px 6px;border-radius:3px;font-weight:600;color:#1C1917;"><span leaf="">米白背景关键词</span></span>
```

### 6e. 加粗正文段落

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;padding:0 10px;font-weight:700;color:#1C1917;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

---

## 组件 7 Case 子章节标题（标签式）

> 用于论点分论、步骤教程等子项目。赤陶空心圆 + 暖墨编号标签 + 标题

```html
<section style="padding:0 10px;margin-bottom:8px;">
  <section style="display:flex;align-items:center;">
    <span style="display:inline-block;width:12px;height:12px;border:2px solid #B05A3C;border-radius:50%;margin-right:12px;flex-shrink:0;font-size:0;overflow:hidden;">.</span>
    <span style="background:#292524;color:#FAFAF8;font-size:11px;font-weight:700;padding:3px 10px;border-radius:4px;margin-right:10px;letter-spacing:1px;"><span leaf="">CASE 01</span></span>
    <span style="font-size:16px;font-weight:700;color:#1C1917;"><span leaf="">子章节标题</span></span>
  </section>
</section>
```

**Case 副标签**（标题下方小字描述）：

```html
<section style="padding:0 10px;margin-bottom:16px;margin-left:24px;">
  <p style="font-size:12px;color:#78716C;margin:0;letter-spacing:1px;">
    <span leaf="">KEYWORD · 简短描述</span>
  </p>
</section>
```

**场景描述句**（深色加粗引导句）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;padding:0 10px;font-weight:600;color:#1C1917;">
  <span leaf="">场景引导句，描述一个具体的情境</span>
</p>
```

---

## 组件 8 引用块（居中金句）

### 8a. 米白底居中金句

> 米白底色 + 居中加粗金句，用于核心观点

```html
<section style="padding:0 10px;margin-bottom:24px;">
  <section style="background:#F5F5F4;border:1px solid #E7E5E4;border-radius:12px;padding:24px 20px;">
    <p style="font-size:17px;font-weight:800;color:#1C1917;margin:0;line-height:1.8;text-align:center;">
      <span leaf="">「这里是核心观点或关键金句。」</span>
    </p>
  </section>
</section>
```

### 8b. 暖墨底白字引用（强调变体）

> 暖墨底 + 暖白字，视觉冲击力最强，温暖而有力

```html
<section style="padding:0 10px;margin-bottom:24px;">
  <section style="background:#292524;border-radius:12px;padding:24px 20px;">
    <p style="font-size:17px;font-weight:800;color:#FAFAF8;margin:0;line-height:1.8;text-align:center;">
      <span leaf="">「这里是最核心的观点。」</span>
    </p>
  </section>
</section>
```

---

## 组件 9 概念/工具徽章列表

> 赤陶圆点标记 + 米白底徽章标签 + 下方描述

```html
<section style="padding:0 10px;margin-bottom:20px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#F5F5F4;border:1px solid #E7E5E4;border-radius:6px;padding:2px 12px;font-size:14px;font-weight:700;color:#1C1917;">
      <span leaf="">● 概念名称</span>
    </span>
  </p>
  <p style="font-size:14px;color:#44403C;margin:0;line-height:1.8;">
    <span leaf="">概念描述说明</span>
  </p>
</section>
```

---

## 组件 10 居中高亮句

> 用于章节结束前的点睛之笔，深炭加粗居中

```html
<p style="font-size:16px;font-weight:700;color:#1C1917;text-align:center;margin:32px 20px;line-height:1.8;">
  <span leaf="">这里是章节结尾的点睛之笔</span>
</p>
```

---

## 组件 11 图片容器

```html
<section style="padding:0 10px;margin-bottom:10px;">
  <section style="background:#FAFAF8;border-radius:12px;padding:6px;border:1px solid #E7E5E4;box-shadow:0 4px 6px -1px rgba(41,37,36,0.05);">
    <section style="margin:0;border-radius:8px;overflow:hidden;">
      <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
    </section>
  </section>
</section>
```

图片 + 说明文字：

```html
<section style="padding:0 10px;margin-bottom:8px;">
  <section style="background:#FAFAF8;border-radius:12px;padding:6px;border:1px solid #E7E5E4;box-shadow:0 4px 6px -1px rgba(41,37,36,0.05);">
    <section style="margin:0;border-radius:8px;overflow:hidden;">
      <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
    </section>
  </section>
</section>
<p style="font-size:12px;color:#A8A29E;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 12 分割线

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#E7E5E4,transparent);margin:8px 0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 13 尾部 CTA 互动卡片

> 圆角大卡片，居中文案 + 三个图标按钮（转发按钮用赤陶色）+ THANKS FOR READING

```html
<section style="padding:0 10px;margin-top:32px;">
  <section style="height:1px;background:#E7E5E4;margin:0 0 32px;"></section>
  <section style="border:1px solid #E7E5E4;border-radius:20px;padding:32px 24px;text-align:center;margin-bottom:32px;">
    <p style="font-size:17px;font-weight:700;color:#1C1917;margin:0 0 24px;line-height:1.6;">
      <span leaf="">觉得有用，随手点个赞、在看、转发三连吧</span>
    </p>
    <section style="display:flex;justify-content:center;margin-bottom:8px;">
      <section style="text-align:center;margin:0 16px;">
        <section style="width:48px;height:48px;background:#F5F5F4;border-radius:12px;margin:0 auto 6px;line-height:48px;font-size:22px;">
          <span leaf="">&#x1F44D;</span>
        </section>
        <p style="font-size:12px;color:#44403C;margin:0;"><span leaf="">点赞</span></p>
      </section>
      <section style="text-align:center;margin:0 16px;">
        <section style="width:48px;height:48px;background:#F5F5F4;border-radius:12px;margin:0 auto 6px;line-height:48px;font-size:22px;">
          <span leaf="">&#x1F440;</span>
        </section>
        <p style="font-size:12px;color:#44403C;margin:0;"><span leaf="">在看</span></p>
      </section>
      <section style="text-align:center;margin:0 16px;">
        <section style="width:48px;height:48px;background:#B05A3C;border-radius:12px;margin:0 auto 6px;line-height:48px;font-size:22px;">
          <span style="color:#FAFAF8;" leaf="">&#x2197;</span>
        </section>
        <p style="font-size:12px;color:#B05A3C;font-weight:600;margin:0;"><span leaf="">转发</span></p>
      </section>
    </section>
    <p style="font-size:11px;color:#A8A29E;letter-spacing:3px;margin:16px 0 0;">
      <span leaf="">THANKS FOR READING</span>
    </p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FAFAF8;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#44403C;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. Hero 封面大卡片 -->
  <!-- 组件2 -->

  <!-- 2. 横向目录导航 -->
  <!-- 组件3 -->

  <!-- 3. 第一章 -->
  <!-- 组件4（章节标题 01 / PART） -->
  <!--   组件5正文 + 组件6高亮 + 组件7 Case + 组件8引用 + 组件11图片 -->

  <!-- 4. 第二章 -->
  <!-- 组件4（02 / PART） -->

  <!-- ... 更多章节 ... -->

  <!-- 5. 结语章节 -->
  <!-- 组件4 结语变体（/// / LAST） -->

  <!-- 6. 居中高亮句（结尾点睛） -->
  <!-- 组件10 -->

  <!-- 7. CTA 互动卡片 -->
  <!-- 组件13 -->

</section>
```

---

## 视觉层级设计（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 深炭加粗 `color:#1C1917` / 暖墨底白字引用 / 赤陶竖线+圆点 | 产品名、步骤、CTA、核心金句、结构地标 | 全文 ≤5 处 |
| **标记层** | 暖石下划线 `#D6D3D1` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 米白底引用 / 米白徽章 / 暖灰荧光笔 | 引用块、概念标签、长句强调 | 按需 |

---

## Markdown -> 黑白灰科技风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| YAML frontmatter / `# 标题` | 组件 2 Hero 卡片 | 提取标题拆分双色调（深炭 + 砂岩灰） |
| `## 章节标题` | 组件 4 章节标题 | 自动编号 01/02... 最后用 /// |
| `### Case 标题` | 组件 7 Case 子章节 | 暖墨底编号标签 + 赤陶空心圆 |
| 普通段落 | 组件 5 正文段落 | 默认样式，主动标记暖石下划线 |
| `**加粗文字**` | 组件 6a 深炭加粗 | 仅限关键锚点 |
| `==高亮文字==` | 组件 6b 暖灰荧光笔 | 底部暖灰标记 |
| `<u>下划线</u>` | 组件 6c 暖石下划线 | 2px `#D6D3D1` |
| `> 引用段落` | 组件 8 引用块 | 米白底/暖墨底居中金句 |
| `![](图片)` | 组件 11 图片容器 | 圆角卡片 |
| 概念/工具列表 | 组件 9 徽章列表 | 米白底徽章 |
| `---` | 组件 12 分割线 | 渐变暖灰线 |
| 文末 | 组件 13 CTA 卡片 | 三连互动（转发按钮赤陶色） |
