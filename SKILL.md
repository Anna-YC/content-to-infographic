---
name: content-to-infographic
description: 将内容（文字、知识、插件信息、产品介绍等）转化为专业视觉海报。当用户要求"把这个做成信息图"、"生成插件介绍图"、"做一个科普海报"、"做能力对比图"、"用样式1/2/3/4/5/6/7/8/9/10/11"，或讨论信息图、视觉卡片、图说生成时触发。
version: "4.2.0"
---

# Content To Infographic
**内容转信息图：将结构化内容转化为专业视觉海报**

## 一句话说明

接收任意结构化内容（插件能力、知识要点、产品介绍、数据对比等），选择最适合的视觉样式，生成专业竖版信息图。

---

## ⚙️ 首次配置（必读）

首次使用前，请在你的运行环境中设置以下环境变量（例如 Codex、Claude Code 或其他支持环境变量的 Agent 环境）：

| 环境变量 | 说明 | 示例 |
|---------|------|------|
| `IMAGE_GEN_API_KEY` | 图片生成服务 API Key | `your-api-key` |
| `IMAGE_GEN_API_URL` | API 端点（可选，可替换为任意 OpenAI-compatible 图片生成接口） | `https://api.example.com/v1/images/generations` |
| `INFOGRAPHIC_FOOTER_BRAND` | 样式1-3的默认落款品牌（可选） | `Your Community` |

> ⚠️ **未配置 `IMAGE_GEN_API_KEY` 将无法生成图片**，脚本启动时会报错并提示填写。

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
| "把这个做成信息图" | → 接收内容 → 分析结构 → **随机选备用样式4-11**，对用户**不说样式编号** |
| "用样式1" | → 深色科技风（方法论/工具） |
| "用样式2" | → 渐变流体风（趋势/创新） |
| "用样式3" | → 轻松学习风（知识/教程） |
| "用样式4" | → 宫崎骏风格（治愈系） |
| "用样式5" | → 复古海报风 |
| "用样式6" | → 赛博霓虹风 |
| "用样式7" | → 自然森系风 |
| "用样式8" | → 杂志编辑风 |
| "用样式9" | → 宫崎骏风格（备用II） |
| "用样式10" | → 新海诚风格 |
| "用样式11" | → 素描风格 |
| "生成插件介绍图" | → 样式1 + 能力+法则+避坑 |
| "做科普海报" | → 样式3 + 知识点解读 |
| "做对比图" | → 样式2 + 数据对比 |
| 直接粘贴内容（未指定样式） | → **随机选备用样式4-11其一** |

> ⚠️ **未指定样式时**：随机选择备用样式（4-11）中的一种，无落款。

---

## API 配置参考

```
模型：gpt-image-2
示例端点：https://api.openai.com/v1/images/generations
Header：User-Agent: OpenAI/1.0
超时：300秒
尺寸：1024x1792（竖版9:16）
```

> 📌 **实际端点和 Key 由用户在自己的环境中配置**。如果使用代理、网关或其他 OpenAI-compatible 服务，请将 `IMAGE_GEN_API_URL` 改成对应的 `/images/generations` 端点。

---

## 样式总览

| 样式 | 名称 | 落款 | 适用场景 |
|------|------|-----|---------|
| 1 | 深色科技风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 工具/方法论/技术架构 |
| 2 | 渐变流体风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 趋势/创新/数据对比 |
| 3 | 轻松学习风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 知识/教程/避坑指南 |
| 4 | 宫崎骏风格 | 无 | 通用/备用/治愈系 |
| 5 | 复古海报风 | 无 | 通用/备用 |
| 6 | 赛博霓虹风 | 无 | 通用/备用 |
| 7 | 自然森系风 | 无 | 通用/备用 |
| 8 | 杂志编辑风 | 无 | 通用/备用 |
| 9 | 宫崎骏风格（备用II） | 无 | 通用/备用/治愈系 |
| 10 | 新海诚风格 | 无 | 通用/备用/风景 |
| 11 | 素描风格 | 无 | 通用/备用/艺术 |

> 样式4-11为**备用样式**，无落款。用户未指定样式时，随机选用其中之一。

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
  → 随机选择备用样式之一：4、5、6、7、8、9、10、11（等概率随机）
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
未指定样式 → 随机选4/5/6/7/8/9/10/11
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
- 样式4-11：**不加落款**

### Step 4 — 调用生图 API

> ⚠️ 调用前请确保已配置 `IMAGE_GEN_API_KEY` 环境变量，否则脚本会报错并提示配置。

```python
import urllib.request, json, ssl, os

# 从环境变量读取配置
API_KEY = os.environ.get("IMAGE_GEN_API_KEY", "")
API_URL = os.environ.get(
    "IMAGE_GEN_API_URL",
    "https://api.openai.com/v1/images/generations"
)

if not API_KEY:
    raise EnvironmentError(
        "IMAGE_GEN_API_KEY is not set. "
        "请在你的运行环境中设置 IMAGE_GEN_API_KEY 环境变量。"
    )

payload = {"model": "gpt-image-2", "prompt": "<Step3的Prompt>", "size": "1024x1792", "n": 1}
data = json.dumps(payload).encode('utf-8')

req = urllib.request.Request(API_URL, data=data,
    headers={"Content-Type": "application/json",
             "Authorization": f"Bearer {API_KEY}",
             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})

ctx = ssl._create_unverified_context()
with urllib.request.urlopen(req, context=ctx, timeout=300) as resp:
    result = json.load(resp)

# 保存PNG
with open("/tmp/output.png", 'wb') as f:
    f.write(base64.b64decode(result['data'][0]['b64_json']))

# 转JPG压缩
os.system("sips -s format jpeg -s formatOptions 82 --resampleWidth 1024 /tmp/output.png --out /tmp/output.jpg")
```

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

### 通用版（样式4-11，无落款）
```
标题：[主题]
内容模块（3-6个）：根据内容类型选择
[无落款]
```

---

## 失败处理

| 问题 | 解决 |
|-----|------|
| `IMAGE_GEN_API_KEY is not set` | 在你的运行环境中添加 `IMAGE_GEN_API_KEY` 环境变量 |
| API超时（502/504） | 精简Prompt重试，超时设300秒 |
| 403 Forbidden | 确认 Key 有效，检查环境变量配置 |
| 发送或上传失败 | 优先返回本地文件路径，再由具体 Agent 环境处理附件发送 |
| 图片模糊 | 确认sips压缩比例≥82 |
| 图片包含二维码 | 从Prompt中删除所有QR码相关描述，重新生成 |
| 信息密度不够 | Prompt加：`DENSE infographic, HIGH DENSITY, every pixel counts` |

---

## 文件规范

```
保存路径：/tmp/
命名格式：
  - {主题}-style1.jpg  (样式1)
  - {主题}-style2.jpg  (样式2)
  - {主题}-style3.jpg  (样式3)
  - {主题}-style4.jpg  (样式4，宫崎骏)
  - {主题}-style5.jpg  (样式5，复古海报)
  - {主题}-style6.jpg  (样式6，赛博霓虹)
  - {主题}-style7.jpg  (样式7，自然森系)
  - {主题}-style8.jpg  (样式8，杂志编辑)
  - {主题}-style9.jpg  (样式9，宫崎骏II)
  - {主题}-style10.jpg (样式10，新海诚)
  - {主题}-style11.jpg (样式11，素描)
  - 样式4预览：/tmp/style4-ghibli-preview.png/jpg
  - 样式5预览：/tmp/style5-preview.png/jpg
  - 样式6预览：/tmp/style6-preview.png/jpg
  - 样式7预览：/tmp/style7-preview.png/jpg
  - 样式8预览：/tmp/style8-preview.png/jpg
  - 样式9预览：/tmp/style9-preview.png/jpg
  - 样式10预览：/tmp/style10-preview.png/jpg
  - 样式11预览：/tmp/style11-preview.png/jpg
```

---

## 给其他 Agent 的使用说明

### 是什么
这是一个"内容→信息图"生成工具。输入任意结构化文字内容，输出专业竖版海报图。

### 何时用
- 用户说"做个信息图"
- 用户说"把这个做成图"
- 用户说"生成一张科普海报"
- 用户说"用样式1/2/3/4/5/6/7/8/9/10/11"
- 用户粘贴了一段内容想让AI做成视觉图
- 用户未指定样式 → 随机选4-11之一

### 怎么用（最简流程）
1. 接收用户内容
2. **判断：用户是否指定了样式？**
   - 指定了 → 用指定样式
   - 未指定 → **随机选样式4/5/6/7/8/9/10/11其中之一**
3. 按模板构建Prompt（注意落款规则：样式1-3有落款，4-11无落款）
4. 调用API生成（**API Key 从环境变量 `IMAGE_GEN_API_KEY` 读取**）
5. sips压缩转JPG
6. 返回本地图片路径，或按当前 Agent 环境支持的方式发送附件

### 关键约束（必须遵守）
1. **不生成二维码**：所有图片均不生成二维码，Prompt中禁止包含QR码相关描述
2. **未指定样式**：随机选4-11，不加落款，且**不告诉用户选了哪个样式**

### 关键配置
- API Key：`IMAGE_GEN_API_KEY`（**必须配置**）
- API URL：`IMAGE_GEN_API_URL`（可选，有默认值）
- 默认落款品牌：`INFOGRAPHIC_FOOTER_BRAND`（可选，仅样式1-3使用）
- 模型：gpt-image-2
- 尺寸：1024x1792
- 超时：300秒

### 落款规则（重要）
| 样式 | 是否有落款 |
|-----|------------|
| 1、2、3 | ✅ 有（对应三个社群） |
| 4、5、6、7、8、9、10、11 | ❌ 无（备用样式） |

### 随机样式选择（Python示例）
```python
import random
# 用户未指定样式时，随机选4-11之一
backup_styles = [4, 5, 6, 7, 8, 9, 10, 11]
chosen_style = random.choice(backup_styles)
print(f"随机选择样式{chosen_style}")
```
