---
name: content-to-infographic
description: 将内容（文字、知识、插件信息、产品介绍等）转化为专业视觉海报。当用户要求"把这个做成信息图"、"生成插件介绍图"、"做一个科普海报"、"做能力对比图"、"用样式1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20"，或讨论信息图、视觉卡片、图说生成时触发。
---

# Content To Infographic
**内容转信息图：将结构化内容转化为专业视觉海报**

## 一句话说明

接收任意结构化内容（插件能力、知识要点、产品介绍、数据对比等），选择最适合的视觉样式，生成专业竖版信息图。

---

## ⚙️ 首次配置（必读）

首次使用前，请在运行环境中配置生图服务凭证。凭证和服务地址只放在本机配置里，不写入公开文档，也不要提交到仓库。

| 环境变量 | 说明 | 示例 |
|---------|------|------|
| `INFOGRAPHIC_FOOTER_BRAND` | 样式1-3的默认落款品牌（可选） | `Your Community` |
| `INFOGRAPHIC_FAST_MODE` | 快速模式（可选，默认已用低质量） | `1` |
| `INFOGRAPHIC_IMAGE_SIZE` | 覆盖默认尺寸（可选） | `864x1536` |
| `INFOGRAPHIC_COMPRESS_JPG` | 是否压缩为 JPG（可选） | `1` |

> ⚠️ 生成服务凭证缺失时无法生成图片。脚本会读取本机环境变量或 `.env` 文件，但公开仓库不保存这些配置。

### 本地配置文件

脚本会自动读取 `GPT_IMAGE_CONFIG` 指定的 `.env` 文件；未指定时读取 `~/.config/gpt-image/.env`（macOS/Linux）或 `%USERPROFILE%\.config\gpt-image\.env`（Windows）。环境变量已存在时，以当前环境变量为准。

> 公开发布时只提交脚本和说明，不提交 `.env`。

### Python 依赖

**推荐安装 Pillow**（跨平台图片压缩）：

```bash
pip install Pillow
```

未安装时脚本会尝试平台原生降级方案：

| 平台 | 降级方案 |
|------|---------|
| macOS | `sips` 命令（系统自带） |
| Windows | PowerShell + System.Drawing（系统自带） |
| Linux | ImageMagick `convert` 命令（需安装） |

### 自定义落款

样式1-3支持落款。落款品牌按以下优先级决定：

1. 用户在本次请求中明确指定的落款
2. 环境变量 `INFOGRAPHIC_FOOTER_BRAND`
3. 默认占位 `Your Brand`

最终落款格式建议为：`By <品牌名> ♦ YYYY.MM.DD`。样式4-11默认不加落款。

---

## 快速对照表

| 用户说... | 执行动作 |
|---------|---------|
| "把这个做成信息图" | → 接收内容 → 分析结构 → **随机选备用样式4-20**，对用户**不说样式编号** |
| "用样式1" | → 深色科技风（方法论/工具） |
| "用样式2" | → 渐变流体风（趋势/创新） |
| "用样式3" | → 轻松学习风（知识/教程） |
| "用样式4" | → 宫崎骏风格（治愈系） |
| "用样式5" | → 复古海报风 |
| "用样式6" | → 赛博霓虹风 |
| "用样式7" | → 自然森系风 |
| "用样式8" | → 杂志编辑风 |
| "用样式9" | → 蛋仔风格（可爱） |
| "用样式10" | → 新海诚风格 |
| "用样式11" | → 素描风格 |
| "用样式12" | → 极简商务风 |
| "用样式13" | → 水墨国风 |
| "用样式14" | → 像素游戏风 |
| "用样式15" | → 波普艺术风 |
| "用样式16" | → 科幻太空风 |
| "用样式17" | → 蒸汽朋克风 |
| "用样式18" | → 孟菲斯设计风 |
| "用样式19" | → 日式浮世绘风 |
| "用样式20" | → 3D等距风 |
| "生成插件介绍图" | → 样式1 + 能力+法则+避坑 |
| "做科普海报" | → 样式3 + 知识点解读 |
| "做对比图" | → 样式2 + 数据对比 |
| 直接粘贴内容（未指定样式） | → **随机选备用样式4-20其一** |

> ⚠️ **未指定样式时**：随机选择备用样式（4-20）中的一种，无落款。

---

## 生成配置参考

```
模型：gpt-image-2
默认质量：low（最快，约 80-90 秒）
高质量模式：设置 GPT_IMAGE_QUALITY=medium 或 high（用户明确要求高质量时使用）
超时：由 GPT_IMAGE_CURL_MAX_TIME 控制（默认 900 秒）
尺寸：1024x1792（竖版9:16）
跨平台：
  - Pillow 压缩 → macOS / Linux / Windows 全平台支持（推荐）
  - sips 降级 → macOS 系统自带
  - PowerShell 降级 → Windows 系统自带
  - ImageMagick 降级 → Linux（需自行安装）
```

> 📌 使用者只需要运行 `scripts/generate_infographic.py`。服务地址和凭证由本机环境负责，不写入公开文档。

---

## 样式总览

| 样式 | 名称 | 落款 | 适用场景 |
|------|------|-----|---------|
| 1 | 深色科技风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 工具/方法论/技术架构 |
| 2 | 渐变流体风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 趋势/创新/数据对比 |
| 3 | 轻松学习风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 知识/教程/避坑指南 |
| 4 | 宫崎骏风格 | 无 | 通用/备用/治愈系 |
| 5 | 复古海报风 | 无 | 通用/备用/怀旧 |
| 6 | 赛博霓虹风 | 无 | 通用/备用/未来感 |
| 7 | 自然森系风 | 无 | 通用/备用/环保 |
| 8 | 杂志编辑风 | 无 | 通用/备用/高端 |
| 9 | 蛋仔风格 | 无 | 通用/备用/可爱 |
| 10 | 新海诚风格 | 无 | 通用/备用/风景 |
| 11 | 素描风格 | 无 | 通用/备用/艺术 |
| 12 | 极简商务风 | 无 | 通用/备用/商务 |
| 13 | 水墨国风 | 无 | 通用/备用/国潮 |
| 14 | 像素游戏风 | 无 | 通用/备用/怀旧游戏 |
| 15 | 波普艺术风 | 无 | 通用/备用/潮流 |
| 16 | 科幻太空风 | 无 | 通用/备用/科幻 |
| 17 | 蒸汽朋克风 | 无 | 通用/备用/机械 |
| 18 | 孟菲斯设计风 | 无 | 通用/备用/创意 |
| 19 | 日式浮世绘风 | 无 | 通用/备用/和风 |
| 20 | 3D等距风 | 无 | 通用/备用/立体 |

> 样式4-20为**备用样式**，无落款。用户未指定样式时，随机选用其中之一。

---

## 样式1：深色科技风（硬核方法论）

**适用场景：** AI工具/插件/方法论/技术架构
**落款：** 可自定义，如 By Your Brand ♦ YYYY.MM.DD
**配色：** 深Navy底 + 橙色Anthropic色 + 白色
**风格：** 网格背景、卡片阴影、代码monospace、橙色高亮分隔线

```
Prompt关键词：
Dark tech infographic, deep navy background, Anthropic orange highlight,
grid line, card shadows, monospace code style, orange accent lines,
DENSE infographic, HIGH DENSITY sections, minimal whitespace
```

---

## 样式2：渐变流体风（潮流创新）

**适用场景：** AI趋势/新技术/创新主题/年轻化内容
**落款：** 可自定义，如 By Your Brand ♦ YYYY.MM.DD
**配色：** 紫蓝渐变（#1a0533→#0a1628）+ 霓虹青+粉色光晕
**风格：** 玻璃拟态卡片、毛玻璃效果、柔光光晕、流体有机形状

```
Prompt关键词：
Modern infographic, deep purple-to-blue gradient, glassmorphism cards,
neon cyan+pink glow, fluid organic shapes, gradient text, soft light orbs,
futuristic dreamy aesthetic, DENSE infographic, HIGH DENSITY sections
```

---

## 样式3：轻松学习风（知识教程）

**适用场景：** AI知识点/学习路线/教程步骤/避坑指南/干货总结
**落款：** 可自定义，如 By Your Brand ♦ YYYY.MM.DD
**配色：** 白→浅黄渐变（#FFFFFF→#FFF9C4）+ 阳光黄+清新绿+天蓝
**风格：** 手绘插画风图标、圆角卡片、气泡对话框、页边涂鸦装饰

```
Prompt关键词：
Light fresh infographic, white to light yellow gradient, hand-drawn style icons,
rounded corner cards, playful doodles, speech bubbles with tips,
bright cheerful colors, educational friendly, DENSE infographic, HIGH DENSITY sections
```

---

## 备用样式（无落款，随机选用）

### 样式4：宫崎骏风格

**适用场景：** 通用备用，适合治愈系内容/自然主题/温柔科普
**落款：** 无
**配色：** 翠绿#2E7D32 + 暖黄#FDD835 + 柔蓝#4FC3F7
**风格：** 吉卜力美学，水彩手绘背景，自然风景，梦幻温柔氛围，柔和暖色，自然主题，手绘风格

```
Prompt关键词：
GHIBLI style infographic, hand-painted watercolor backgrounds,
lush green+warm yellow+soft blue, Miyazaki anime aesthetic,
soft watercolor textures, natural landscapes, pastoral scenery,
dreamy gentle atmosphere, gentle warm colors, nature themes, hand-drawn style
```

---

### 样式5：复古海报风

**适用场景：** 通用备用，适合历史时间线/经典主题/怀旧内容
**落款：** 无
**配色：** 奶油底（带纸纹）+ 烧橙#D84315 + 墨绿#2E7D32 + 藏青#0D47A1
**风格：** 复古海报美学，粗衬线体标题，装饰边框+角落装饰，温暖怀旧感

```
Prompt关键词：
VINTAGE poster infographic, warm cream background with paper texture,
burnt orange + forest green + navy, retro typography slab-serif bold,
decorative borders, corner ornaments, vintage illustration style icons,
warm nostalgic classic poster aesthetic
```

---

### 样式6：赛博霓虹风

**适用场景：** 通用备用，适合未来主题/科技趋势/酷炫内容
**落款：** 无
**配色：** 纯黑底 + 霓虹青#00FFFF + 品红#FF00FF + 黄#FFFF00
**风格：** 赛博朋克美学，发光网格地板，霓虹招牌风格文字，黑暗环境+霓虹边框，故障效果点缀，高对比度

```
Prompt关键词：
CYBERPUNK neon infographic, deep black background,
neon glow cyan+magenta+yellow, glowing grid lines on floor,
neon sign style text with glow effect, dark sections with neon borders,
futuristic tech aesthetic, glitch effect accents, high contrast
```

---

### 样式7：自然森系风

**适用场景：** 通用备用，适合可持续发展/自然主题/温和内容
**落款：** 无
**配色：** 鼠尾草绿→暖米色渐变 + 森林绿#2E7D32 + 暖棕#795548 + 天蓝#4FC3F7
**风格：** 自然大地美学，有机形状，叶片藤蔓装饰，手绘植物插画，自然纹理背景，柔和温暖，有机排版

```
Prompt关键词：
NATURE earthy infographic, soft sage green to warm beige gradient,
forest green + warm brown + sky blue, organic shapes,
leaf and vine decorations, hand-drawn botanical illustrations,
natural texture background, calm eco-friendly aesthetic,
rounded organic typography, gentle and warm
```

---

### 样式8：杂志编辑风

**适用场景：** 通用备用，适合深度文章/观点输出/高端内容/信息密集型
**落款：** 无
**配色：** 暖白/米白底 + 深棕#3E2723 + 金色#D4A017 + 深酒红#6D4C41
**风格：** 高端杂志美学，大标题衬线体，顶部导航标签栏，左右分栏布局（左侧主内容引言+编号模块列表，右侧深色侧边栏要点），装饰性线描图标，引用金句区（带署名），金色分隔线点缀，精致考究，信息密度高

```
Prompt关键词：
EDITORIAL magazine infographic 9:16, warm cream off-white background,
dark brown + gold + burgundy, large serif title typography,
top navigation tab bar with labels,
left-right two-column layout: left main content with intro+numbered sections,
right dark sidebar panel with key bullet points,
decorative line-art icons, pull quote callouts with attribution,
thin gold divider lines, sophisticated New Yorker style,
high information density, professional editorial layout
```

---

### 样式9：蛋仔风格

**适用场景：** 通用备用，适合年轻化内容/可爱主题/轻松科普/游戏相关
**落款：** 无
**配色：** 粉#FF69B4 + 薄荷绿#98FF98 + 天蓝#00BFFF + 阳光黄#FFD700
**风格：** 蛋仔派对美学，可爱圆润蛋仔角色，明亮粉彩，圆润形状，Q萌美学，粗轮廓线，快乐氛围，卡通风格

```
Prompt关键词：
CUTE chubby egg character style infographic, bright pastel colors,
pink+mint green+sky blue+sunshine yellow, round soft shapes,
cute egg characters with faces, playful fun aesthetic,
cartoon style, thick outlines, kawaii egg mascot characters,
soft rounded typography, happy cheerful vibe, Eggy Party game art style
```

---

### 样式10：新海诚风格

**适用场景：** 通用备用，适合风景主题/电影感内容/浪漫科普
**落款：** 无
**配色：** 深蔚蓝#0D47A1 + 金橙夕阳#FF8F00 + 翠绿#2E7D32
**风格：** 新海诚美学，明亮蓝天+详细白云，电影级光影，详细云层形态，《你的名字》美学，灯光十字星效果，鲜艳饱和度，戏剧性天空，风景动漫背景风格

```
Prompt关键词：
SHINKAI Makoto style infographic, bright blue sky with detailed white clouds,
deep azure + golden sunset orange + vibrant green,
realistic anime landscape, cinematic lighting, detailed cloud formations,
Your Name movie aesthetic, cross-star effect on lights,
vivid saturation, dramatic sky, scenic anime background style
```

---

### 样式11：素描风格

**适用场景：** 通用备用，适合艺术主题/手绘感内容/简约科普
**落款：** 无
**配色：** 黑白（铅笔灰阶）
**风格：** 铅笔素描美学，白纸纹理背景，写实铅笔阴影，手绘素描线条，交叉排线阴影技法，单色教育图表风格，艺术素描美学，铅笔笔触纹理，无色彩纯素描绘画风格

```
Prompt关键词：
PENCIL sketch infographic, black and white pencil drawing style,
white paper texture background, realistic pencil shading,
hand-drawn sketch lines, cross-hatching shading technique,
monochrome educational diagram style, artistic sketch aesthetic,
pencil stroke textures, no color pure sketch drawing style
```

---

### 样式12：极简商务风

**适用场景：** 通用备用，适合商务汇报/企业培训/管理方法论/产品Roadmap
**落款：** 无
**配色：** 白底#FFFFFF + 深灰#333333 + 蓝灰#607D8B + 点缀金#C9A84C
**风格：** 极简主义美学，大量留白，细线分隔，几何图标，无衬线体排版，瑞士设计感，优雅克制，高端商务调性

```
Prompt关键词：
MINIMALIST business infographic, white background with generous whitespace,
dark gray + slate blue + gold accent, geometric line icons,
clean sans-serif typography, thin dividing lines,
Swiss design aesthetic, elegant restrained layout,
professional corporate style, high-end minimalism
```

---
### 样式13：水墨国风

**适用场景：** 通用备用，适合传统文化/国学内容/东方美学/中式品牌
**落款：** 无
**配色：** 米白宣纸底#F5F0E8 + 墨黑#1A1A1A + 朱砂红#C41E3A + 淡青#7BA7BC
**风格：** 中国传统水墨画美学，宣纸纹理背景，毛笔笔触，墨色浓淡层次，朱砂印章点缀，竖排文字选项，留白意境，山水云雾元素

```
Prompt关键词：
CHINESE ink wash painting infographic, rice paper texture background,
black ink + vermillion red + pale celadon, brush stroke calligraphy,
ink gradients light to dark, red seal stamp accents,
mountain mist cloud elements, traditional Chinese aesthetic,
elegant negative space, scholarly refined atmosphere
```

---
### 样式14：像素游戏风

**适用场景：** 通用备用，适合游戏主题/编程入门/童年回忆/复古科技
**落款：** 无
**配色：** 像素色盘：亮绿#00FF00 + 品红#FF00FF + 青#00FFFF + 黄#FFFF00（8-bit 调色板）
**风格：** 复古像素艺术美学，8-bit/16-bit游戏风格，锯齿边缘，像素字体，方块状UI元素，NES/红白机时代感，高饱和原色，点阵图案边框

```
Prompt关键词：
PIXEL ART retro game infographic, 8-bit 16-bit video game style,
blocky pixel typography, pixelated borders and icons,
bright saturated primary colors, NES retro gaming aesthetic,
jagged pixel edges, sprite-style decorations,
arcade game UI elements, nostalgic gaming vibe
```

---
### 样式15：波普艺术风

**适用场景：** 通用备用，适合潮流文化/品牌营销/创意内容/社交媒体
**落款：** 无
**配色：** 鲜艳原色碰撞：亮红#FF0000 + 黄#FFD700 + 宝蓝#1E3A8A + 白#FFFFFF
**风格：** 波普艺术美学（Andy Warhol风格），大胆配色，半色调网点纹理，粗黑描边，重复图案，漫画风格对话框，丝网印刷质感，高对比高冲击

```
Prompt关键词：
POP ART infographic, bold vibrant color blocks,
halftone dot patterns, thick black outlines, comic book style speech bubbles,
Andy Warhol aesthetic, screen print texture,
repeating graphic patterns, high contrast high impact,
playful bold pop culture vibe, Ben-Day dots effect
```

---
### 样式16：科幻太空风

**适用场景：** 通用备用，适合未来科技/太空探索/科幻内容/前沿趋势
**落款：** 无
**配色：** 深邃太空黑#0A0A0F + 星云紫#6B2FA0 + 恒星金#FFD700 + 科技蓝#00BFFF
**风格：** 太空科幻美学，星云背景，星轨线条，发光文字，全息投影感，行星/轨道元素，深邃宇宙氛围，科技面板边框

```
Prompt关键词：
SCI-FI space infographic, deep cosmic space background,
nebula purple + star gold + tech blue, holographic UI elements,
star trails and orbital rings, glowing neon text on dark,
planet and constellation motifs, futuristic spacecraft dashboard,
deep universe atmosphere, cosmic wonder aesthetic
```

---
### 样式17：蒸汽朋克风

**适用场景：** 通用备用，适合机械主题/工业历史/手工匠人/复古科技
**落款：** 无
**配色：** 铜锈棕#8B6914 + 黄铜金#C5A44E + 深棕#3E2723 + 羊皮纸#F5DEB3
**风格：** 蒸汽朋克美学，齿轮和机械元素，维多利亚时代装饰，黄铜和铜材质纹理，皮革背景，怀表/飞艇/齿轮图标，复古排版，金属铆钉边框

```
Prompt关键词：
STEAMPUNK infographic, brass and copper mechanical aesthetic,
gears cogs clockwork elements, Victorian-era ornate decorations,
warm brown leather + brass gold + copper tones,
parchment paper texture background, riveted metal borders,
retro industrial revolution vibe, mechanical gear icons
```

---
### 样式18：孟菲斯设计风

**适用场景：** 通用备用，适合创意设计/艺术内容/品牌故事/年轻化营销
**落款：** 无
**配色：** 粉#FF6B6B + 薄荷绿#4ECDC4 + 黄#FFE66D + 紫#6C5CE7 + 白底（孟菲斯标志性配色）
**风格：** 孟菲斯设计美学（80年代意大利后现代），几何色块拼贴，波浪线和锯齿线，波点图案，大胆撞色，非对称布局，趣味涂鸦感，反叛传统设计的活泼感

```
Prompt关键词：
MEMPHIS design infographic, geometric color blocks collage,
squiggly lines and zigzag patterns, polka dot textures,
bold clashing colors pink+mint+yellow+purple on white,
asymmetric playful layout, 80s postmodern Italian design,
abstract geometric shapes, fun creative rebellious aesthetic
```

---
### 样式19：日式浮世绘风

**适用场景：** 通用备用，适合日本文化/旅行主题/东方美学/艺术内容
**落款：** 无
**配色：** 靛蓝#1B2A4A + 朱红#D64045 + 金黄#E8A838 + 米白#F2E8D5
**风格：** 浮世绘美学，木版画纹理，渐变色彩（bokashi技法），海浪和富士山元素，和风图案边框，竖排日文装饰，和纸纹理背景

```
Prompt关键词：
UKIYO-E Japanese woodblock print infographic,
indigo blue + vermillion red + golden yellow + cream,
woodblock texture effect, Hokusai wave motifs,
bokashi color gradation, traditional Japanese patterns border,
washi paper texture background, Edo period aesthetic,
elegant oriental artistic atmosphere
```

---
### 样式20：3D等距风

**适用场景：** 通用备用，适合数据可视化/产品展示/流程说明/技术图解
**落款：** 无
**配色：** 柔和渐变底 + 珊瑚橙#FF6F61 + 湖水蓝#5B9BD5 + 草绿#70AD47 + 暖灰#D9D9D9
**风格：** 3D等距插画美学，等角投影视角，立体几何建筑块，柔和光照和阴影，圆润边角3D元素，漂浮小岛式布局，现代扁平3D风格，C4D质感

```
Prompt关键词：
ISOMETRIC 3D infographic, 3D isometric illustration style,
soft lighting with gentle shadows, rounded 3D geometric blocks,
floating platform island layout, C4D-style rendering,
coral orange + teal blue + grass green palette,
modern flat 3D aesthetic, clean volumetric design
```

---

## 核心工作流程

### Step 1 — 接收内容，分析结构

识别内容类型：
- 有"能力/功能"列表 → 能力区必选
- 有"法则/规则" → 法则区必选
- 有"注意事项/陷阱" → 避坑区必选
- 有"数据/对比" → 数据区必选
- 无特定结构 → 提炼3-5要点

### Step 2 — 选择样式

```
情况A：用户明确指定样式（"用样式X"）
  → 使用指定样式
  → 按该样式的落款规则处理

情况B：用户未指定样式
  → 随机选择备用样式之一：4、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20（等概率随机）
  → 不添加落款
  → **不告诉用户选了哪个样式**，只说"重新制作 ✅"或"已生成 ✅"
```

**推荐映射（供参考，非强制）：**
```
内容类型 → 推荐样式
─────────────────────────
AI工具/插件/方法论 → 样式1
AI趋势/新技术/创新 → 样式2
AI知识点/教程/避坑 → 样式3
未指定样式 → 随机选4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20
```

### Step 3 — 构建 Prompt

**公式：**
```
DENSE infographic [比例] [背景描述],
[视觉风格关键词],
[内容模块详细描述],
[高密度要求],
[落款（仅样式1-3）]
```

**比例：** `9:16`（竖版）

**高密度必加：** `DENSE infographic, HIGH DENSITY sections, minimal whitespace, every pixel counts`

**落款规则：**
- 样式1-3：可加自定义落款（如 `Corner small: 'By Your Brand ♦ 2026.05.25'`）。若用户未指定，优先使用环境变量 `INFOGRAPHIC_FOOTER_BRAND`；未设置时使用 `Your Brand` 占位。
- 样式4-20：**不加落款**

### Step 4 — 调用生图脚本

> ⚠️ 调用前请确保本机已配置生图服务凭证。直接运行脚本即可，不要把凭证或服务地址写进 prompt、文档或仓库。

```bash
# macOS / Linux
python3 scripts/generate_infographic.py "<Step3的Prompt>" /tmp/output.png

# Windows (PowerShell)
python scripts/generate_infographic.py "<Step3的Prompt>" C:\temp\output.png

# Windows (CMD)
python scripts/generate_infographic.py "<Step3的Prompt>" C:\temp\output.png
```

脚本内部逻辑（无需手动实现）：
1. 读取本机配置文件或运行环境变量
2. 调用已配置的生图服务
3. 保存 PNG
4. 按配置压缩为 JPG

### Step 5 — 交付图片

```
返回本地图片路径，例如：/tmp/output.jpg
如果你的 Agent 环境支持发送图片，可直接使用该本地文件路径作为附件。
```

---

## 关键约束

- **不生成二维码**：所有图片均不生成二维码，Prompt中禁止包含任何QR码相关内容

## 版式模板（按内容类型选用）

### 能力+法则+避坑 综合版（样式1）
```
标题：[插件/工具名] 核心能力图鉴
副标题：[一句话定位]
核心能力（4-6个）：图标+关键词
黄金法则（3条）：编号列表
避坑指南（2-3条）：警告图标
落款：By Your Brand ♦ YYYY.MM.DD
```

### 趋势/数据 高密度版（样式2）
```
标题：[主题]
副标题：[引发思考]
高亮玻璃卡：必看理由
数据模块：七大/五大模块
对比表格：数据对比
落款：By Your Brand ♦ YYYY.MM.DD
```

### 知识点 轻松学习版（样式3）
```
标题：[主题]
气泡提示：核心概念
模块区：基础/进阶/实战/持续学习
避坑指南：警告图标
落款：By Your Brand ♦ YYYY.MM.DD
```

### 通用版（样式4-20，无落款）
```
标题：[主题]
内容模块（3-6个）：根据内容类型选择
[无落款]
```

---

## 失败处理

| 问题 | 解决 |
| 提示缺少凭证 | 在本机 `.env` 或运行环境中设置生图服务凭证 |
| `gpt-image` 命令找不到 | 安装 CLI 工具，或设置 `INFOGRAPHIC_IMAGE_COMMAND` / `GPT_IMAGE_BIN` 环境变量指定路径<br>Windows 还会查找 `%USERPROFILE%\bin\gpt-image.exe` 和 `%USERPROFILE%\AppData\Local\gpt-image\gpt-image.exe` |
| Pillow 未安装 | 运行 `pip install Pillow`；未安装时脚本会自动使用平台降级方案（macOS sips / Windows PowerShell / Linux ImageMagick） |
| 生成超时 | 精简 Prompt，或设置 `GPT_IMAGE_CURL_MAX_TIME` 提高超时上限（默认 900s） |
| 命令执行失败（exit code ≠ 0） | 检查生图服务是否正常运行，查看 stdout/stderr 输出定位原因 |
| 生成速度慢 | 默认已用 low 质量（约 80s）；用户明确要求高质量时设 `GPT_IMAGE_QUALITY=medium` 或 `high` |
| 发送或上传失败 | 优先返回本地文件路径，再由具体 Agent 环境处理附件发送 |
| 图片模糊 | 确认 JPG 压缩质量≥82 |
| 图片包含二维码 | 从Prompt中删除所有QR码相关描述，重新生成 |
| 信息密度不够 | Prompt加：`DENSE infographic, HIGH DENSITY, every pixel counts` |
| JPG 压缩失败 | 推荐安装 Pillow：`pip install Pillow`（全平台可用）<br>未安装时：macOS 用 sips ✓ / Windows 用 PowerShell ✓ / Linux 需 ImageMagick (`apt install imagemagick` 或 `brew install imagemagick`) |

---

## 文件规范

```
保存路径：
  macOS / Linux：/tmp/
  Windows：%TEMP% 或当前目录
命名格式：
  - {主题}-style1.jpg  (样式1)
  - {主题}-style2.jpg  (样式2)
  - {主题}-style3.jpg  (样式3)
  - {主题}-style4.jpg  (样式4，宫崎骏)
  - {主题}-style5.jpg  (样式5，复古海报)
  - {主题}-style6.jpg  (样式6，赛博霓虹)
  - {主题}-style7.jpg  (样式7，自然森系)
  - {主题}-style8.jpg  (样式8，杂志编辑)
  - {主题}-style9.jpg  (样式9，蛋仔)
  - {主题}-style10.jpg (样式10，新海诚)
  - {主题}-style11.jpg (样式11，素描)
  - {主题}-style12.jpg (样式12，极简商务)
  - {主题}-style13.jpg (样式13，水墨国风)
  - {主题}-style14.jpg (样式14，像素游戏)
  - {主题}-style15.jpg (样式15，波普艺术)
  - {主题}-style16.jpg (样式16，科幻太空)
  - {主题}-style17.jpg (样式17，蒸汽朋克)
  - {主题}-style18.jpg (样式18，孟菲斯)
  - {主题}-style19.jpg (样式19，浮世绘)
  - {主题}-style20.jpg (样式20，3D等距)
  - 样式4预览：/tmp/style4-ghibli-preview.png/jpg
  - 样式5预览：/tmp/style5-preview.png/jpg
  - 样式6预览：/tmp/style6-preview.png/jpg
  - 样式7预览：/tmp/style7-preview.png/jpg
  - 样式8预览：/tmp/style8-preview.png/jpg
  - 样式9预览：/tmp/style9-preview.png/jpg
  - 样式10预览：/tmp/style10-preview.png/jpg
  - 样式11预览：/tmp/style11-preview.png/jpg
  - 样式12预览：/tmp/style12-preview.png/jpg
  - 样式13预览：/tmp/style13-preview.png/jpg
  - 样式14预览：/tmp/style14-preview.png/jpg
  - 样式15预览：/tmp/style15-preview.png/jpg
  - 样式16预览：/tmp/style16-preview.png/jpg
  - 样式17预览：/tmp/style17-preview.png/jpg
  - 样式18预览：/tmp/style18-preview.png/jpg
  - 样式19预览：/tmp/style19-preview.png/jpg
  - 样式20预览：/tmp/style20-preview.png/jpg
```

---

## 给其他 Agent 的使用说明

### 是什么
这是一个"内容→信息图"生成工具。输入任意结构化文字内容，输出专业竖版海报图。

### 何时用
- 用户说"做个信息图"
- 用户说"把这个做成图"
- 用户说"生成一张科普海报"
- 用户说"用样式1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20"
- 用户粘贴了一段内容想让AI做成视觉图
- 用户未指定样式 → 随机选4-20之一

### 怎么用（最简流程）
1. 接收用户内容
2. **判断：用户是否指定了样式？**
   - 指定了 → 用指定样式
   - 未指定 → **随机选样式4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20其中之一**
3. 按模板构建Prompt（注意落款规则：样式1-3有落款，4-11无落款）
4. **直接运行脚本**：
   ```bash
   # macOS / Linux
   python3 scripts/generate_infographic.py "<prompt>" /tmp/output.png

   # Windows
   python scripts/generate_infographic.py "<prompt>" %TEMP%\output.png
   ```
5. 脚本自动完成 JPG 压缩（Pillow 跨平台 → 平台原生降级方案）
6. 返回本地图片路径，或按当前 Agent 环境支持的方式发送附件

### 关键约束（必须遵守）
1. **不生成二维码**：所有图片均不生成二维码，Prompt中禁止包含QR码相关描述
2. **未指定样式**：随机选4-11，不加落款，且**不告诉用户选了哪个样式**
3. **不在公开内容写入凭证或服务地址**：这些只放在本机配置中

### 关键配置
- 默认落款品牌：`INFOGRAPHIC_FOOTER_BRAND`（可选，仅样式1-3使用）
- 模型：gpt-image-2
- 尺寸：1024x1792
- 默认质量：`low`（最快，约 80s）
- 高质量模式：`GPT_IMAGE_QUALITY=medium`（约 170s）或 `high`（更慢，精细度高）
- 快速模式：`INFOGRAPHIC_FAST_MODE=1`（兼容保留，效果等同于默认 low）

### 落款规则（重要）
| 样式 | 是否有落款 |
|-----|------------|
| 1、2、3 | ✅ 有（对应三个社群） |
| 4、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20 | ❌ 无（备用样式） |

### 随机样式选择（Python示例）
```python
import random
# 用户未指定样式时，随机选4-11之一
backup_styles = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
chosen_style = random.choice(backup_styles)
print(f"随机选择样式{chosen_style}")
```
