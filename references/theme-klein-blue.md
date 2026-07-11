# 公众号排版组件库 —— 克莱因蓝艺术展册

> **使用说明**：本组件库将克莱因蓝、鸿蒙无衬线、几何细线与大面积纯白留白转译为微信公众号可用的内联 HTML。适合观点文章、艺术评论、品牌叙事、作品集、访谈与结构化教程。
>
> **设计原则**：正文保持白底与稳定阅读；`#002FA7` 只承担标题、细线、标签、关键引用和少量强锚点；深蓝色块每屏不超过一个；装饰统一使用圆点、四角星、菱形和 1px 细线。
>
> **微信兼容规则**：所有文字节点必须置于 `<span leaf="">`；装饰空元素放 `<span leaf=""><br></span>`；禁用 style 与 script 标签、class 与 id 属性、div 与 svg 标签、复杂定位、Grid、CSS 变量与交互；所有文字字号不超过 `24px`。

---

## 设计变量速查表

```text
主题名称：       克莱因蓝艺术展册
主题 ID：        klein-blue
主色：           #002FA7（Klein Blue）
主色深：         #001E78（深蓝引用 / 封面渐变）
主色亮：         #0648D8（渐变高光 / 次级进度）
浅蓝：           #E8ECFF（标签底 / 弱强调底）
极浅蓝：         #F3F6FF（导读 / 提示 / 代码底）
纯白：           #FFFFFF（文章背景）
标题色：         #111111
正文色：         #434650
辅助文字：       #7D86A5
细线：           #D8E1F6
强细线：         #B8C8F5
正文：           16px / line-height 1.75
内容区边距：     0 10px
章节间距：       48px
常规圆角：       4px–8px；标签 999px；封面图可用拱门圆角
轻阴影：         0 6px 18px rgba(0,47,167,0.08)
强调阴影：       0 8px 24px rgba(0,47,167,0.16)
```

中文字体栈：`'HarmonyOS Sans SC','HarmonyOS Sans','PingFang SC','Microsoft YaHei','Noto Sans CJK SC',sans-serif`

英文与编号：`Georgia,'Times New Roman',serif`

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;color:#111111;font-family:'HarmonyOS Sans SC','HarmonyOS Sans','PingFang SC','Microsoft YaHei','Noto Sans CJK SC',sans-serif;line-height:1.75;letter-spacing:0.3px;overflow-x:hidden;">
  <!-- 所有文章组件放在这里 -->
</section>
```

---

## 组件 2 展册刊头

> 用于内文封面顶部。仅保留圆点、细线和英文栏目字，避免固定中文刊头干扰账号品牌。

```html
<section style="margin:0;padding:24px 18px 18px;background:#FFFFFF;box-sizing:border-box;">
  <section style="display:flex;align-items:center;">
    <span style="display:inline-block;width:8px;height:8px;margin-right:9px;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    <span style="flex:1;height:1px;margin:0 10px 0 0;background:#D8E1F6;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    <span style="font-family:Georgia,'Times New Roman',serif;font-size:9px;color:#002FA7;letter-spacing:1px;"><span leaf="">KLEIN BLUE · ✦</span></span>
  </section>
</section>
```

---

## 组件 3 纯蓝宣言封面

> 观点、访谈、随笔类文章的默认封面。每篇最多一个。

```html
<section style="margin:0 10px 36px;padding:34px 22px;background:linear-gradient(135deg,#002FA7 0%,#0648D8 52%,#001E78 100%);border-radius:6px;box-shadow:0 8px 24px rgba(0,47,167,0.16);box-sizing:border-box;">
  <p style="margin:0 0 26px;font-family:Georgia,'Times New Roman',serif;font-size:10px;color:#E8ECFF;letter-spacing:2px;"><span leaf="">BLUE MANIFESTO</span></p>
  <p style="margin:0 0 18px;font-size:24px;line-height:1.4;font-weight:600;color:#FFFFFF;"><span leaf="">宣言标题占位：让颜色成为观点，而不是装饰</span></p>
  <p style="margin:0;font-size:15px;line-height:1.9;color:#FFFFFF;"><span leaf="">宣言说明占位：这里展示一段具有判断力的开场文字，以纯蓝色块建立全文最强视觉锚点。</span></p>
</section>
```

---

## 组件 4 编号索引封面

> 数据报告、工具盘点与结构型文章的索引封面；与组件 3 二选一。

```html
<section style="margin:0 10px 36px;padding:26px 22px 24px;background:#FFFFFF;border:1px solid #D8E1F6;border-right:8px solid #002FA7;box-shadow:0 6px 18px rgba(0,47,167,0.08);box-sizing:border-box;">
  <p style="margin:0 0 12px;font-family:Georgia,'Times New Roman',serif;font-size:24px;line-height:1;color:#002FA7;"><span leaf="">01</span></p>
  <span style="display:block;width:72px;height:1px;margin:0 0 22px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span>
  <p style="margin:0 0 14px;font-size:20px;line-height:1.45;font-weight:600;color:#002FA7;"><span leaf="">专题标题占位：一个结构问题的展开方式</span></p>
  <p style="margin:0 0 16px;font-size:14px;line-height:1.8;color:#434650;"><span leaf="">封面说明占位：用简短文字说明本篇的核心问题、观察尺度与阅读价值。</span></p>
  <p style="margin:0;font-size:11px;line-height:1.9;color:#7D86A5;"><span leaf="">深度占位　理性占位　自由占位　纯粹占位</span></p>
</section>
```

---

## 组件 5 专题摘要导读

```html
<section style="margin:0 10px 32px;padding:20px 18px;background:#F3F6FF;border-top:1px solid #002FA7;border-bottom:1px solid #D8E1F6;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-family:Georgia,'Times New Roman',serif;font-size:10px;color:#002FA7;letter-spacing:2px;"><span leaf="">LEAD · 专题摘要</span></p>
  <p style="margin:0;font-size:16px;line-height:1.85;font-weight:600;color:#111111;"><span leaf="">一句话导读占位：本篇将从结构、方法与边界三个层面展开，并保留足够留白供读者形成自己的判断。</span></p>
</section>
```

---

## 组件 6 三段目录索引

> 三个及以上章节时生成，精选三个核心看点，不罗列所有章节。

```html
<section style="margin:0 10px 36px;padding:22px 18px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 16px;font-size:11px;color:#7D86A5;letter-spacing:2px;"><span leaf="">本文看点 · CONTENTS</span></p>
  <section style="margin:0 0 14px;padding:0 0 14px;border-bottom:1px solid #E8ECFF;display:flex;align-items:baseline;">
    <span style="width:34px;margin-right:10px;font-family:Georgia,'Times New Roman',serif;font-size:18px;color:#002FA7;"><span leaf="">01</span></span>
    <span style="font-size:14px;line-height:1.6;font-weight:600;color:#111111;"><span leaf="">核心看点占位：问题如何被看见</span></span>
  </section>
  <section style="margin:0 0 14px;padding:0 0 14px;border-bottom:1px solid #E8ECFF;display:flex;align-items:baseline;">
    <span style="width:34px;margin-right:10px;font-family:Georgia,'Times New Roman',serif;font-size:18px;color:#002FA7;"><span leaf="">02</span></span>
    <span style="font-size:14px;line-height:1.6;font-weight:600;color:#111111;"><span leaf="">核心看点占位：结构如何被建立</span></span>
  </section>
  <section style="margin:0;display:flex;align-items:baseline;">
    <span style="width:34px;margin-right:10px;font-family:Georgia,'Times New Roman',serif;font-size:18px;color:#002FA7;"><span leaf="">03</span></span>
    <span style="font-size:14px;line-height:1.6;font-weight:600;color:#111111;"><span leaf="">核心看点占位：结论如何被复用</span></span>
  </section>
</section>
```

---

## 组件 7 编号章节标题

> 第一章 `margin-top:20px`，后续章 `48px`。普通章使用 `01/02…`；结语章改为 `∞ + THE END`。

```html
<section style="margin:48px 10px 28px;padding:0;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-family:Georgia,'Times New Roman',serif;font-size:24px;line-height:1;color:#002FA7;"><span leaf="">01</span></p>
  <span style="display:block;width:82px;height:1px;margin:0 0 16px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span>
  <p style="margin:0 0 5px;font-size:21px;line-height:1.45;font-weight:600;color:#002FA7;"><span leaf="">章节标题占位：建立属于内容的秩序</span></p>
  <p style="margin:0;font-size:10px;color:#7D86A5;letter-spacing:2px;"><span leaf="">STRUCTURE · INSIGHT</span></p>
</section>
```

结语变体：

```html
<section style="margin:48px 10px 28px;padding:18px 0;border-top:1px solid #D8E1F6;border-bottom:1px solid #D8E1F6;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 8px;font-family:Georgia,'Times New Roman',serif;font-size:24px;color:#002FA7;line-height:1;"><span leaf="">∞</span></p>
  <p style="margin:0 0 5px;font-size:20px;line-height:1.45;font-weight:600;color:#002FA7;"><span leaf="">结语标题占位：把答案留在更远的地方</span></p>
  <p style="margin:0;font-size:10px;color:#7D86A5;letter-spacing:2px;"><span leaf="">THE END · EPILOGUE</span></p>
</section>
```

---

## 组件 8 蓝点小节标题

```html
<section style="margin:28px 10px 14px;padding:0;display:flex;align-items:center;box-sizing:border-box;">
  <span style="width:8px;height:8px;margin-right:10px;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span>
  <span style="font-size:15px;line-height:1.55;font-weight:700;color:#002FA7;"><span leaf="">小节标题占位</span></span>
  <span style="flex:1;height:1px;margin-left:12px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span>
</section>
```

---

## 组件 9 正文段落

基础段落：

```html
<p style="margin:0 10px 20px;font-size:16px;line-height:1.75;color:#434650;text-align:justify;letter-spacing:0.3px;"><span leaf="">正文内容占位：这里展示标准段落的字号、行距与留白关系。文字保持克制，不依赖色块，以稳定阅读为第一优先级。</span></p>
```

关键词下划线段落：

```html
<p style="margin:0 10px 20px;font-size:16px;line-height:1.75;color:#434650;text-align:justify;"><span leaf="">正文内容占位：阅读过程中需要突出的是</span><span style="border-bottom:2px solid #002FA7;color:#111111;font-weight:600;"><span leaf="">关键短语占位</span></span><span leaf="">，而不是让整段文字都变成蓝色。</span></p>
```

---

## 组件 10 行内强调样式

普通加粗：

```html
<strong style="color:#111111;"><span leaf="">普通加粗占位</span></strong>
```

蓝色锚点（全文不超过 5 处）：

```html
<strong style="color:#002FA7;"><span leaf="">蓝色锚点占位</span></strong>
```

浅蓝标签：

```html
<span style="background:#E8ECFF;color:#002FA7;padding:2px 7px;border-radius:3px;font-weight:700;"><span leaf="">核心标签占位</span></span>
```

行内代码：

```html
<code style="padding:2px 6px;background:#F3F6FF;color:#002FA7;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;"><span leaf="">inline_code</span></code>
```

---

## 组件 11 引用组件族

### 11a 深蓝金句引用

> 适合 60 个汉字以内的核心金句，每篇 1–2 次。

```html
<section style="margin:8px 10px 28px;padding:22px 20px;background:linear-gradient(135deg,#002FA7 0%,#001E78 100%);border-radius:6px;box-shadow:0 8px 24px rgba(0,47,167,0.16);box-sizing:border-box;">
  <p style="margin:0 0 12px;font-family:Georgia,'Times New Roman',serif;font-size:24px;line-height:1;color:#E8ECFF;"><span leaf="">“</span></p>
  <p style="margin:0 0 16px;font-size:16px;line-height:1.9;color:#FFFFFF;font-weight:600;"><span leaf="">引用内容占位：真正值得被看见的，不只是答案，还有答案背后的判断方式。</span></p>
  <p style="margin:0;text-align:right;font-size:11px;color:#E8ECFF;letter-spacing:1px;"><span leaf="">—— 作者或来源占位</span></p>
</section>
```

### 11b 左线长引用

```html
<section style="margin:0 10px 28px;padding:14px 0 14px 20px;border-left:3px solid #002FA7;box-sizing:border-box;">
  <p style="margin:0 0 9px;font-size:10px;color:#7D86A5;letter-spacing:2px;"><span leaf="">REFERENCE · 引用占位</span></p>
  <p style="margin:0;font-size:15px;line-height:1.9;color:#434650;text-align:justify;"><span leaf="">长引用内容占位：这里适合承载相对完整的背景说明、原始观点或材料摘录，以蓝色竖线建立层级，而不使用大面积色块。</span></p>
</section>
```

### 11c 居中金句分隔

```html
<section style="margin:32px 10px;padding:22px 18px;border-top:1px solid #D8E1F6;border-bottom:1px solid #D8E1F6;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 12px;font-size:10px;color:#002FA7;letter-spacing:2px;"><span leaf="">✦ THOUGHT ✦</span></p>
  <p style="margin:0;font-size:16px;line-height:1.9;font-weight:600;color:#002FA7;"><span leaf="">过渡金句占位：让一段思考在章节之间停留片刻。</span></p>
</section>
```

---

## 组件 12 提示卡组件族

### 12a 信息卡

```html
<section style="margin:0 10px 24px;padding:18px 20px;background:#F3F6FF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 7px;font-size:11px;color:#002FA7;font-weight:700;letter-spacing:1px;"><span leaf="">◇ 信息说明</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#434650;"><span leaf="">信息内容占位：用于补充读者理解当前段落所需的背景、定义或上下文。</span></p>
</section>
```

### 12b 重点提示

```html
<section style="margin:0 10px 24px;padding:16px 0 16px 18px;border-left:4px solid #002FA7;border-top:1px solid #E8ECFF;border-bottom:1px solid #E8ECFF;box-sizing:border-box;">
  <p style="margin:0 0 6px;font-size:11px;color:#002FA7;font-weight:700;letter-spacing:1px;"><span leaf="">✦ 重点提示</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#111111;font-weight:600;"><span leaf="">重点内容占位：这里放置需要立即被读者注意的一条原则或结论。</span></p>
</section>
```

### 12c 风险警示

```html
<section style="margin:0 10px 24px;padding:18px 20px;background:#FFFFFF;border:1px solid #002FA7;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 8px;font-size:11px;color:#002FA7;font-weight:700;letter-spacing:1px;"><span leaf="">△ 风险提醒</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#434650;"><span leaf="">风险内容占位：指出一种容易误判的情况，并说明需要额外检查的边界。</span></p>
</section>
```

### 12d 完成确认

```html
<section style="margin:0 10px 24px;padding:18px 20px;background:#E8ECFF;border-top:2px solid #002FA7;border-radius:0 0 6px 6px;box-sizing:border-box;">
  <p style="margin:0 0 8px;font-size:11px;color:#002FA7;font-weight:700;letter-spacing:1px;"><span leaf="">○ 完成确认</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#111111;"><span leaf="">确认内容占位：用于总结已经达成的阶段结果、验证条件或交付状态。</span></p>
</section>
```

---

## 组件 13 CTA 行动引导

主 CTA：

```html
<section style="margin:30px 10px;padding:26px 20px;background:#002FA7;border-radius:6px;text-align:center;box-shadow:0 8px 24px rgba(0,47,167,0.16);box-sizing:border-box;">
  <p style="margin:0 0 9px;font-size:18px;line-height:1.5;font-weight:600;color:#FFFFFF;"><span leaf="">行动标题占位：继续完成下一步阅读</span></p>
  <p style="margin:0 0 18px;font-size:13px;line-height:1.75;color:#E8ECFF;"><span leaf="">行动说明占位：用一句简短文字交代后续可获得的延伸内容。</span></p>
  <span style="display:inline-block;padding:8px 18px;background:#FFFFFF;color:#002FA7;border-radius:999px;font-size:12px;font-weight:700;"><span leaf="">按钮文案占位 →</span></span>
</section>
```

轻量 CTA：

```html
<section style="margin:0 10px 28px;padding:18px 0;border-top:1px solid #002FA7;border-bottom:1px solid #D8E1F6;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 12px;font-size:15px;line-height:1.7;font-weight:600;color:#111111;"><span leaf="">轻量引导占位：如果这部分与你有关，可以继续查看结构说明。</span></p>
  <span style="display:inline-block;padding:5px 14px;border:1px solid #B8C8F5;border-radius:999px;font-size:12px;color:#002FA7;font-weight:600;"><span leaf="">查看延伸内容</span></span>
</section>
```

---

## 组件 14 单步说明卡

```html
<section style="margin:0 10px 24px;padding:20px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:8px;box-shadow:0 6px 18px rgba(0,47,167,0.08);box-sizing:border-box;">
  <section style="display:flex;align-items:flex-start;margin:0 0 12px;">
    <span style="display:inline-block;flex:none;white-space:nowrap;margin:1px 10px 0 0;padding:3px 10px;background:#002FA7;color:#FFFFFF;border-radius:999px;font-family:Georgia,'Times New Roman',serif;font-size:11px;"><span leaf="">STEP 01</span></span>
    <span style="font-size:15px;line-height:1.6;font-weight:700;color:#002FA7;"><span leaf="">步骤标题占位</span></span>
  </section>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#434650;text-align:justify;"><span leaf="">步骤说明占位：描述这一阶段需要完成的动作、判断条件和预期结果。</span></p>
</section>
```

---

## 组件 15 三段流程总览

```html
<section style="margin:0 10px 30px;padding:22px 20px;background:#F3F6FF;border-top:1px solid #002FA7;border-bottom:1px solid #D8E1F6;box-sizing:border-box;">
  <p style="margin:0 0 16px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">PROCESS · 流程总览</span></p>
  <section style="margin:0 0 14px;padding:0 0 14px;border-bottom:1px solid #D8E1F6;display:flex;align-items:flex-start;"><span style="width:26px;margin-right:12px;font-family:Georgia,'Times New Roman',serif;font-size:18px;color:#002FA7;"><span leaf="">01</span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.7;color:#434650;"><strong style="color:#111111;"><span leaf="">流程节点占位</span></strong><span leaf="">　先确认问题边界与输入条件。</span></p></section>
  <section style="margin:0 0 14px;padding:0 0 14px;border-bottom:1px solid #D8E1F6;display:flex;align-items:flex-start;"><span style="width:26px;margin-right:12px;font-family:Georgia,'Times New Roman',serif;font-size:18px;color:#002FA7;"><span leaf="">02</span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.7;color:#434650;"><strong style="color:#111111;"><span leaf="">流程节点占位</span></strong><span leaf="">　再组织材料并形成结构草案。</span></p></section>
  <section style="margin:0;display:flex;align-items:flex-start;"><span style="width:26px;margin-right:12px;font-family:Georgia,'Times New Roman',serif;font-size:18px;color:#002FA7;"><span leaf="">03</span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.7;color:#434650;"><strong style="color:#111111;"><span leaf="">流程节点占位</span></strong><span leaf="">　最后检查结果并记录复用方式。</span></p></section>
</section>
```

---

## 组件 16 垂直时间线

```html
<section style="margin:0 10px 30px;padding:20px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 18px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">TIMELINE · 阶段脉络</span></p>
  <section style="display:flex;margin:0 0 18px;">
    <section style="width:16px;margin-right:12px;text-align:center;"><span style="display:inline-block;width:8px;height:8px;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="display:block;width:1px;height:42px;margin:3px auto 0;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span></section>
    <section style="flex:1;"><p style="margin:0 0 3px;font-size:10px;color:#002FA7;letter-spacing:1px;"><span leaf="">阶段一占位</span></p><p style="margin:0 0 4px;font-size:14px;color:#111111;font-weight:700;"><span leaf="">时间线标题占位</span></p><p style="margin:0;font-size:12px;line-height:1.65;color:#7D86A5;"><span leaf="">阶段说明占位：记录起点与初始判断。</span></p></section>
  </section>
  <section style="display:flex;margin:0 0 18px;">
    <section style="width:16px;margin-right:12px;text-align:center;"><span style="display:inline-block;width:8px;height:8px;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="display:block;width:1px;height:42px;margin:3px auto 0;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span></section>
    <section style="flex:1;"><p style="margin:0 0 3px;font-size:10px;color:#002FA7;letter-spacing:1px;"><span leaf="">阶段二占位</span></p><p style="margin:0 0 4px;font-size:14px;color:#111111;font-weight:700;"><span leaf="">时间线标题占位</span></p><p style="margin:0;font-size:12px;line-height:1.65;color:#7D86A5;"><span leaf="">阶段说明占位：记录调整与关键转折。</span></p></section>
  </section>
  <section style="display:flex;">
    <section style="width:16px;margin-right:12px;text-align:center;"><span style="display:inline-block;width:8px;height:8px;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span></section>
    <section style="flex:1;"><p style="margin:0 0 3px;font-size:10px;color:#002FA7;letter-spacing:1px;"><span leaf="">阶段三占位</span></p><p style="margin:0 0 4px;font-size:14px;color:#111111;font-weight:700;"><span leaf="">时间线标题占位</span></p><p style="margin:0;font-size:12px;line-height:1.65;color:#7D86A5;"><span leaf="">阶段说明占位：记录结论与后续方向。</span></p></section>
  </section>
</section>
```

---

## 组件 17 标准图片

```html
<figure style="margin:0 10px 28px;padding:0;box-sizing:border-box;">
  <section style="padding:4px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:4px;overflow:hidden;">
    <span leaf=""><img src="{{图片URL}}" alt="{{图片说明}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
  <figcaption style="margin:8px 10px 0;text-align:center;font-size:12px;line-height:1.6;color:#7D86A5;"><span leaf="">— 图片说明占位：用于补充画面来源与内容关系</span></figcaption>
</figure>
```

---

## 组件 18 媒体占位与对比

### 18a 图片素材占位

```html
<section style="margin:0 10px 28px;padding:32px 20px;background:#F3F6FF;border:1px dashed #B8C8F5;border-radius:8px;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-family:Georgia,'Times New Roman',serif;font-size:22px;color:#002FA7;"><span leaf="">◇</span></p>
  <p style="margin:0 0 6px;font-size:14px;color:#002FA7;font-weight:700;"><span leaf="">图片素材待补</span></p>
  <p style="margin:0;font-size:12px;line-height:1.65;color:#7D86A5;"><span leaf="">占位说明：此处插入与段落语义匹配的艺术图片或结构示意图。</span></p>
</section>
```

### 18b 双图对比

```html
<section style="margin:0 10px 30px;padding:20px;background:#FFFFFF;border-top:1px solid #002FA7;border-bottom:1px solid #D8E1F6;box-sizing:border-box;">
  <p style="margin:0 0 16px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">COMPARE · 双图对比</span></p>
  <figure style="margin:0 0 18px;padding:0;"><p style="margin:0 0 7px;font-size:11px;color:#7D86A5;"><span leaf="">对比项 A 占位</span></p><span leaf=""><img src="{{对比图A URL}}" alt="{{对比图A说明}}" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:4px;"></span></figure>
  <figure style="margin:0;padding:0;"><p style="margin:0 0 7px;font-size:11px;color:#7D86A5;"><span leaf="">对比项 B 占位</span></p><span leaf=""><img src="{{对比图B URL}}" alt="{{对比图B说明}}" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:4px;"></span></figure>
</section>
```

### 18c 静态视频占位

```html
<section style="margin:0 10px 30px;padding:38px 20px;background:linear-gradient(135deg,#002FA7,#001E78);border-radius:6px;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 12px;font-size:24px;color:#FFFFFF;line-height:1;"><span leaf="">▷</span></p>
  <p style="margin:0 0 7px;font-size:15px;color:#FFFFFF;font-weight:700;"><span leaf="">视频内容占位</span></p>
  <p style="margin:0;font-size:12px;line-height:1.65;color:#E8ECFF;"><span leaf="">静态说明占位：此处用于提示后续补充视频封面或演示片段。</span></p>
</section>
```

---

## 组件 19 代码块组件族

深色代码块：

```html
<section style="margin:0 10px 24px;background:#001E78;border-radius:6px;overflow:hidden;box-shadow:0 6px 18px rgba(0,47,167,0.12);box-sizing:border-box;">
  <section style="padding:9px 14px;background:#002FA7;display:flex;align-items:center;">
    <span style="width:8px;height:8px;margin-right:6px;background:#FFFFFF;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="width:8px;height:8px;margin-right:6px;background:#B8C8F5;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="width:8px;height:8px;margin-right:10px;background:#0648D8;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    <span style="font-family:Consolas,Monaco,monospace;font-size:11px;color:#E8ECFF;letter-spacing:1px;"><span leaf="">language</span></span>
  </section>
  <section style="padding:12px 14px;"><p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#FFFFFF;"><span leaf="">const structure = '代码内容占位';</span></p><p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E8ECFF;"><span leaf="">return structure;</span></p></section>
</section>
```

浅色代码块：

```html
<section style="margin:0 10px 28px;background:#F3F6FF;border:1px solid #D8E1F6;border-left:3px solid #002FA7;border-radius:6px;overflow:hidden;box-sizing:border-box;">
  <section style="padding:8px 14px;border-bottom:1px solid #D8E1F6;"><span style="font-family:Consolas,Monaco,monospace;font-size:11px;color:#7D86A5;letter-spacing:1px;"><span leaf="">config</span></span></section>
  <section style="padding:12px 14px;"><p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#111111;"><span leaf="">theme: 'klein-blue'</span></p><p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#002FA7;"><span leaf="">content: '配置内容占位'</span></p></section>
</section>
```

---

## 组件 20 真实数据表格

> `table` 只用于真实数据语义，不承担布局。

```html
<section style="margin:0 10px 28px;overflow-x:auto;box-sizing:border-box;">
  <p style="margin:0 0 12px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">DATA · 字段对照</span></p>
  <table style="width:100%;border-collapse:collapse;font-size:13px;line-height:1.6;">
    <thead><tr><th style="padding:9px 10px;background:#002FA7;color:#FFFFFF;text-align:left;font-weight:700;"><span leaf="">字段标题占位</span></th><th style="padding:9px 10px;background:#002FA7;color:#FFFFFF;text-align:left;font-weight:700;"><span leaf="">说明标题占位</span></th></tr></thead>
    <tbody><tr><td style="padding:9px 10px;border-bottom:1px solid #D8E1F6;color:#111111;"><span leaf="">字段内容占位</span></td><td style="padding:9px 10px;border-bottom:1px solid #D8E1F6;color:#434650;"><span leaf="">对应说明占位</span></td></tr><tr><td style="padding:9px 10px;border-bottom:1px solid #D8E1F6;background:#F3F6FF;color:#111111;"><span leaf="">字段内容占位</span></td><td style="padding:9px 10px;border-bottom:1px solid #D8E1F6;background:#F3F6FF;color:#434650;"><span leaf="">对应说明占位</span></td></tr></tbody>
  </table>
</section>
```

---

## 组件 21 指标与进度组件族

双指标卡：

```html
<section style="margin:0 10px 28px;padding:20px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <section style="display:flex;align-items:stretch;">
    <section style="flex:1;margin-right:8px;padding:18px 12px;background:#002FA7;text-align:center;border-radius:4px;"><p style="margin:0 0 6px;font-family:Georgia,'Times New Roman',serif;font-size:24px;line-height:1;color:#FFFFFF;"><span leaf="">XX%</span></p><p style="margin:0;font-size:11px;color:#E8ECFF;"><span leaf="">指标说明占位</span></p></section>
    <section style="flex:1;padding:18px 12px;background:#F3F6FF;border:1px solid #D8E1F6;text-align:center;border-radius:4px;"><p style="margin:0 0 6px;font-family:Georgia,'Times New Roman',serif;font-size:24px;line-height:1;color:#002FA7;"><span leaf="">XX</span></p><p style="margin:0;font-size:11px;color:#7D86A5;"><span leaf="">指标说明占位</span></p></section>
  </section>
</section>
```

进度条：

```html
<section style="margin:0 10px 30px;padding:20px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 16px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">PROGRESS · 比例示意</span></p>
  <p style="margin:0 0 6px;font-size:12px;color:#434650;"><span leaf="">进度项目占位 A</span></p>
  <section style="height:6px;margin:0 0 16px;background:#E8ECFF;border-radius:999px;overflow:hidden;"><span style="display:block;width:72%;height:6px;background:#002FA7;border-radius:999px;font-size:0;line-height:0;"><span leaf=""><br></span></span></section>
  <p style="margin:0 0 6px;font-size:12px;color:#434650;"><span leaf="">进度项目占位 B</span></p>
  <section style="height:6px;background:#E8ECFF;border-radius:999px;overflow:hidden;"><span style="display:block;width:48%;height:6px;background:#0648D8;border-radius:999px;font-size:0;line-height:0;"><span leaf=""><br></span></span></section>
</section>
```

---

## 组件 22 列表组件族

无序列表：

```html
<section style="margin:0 10px 28px;padding:20px;background:#F3F6FF;border-left:3px solid #002FA7;box-sizing:border-box;">
  <section style="display:flex;align-items:flex-start;margin:0 0 12px;"><span style="width:7px;height:7px;margin:7px 11px 0 0;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.75;color:#434650;"><span leaf="">无序要点占位：用于并列展示第一条结构说明。</span></p></section>
  <section style="display:flex;align-items:flex-start;margin:0 0 12px;"><span style="width:7px;height:7px;margin:7px 11px 0 0;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.75;color:#434650;"><span leaf="">无序要点占位：用于并列展示第二条结构说明。</span></p></section>
  <section style="display:flex;align-items:flex-start;"><span style="width:7px;height:7px;margin:7px 11px 0 0;background:#002FA7;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.75;color:#434650;"><span leaf="">无序要点占位：用于并列展示第三条结构说明。</span></p></section>
</section>
```

有序列表：

```html
<section style="margin:0 10px 28px;padding:0;box-sizing:border-box;">
  <section style="display:flex;align-items:flex-start;margin:0 0 14px;padding:0 0 14px;border-bottom:1px solid #E8ECFF;"><span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;margin:1px 12px 0 0;background:#002FA7;color:#FFFFFF;border-radius:50%;font-family:Georgia,'Times New Roman',serif;font-size:12px;"><span leaf="">1</span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.75;color:#434650;"><span leaf="">编号内容占位：先明确问题和输入条件。</span></p></section>
  <section style="display:flex;align-items:flex-start;margin:0 0 14px;padding:0 0 14px;border-bottom:1px solid #E8ECFF;"><span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;margin:1px 12px 0 0;background:#FFFFFF;color:#002FA7;border:1px solid #002FA7;border-radius:50%;font-family:Georgia,'Times New Roman',serif;font-size:12px;"><span leaf="">2</span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.75;color:#434650;"><span leaf="">编号内容占位：再组织材料和结构顺序。</span></p></section>
  <section style="display:flex;align-items:flex-start;"><span style="display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;margin:1px 12px 0 0;background:#FFFFFF;color:#002FA7;border:1px solid #002FA7;border-radius:50%;font-family:Georgia,'Times New Roman',serif;font-size:12px;"><span leaf="">3</span></span><p style="flex:1;margin:0;font-size:14px;line-height:1.75;color:#434650;"><span leaf="">编号内容占位：最后检查结果和复用方式。</span></p></section>
</section>
```

任务清单：

```html
<section style="margin:0 10px 30px;padding:20px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 14px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">CHECKLIST · 检查清单</span></p>
  <p style="margin:0 0 10px;font-size:14px;line-height:1.7;color:#434650;"><span style="display:inline-block;width:18px;margin-right:8px;color:#002FA7;font-weight:700;"><span leaf="">✓</span></span><span leaf="">已完成事项占位：结构层级检查</span></p>
  <p style="margin:0 0 10px;font-size:14px;line-height:1.7;color:#434650;"><span style="display:inline-block;width:18px;margin-right:8px;color:#002FA7;font-weight:700;"><span leaf="">✓</span></span><span leaf="">已完成事项占位：重点信息检查</span></p>
  <p style="margin:0;font-size:14px;line-height:1.7;color:#7D86A5;"><span style="display:inline-block;width:18px;margin-right:8px;color:#B8C8F5;font-weight:700;"><span leaf="">○</span></span><span leaf="">待完成事项占位：素材与说明补充</span></p>
</section>
```

---

## 组件 23 标签胶囊组

```html
<section style="margin:0 10px 28px;padding:20px;background:#F3F6FF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 14px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">TAGS · 标签组合</span></p>
  <p style="margin:0;line-height:2.2;">
    <span style="display:inline-block;margin:0 8px 8px 0;padding:4px 12px;background:#E8ECFF;border:1px solid #E8ECFF;border-radius:999px;font-size:12px;line-height:1.4;color:#002FA7;"><span leaf="">浅底标签</span></span>
    <span style="display:inline-block;margin:0 8px 8px 0;padding:4px 12px;background:#FFFFFF;border:1px solid #B8C8F5;border-radius:999px;font-size:12px;line-height:1.4;color:#002FA7;"><span leaf="">描边标签</span></span>
    <span style="display:inline-block;margin:0 8px 8px 0;padding:4px 12px;background:#002FA7;border:1px solid #002FA7;border-radius:999px;font-size:12px;line-height:1.4;color:#FFFFFF;"><span leaf="">实底标签</span></span>
  </p>
</section>
```

---

## 组件 24 图文推荐卡

```html
<section style="margin:0 10px 30px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:8px;overflow:hidden;box-shadow:0 6px 18px rgba(0,47,167,0.08);box-sizing:border-box;">
  <span leaf=""><img src="{{推荐图URL}}" alt="{{推荐图说明}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  <section style="padding:18px 20px;">
    <section style="display:flex;align-items:center;margin:0 0 7px;"><span style="flex:1;font-size:15px;color:#002FA7;font-weight:700;"><span leaf="">卡片标题示例占位</span></span><span style="font-size:15px;color:#002FA7;"><span leaf="">✦</span></span></section>
    <p style="margin:0 0 12px;font-size:13px;line-height:1.75;color:#434650;"><span leaf="">卡片说明占位：用于推荐相关内容、案例或进一步阅读材料。</span></p>
    <p style="margin:0;font-size:12px;color:#002FA7;font-weight:700;"><span leaf="">→ 阅读引导占位</span></p>
  </section>
</section>
```

---

## 组件 25 重点摘要卡

```html
<section style="margin:0 10px 30px;padding:24px 20px;background:#FFFFFF;border-top:3px solid #002FA7;border-right:1px solid #D8E1F6;border-bottom:1px solid #D8E1F6;border-left:1px solid #D8E1F6;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-size:10px;color:#7D86A5;letter-spacing:2px;"><span leaf="">SUMMARY · 摘要占位</span></p>
  <p style="margin:0 0 10px;font-size:18px;line-height:1.5;color:#002FA7;font-weight:600;"><span leaf="">摘要标题占位：把复杂内容压缩成一条清晰判断</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#434650;text-align:justify;"><span leaf="">摘要说明占位：这里汇总本节最重要的逻辑、证据与边界，方便读者快速回看。</span></p>
</section>
```

---

## 组件 26 常见问答

```html
<section style="margin:0 10px 30px;padding:20px 18px;background:#F3F6FF;border-top:1px solid #002FA7;box-sizing:border-box;">
  <p style="margin:0 0 16px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">FAQ · 常见问答</span></p>
  <section style="margin:0 0 16px;padding:0 0 16px;border-bottom:1px solid #D8E1F6;"><p style="margin:0 0 7px;font-size:14px;line-height:1.7;color:#111111;font-weight:700;"><span leaf="">Q　问题标题占位：这里适合回答什么？</span></p><p style="margin:0;font-size:13px;line-height:1.75;color:#434650;"><span leaf="">A　回答内容占位：用简洁段落说明判断条件、适用范围与必要限制。</span></p></section>
  <section style="margin:0;"><p style="margin:0 0 7px;font-size:14px;line-height:1.7;color:#111111;font-weight:700;"><span leaf="">Q　问题标题占位：需要注意哪些边界？</span></p><p style="margin:0;font-size:13px;line-height:1.75;color:#434650;"><span leaf="">A　回答内容占位：补充容易忽略的前提与检查方式。</span></p></section>
</section>
```

---

## 组件 27 作者信息

```html
<section style="margin:0 10px 30px;padding:22px 20px;background:#FFFFFF;border:1px solid #D8E1F6;border-radius:8px;box-shadow:0 6px 18px rgba(0,47,167,0.08);box-sizing:border-box;">
  <section style="display:flex;align-items:center;margin:0 0 14px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:42px;margin-right:13px;background:#002FA7;color:#FFFFFF;border-radius:50%;font-family:Georgia,'Times New Roman',serif;font-size:18px;"><span leaf="">A</span></span>
    <section style="flex:1;"><p style="margin:0 0 3px;font-size:15px;color:#111111;font-weight:700;"><span leaf="">作者名称占位</span></p><p style="margin:0;font-size:10px;color:#7D86A5;letter-spacing:1px;"><span leaf="">AUTHOR · 身份说明占位</span></p></section>
  </section>
  <p style="margin:0;font-size:13px;line-height:1.75;color:#434650;text-align:justify;"><span leaf="">作者简介占位：用一段克制说明介绍长期关注的内容方向与写作视角。</span></p>
</section>
```

---

## 组件 28 联系、下载与延伸阅读

联系方式：

```html
<section style="margin:0 10px 28px;padding:20px;background:#F3F6FF;border:1px solid #D8E1F6;border-radius:6px;box-sizing:border-box;">
  <p style="margin:0 0 12px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">CONTACT · 联系信息</span></p>
  <p style="margin:0 0 8px;font-size:13px;line-height:1.7;color:#434650;"><span style="display:inline-block;width:62px;color:#7D86A5;"><span leaf="">联系渠道</span></span><span leaf="">渠道内容占位</span></p>
  <p style="margin:0;font-size:13px;line-height:1.7;color:#434650;"><span style="display:inline-block;width:62px;color:#7D86A5;"><span leaf="">补充说明</span></span><span leaf="">联系说明占位</span></p>
</section>
```

下载引导：

```html
<section style="margin:0 10px 28px;padding:24px 20px;background:#002FA7;border-radius:6px;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 8px;font-size:17px;line-height:1.5;color:#FFFFFF;font-weight:600;"><span leaf="">扩展材料标题占位</span></p>
  <p style="margin:0 0 17px;font-size:12px;line-height:1.7;color:#E8ECFF;"><span leaf="">材料说明占位：用于说明可获得的静态补充文档或阅读清单。</span></p>
  <span style="display:inline-block;padding:7px 16px;background:#FFFFFF;color:#002FA7;border-radius:999px;font-size:12px;font-weight:700;"><span leaf="">获取方式占位 ↓</span></span>
</section>
```

延伸阅读：

```html
<section style="margin:0 10px 30px;padding:0;box-sizing:border-box;">
  <p style="margin:0 0 14px;font-size:11px;color:#002FA7;letter-spacing:2px;font-weight:700;"><span leaf="">FURTHER READING · 延伸阅读</span></p>
  <section style="margin:0 0 12px;padding:14px 16px;background:#FFFFFF;border:1px solid #D8E1F6;border-left:3px solid #002FA7;"><p style="margin:0 0 4px;font-size:14px;color:#111111;font-weight:700;"><span leaf="">延伸条目标题占位</span></p><p style="margin:0;font-size:12px;line-height:1.65;color:#7D86A5;"><span leaf="">条目说明占位：补充与正文相关的阅读方向。</span></p></section>
  <section style="margin:0;padding:14px 16px;background:#FFFFFF;border:1px solid #D8E1F6;border-left:3px solid #B8C8F5;"><p style="margin:0 0 4px;font-size:14px;color:#111111;font-weight:700;"><span leaf="">延伸条目标题占位</span></p><p style="margin:0;font-size:12px;line-height:1.65;color:#7D86A5;"><span leaf="">条目说明占位：提供另一种理解问题的视角。</span></p></section>
</section>
```

---

## 组件 29 装饰分隔线

星芒分隔：

```html
<section style="margin:34px 10px;display:flex;align-items:center;box-sizing:border-box;">
  <span style="font-size:12px;color:#002FA7;"><span leaf="">✦</span></span><span style="flex:1;height:1px;margin:0 12px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="font-size:10px;color:#002FA7;"><span leaf="">◆</span></span><span style="flex:1;height:1px;margin:0 12px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="font-size:12px;color:#002FA7;"><span leaf="">✦</span></span>
</section>
```

轻量菱形分隔：

```html
<section style="margin:34px 10px;display:flex;align-items:center;box-sizing:border-box;">
  <span style="flex:1;height:1px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span><span style="margin:0 12px;font-size:10px;color:#002FA7;"><span leaf="">◆</span></span><span style="flex:1;height:1px;background:#B8C8F5;font-size:0;line-height:0;"><span leaf=""><br></span></span>
</section>
```

---

## 组件 30 结尾组件族

结尾总结：

```html
<section style="margin:42px 10px 28px;padding:26px 20px;background:#F3F6FF;border-top:1px solid #002FA7;border-bottom:1px solid #D8E1F6;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-size:10px;color:#002FA7;letter-spacing:2px;"><span leaf="">FINAL NOTE · 结尾总结</span></p>
  <p style="margin:0 0 12px;font-size:20px;line-height:1.5;color:#002FA7;font-weight:600;"><span leaf="">总结标题占位：把结论交还给读者</span></p>
  <p style="margin:0;font-size:14px;line-height:1.85;color:#434650;text-align:justify;"><span leaf="">总结内容占位：回收全文的核心问题，说明仍然开放的边界，并给出一个可继续思考的方向。</span></p>
</section>
```

末尾互动：

```html
<section style="margin:0 10px 28px;padding:26px 20px;background:#002FA7;border-radius:6px;text-align:center;box-sizing:border-box;">
  <p style="margin:0 0 8px;font-size:18px;line-height:1.5;color:#FFFFFF;font-weight:600;"><span leaf="">互动引导占位：感谢读到这里</span></p>
  <p style="margin:0 0 18px;font-size:13px;line-height:1.75;color:#E8ECFF;"><span leaf="">如果这段内容带来启发，可以用点赞、在看或转发完成一次轻量回应。</span></p>
  <p style="margin:0;"><span style="display:inline-block;margin:0 4px;padding:6px 13px;background:#FFFFFF;color:#002FA7;border-radius:999px;font-size:11px;font-weight:700;"><span leaf="">点赞</span></span><span style="display:inline-block;margin:0 4px;padding:6px 13px;background:#E8ECFF;color:#002FA7;border-radius:999px;font-size:11px;font-weight:700;"><span leaf="">在看</span></span><span style="display:inline-block;margin:0 4px;padding:6px 13px;border:1px solid #FFFFFF;color:#FFFFFF;border-radius:999px;font-size:11px;font-weight:700;"><span leaf="">转发</span></span></p>
</section>
```

END 几何收束：

```html
<section style="margin:0 10px 30px;padding:28px 18px;text-align:center;border-top:1px solid #D8E1F6;border-bottom:1px solid #D8E1F6;box-sizing:border-box;">
  <p style="margin:0 0 9px;font-size:22px;line-height:1.4;color:#002FA7;font-weight:600;"><span leaf="">感谢你的阅读 ✦</span></p>
  <p style="margin:0 0 18px;font-size:12px;line-height:1.7;color:#7D86A5;"><span leaf="">结尾说明占位：愿你在深邃的蓝色中，找到属于自己的自由。</span></p>
  <p style="margin:0;font-family:Georgia,'Times New Roman',serif;font-size:10px;color:#002FA7;letter-spacing:2px;"><span leaf="">— END —</span></p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;color:#111111;font-family:'HarmonyOS Sans SC','HarmonyOS Sans','PingFang SC','Microsoft YaHei','Noto Sans CJK SC',sans-serif;line-height:1.75;letter-spacing:0.3px;overflow-x:hidden;">

  <!-- 1. 展册刊头：组件 2 -->

  <!-- 2. 内文封面：观点/访谈/随笔用组件 3；报告/盘点用组件 4；二选一 -->

  <!-- 3. 前言正文：组件 9 × N -->

  <!-- 4. 专题摘要：组件 5 -->

  <!-- 5. 目录索引：组件 6，仅在三个及以上章节时生成 -->

  <!-- 6. 第一章：组件 7，margin-top 改为 20px -->
  <!--    章内按内容装配：组件 8 小节标题 + 9 正文 + 10 行内强调 -->
  <!--    观点内容选组件 11；提示内容选组件 12；结构内容选组件 14–16、20–25 -->

  <!-- 7. 章间使用组件 29 轻量菱形分隔 -->

  <!-- 8. 第二章至倒数第二章：组件 7，margin-top 48px；章内组件按语义装配 -->

  <!-- 9. 结语章：组件 7 的 ∞ + THE END 变体 -->

  <!-- 10. 结尾总结：组件 30 结尾总结变体 -->

  <!-- 11. 可选末尾互动：组件 30 末尾互动变体，每篇最多一个 -->

  <!-- 12. END 几何收束：组件 30 固定收束 -->

</section>
```

**骨架铁律**：刊头在最前；封面组件 3/4 二选一；前言先于摘要和目录；目录在第一章之前；正文以白底为主，深蓝引用和 CTA 不连续出现；章节之间只用一种组件 29 分隔；全文只有一个结尾总结和一个 END。

---

## 视觉层级与使用配额

| 层级 | 视觉语言 | 用途 | 建议频率 |
|---|---|---|---|
| 强锚点层 | 深蓝渐变封面、深蓝引用、主 CTA | 开场、核心金句、关键行动 | 同屏最多 1 个，全文各 1–2 次 |
| 结构层 | 蓝色章节号、圆点标题、1px 细线、浅蓝底卡 | 章节、步骤、数据、目录 | 按结构使用 |
| 阅读层 | 16px 正文、黑色加粗、蓝色下划线 | 主体阅读与关键词 | 每段下划线 0–2 处 |
| 辅助层 | `#7D86A5` 元信息、图注、英文标签 | 来源、日期、说明 | 克制使用 |

- 深蓝色块不得连续出现，中间至少间隔一个白底正文组件。
- 浅蓝底只用于导读、信息卡、清单、代码和少量结构区，不把整篇正文铺成浅蓝。
- 普通加粗默认 `#111111`；`#002FA7` 蓝色加粗全文不超过 5 处。
- 阴影只给封面、核心引用、推荐卡；普通段落、列表和表格不使用阴影。
- 圆点、四角星、菱形三种装饰符号足够，不混入彩色 emoji 或其他图标体系。

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 教程 / 操作指南 | 摘要 5 + 步骤卡 14 + 流程总览 15 + 代码块 19 + 有序列表 22 | 重点提示 12b、任务清单 22、完成确认 12d |
| 盘点 / 工具清单 | 目录 6 + 标签组 23 + 图文推荐卡 24 + 无序列表 22 | 指标卡 21、延伸阅读 28、摘要卡 25 |
| 观点 / 深度分析 | 封面 3/4 + 正文 9 + 深蓝金句 11a + 居中金句 11c | 左线长引用 11b、摘要卡 25、信息卡 12a |
| 访谈 / 人物特稿 | 封面 3 + 正文 9 + 左线长引用 11b + 时间线 16 + 作者信息 27 | 深蓝金句 11a、标准图片 17、延伸阅读 28 |
| 数据复盘 / 报告 | 摘要 5 + 数据表 20 + 指标与进度 21 + 有序列表 22 | 信息卡 12a、风险警示 12c、重点摘要 25 |
| 生活 / 情感随笔 | 封面 3 + 留白正文 9 + 居中金句 11c + 标准图片 17 | 左线长引用 11b、轻量 CTA 13、星芒分隔 29 |
| 案例实战 | 封面 3/4 + 流程总览 15 + 时间线 16 + 双图对比 18b + 结尾总结 30 | 步骤卡 14、风险警示 12c、任务清单 22 |

所有文章类型共用：展册刊头 2 + 封面 3/4（二选一）+ 编号章节 7 + 正文 9 + 结尾组件 30。目录 6 仅在三个及以上章节时出现；一篇文章点缀组件种类建议不超过 4 种。

---

## Markdown → 克莱因蓝排版映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 平台文章标题；内文封面写入组件 3/4 | 观点/访谈/随笔默认组件 3，报告/盘点默认组件 4；不在正文重复两次 |
| 文章开头第一个 `> 引言` | 组件 5 专题摘要或组件 3 封面导语 | 与平台外标题错开视角 |
| `## 章节标题` | 组件 7 编号章节 | 自动编号 01/02…；结语用 ∞ + THE END |
| `### 小节标题` | 组件 8 蓝点小节标题 | 不套用章节编号 |
| 普通段落 | 组件 9 正文段落 | 16px / 1.75，白底 |
| `**加粗文字**` | 组件 10 普通黑色加粗 | 蓝色加粗只给少量锚点 |
| `==高亮文字==` | 组件 10 浅蓝标签 | 核心概念，每篇 2–5 个 |
| `<u>下划线</u>` / `++文字++` | 组件 9 蓝色下划线 | 每段 0–2 个短语 |
| 行内 `` `code` `` | 组件 10 行内代码 | 字段、命令、短配置 |
| 短 `> 引用`（不超过约 60 字） | 组件 11a 深蓝金句 | 每篇 1–2 次 |
| 长 `> 引用` | 组件 11b 左线长引用 | 背景说明、原文摘录 |
| 核心过渡金句 | 组件 11c 居中金句 | 章节间停顿 |
| `信息：` | 组件 12a 信息卡 | 补充背景、定义或上下文 |
| `提示：` / `重点：` | 组件 12b 重点提示 | 需要立即注意的原则或结论 |
| `警告：` / `注意：` | 组件 12c 风险警示 | 风险、限制、边界 |
| `完成：` / `结果：` | 组件 12d 完成确认 | 阶段结果或验证状态 |
| `行动：标题` | 组件 13 主 CTA | 后续动作明确、全文最多 1 次 |
| `轻行动：内容` | 组件 13 轻量 CTA | 弱引导，不与主 CTA 连续出现 |
| `步骤：标题` + 下一段说明 | 组件 14 单步说明卡 | 教程与案例中的独立步骤 |
| 三段流程结构 | 组件 15 流程总览 | 三个阶段或三步方法，节点保持精简 |
| `1. 2. 3.` | 组件 22 有序列表 | 普通步骤清单 |
| 日期或阶段开头的有序项 | 组件 16 时间线 | 访谈经历、案例演进 |
| `-` / `*` 无序项 | 组件 22 无序列表 | 并列要点 |
| 短语型无序项（每项不超过约 8 字） | 组件 23 标签组 | 3–8 个短标签 |
| `- [x]` / `- [ ]` | 组件 22 任务清单 | 静态展示，不生成交互控件 |
| 围栏代码块 | 组件 19 深色或浅色代码块 | 默认深色；原文或用户明确要求浅色时用浅色；每行一个段落，不用 `white-space:pre` |
| Markdown 表格 | 组件 20 真实数据表 | 只用于真实表格语义 |
| 两项核心数据 | 组件 21 双指标卡 | 数据必须来自原文，不虚构 |
| 三项同类指标 | 组件 21 三项指标条 | 适合并列指标，标签保持短句 |
| 百分比 / 完成度 | 组件 21 进度条 | 仅在原文提供真实数值时生成 |
| `![](图片)` | 组件 17 标准图片 | 保留原 URL 与 alt |
| 连续两张对照图片 | 组件 18b 双图对比 | 上下堆叠，避免复杂双栏 |
| 待补图片 / 视频 | 组件 18a / 18c | 视频仅生成静态占位 |
| 图文推荐结构 | 组件 24 图文推荐卡 | 原文有标题、说明和图片时生成 |
| `摘要：` / 重点结论组 | 组件 25 重点摘要卡 | 汇总 2–4 条核心信息 |
| `***` | 组件 29 星芒分隔 | 生活随笔、艺术评论可用 |
| `---` | 组件 29 轻量菱形分隔 | 理性文章默认使用；全文统一一种分隔形式 |
| FAQ 问答结构 | 组件 26 | 一问一答静态展开 |
| 作者介绍 | 组件 27 | 无作者资料时整块删除 |
| 联系 / 下载 / 延伸阅读 | 组件 28 | 仅在原文提供对应内容时生成 |
| 文末 | 组件 30 | 总结 → 可选互动 → END；不自动追加固定作者签名文案 |
