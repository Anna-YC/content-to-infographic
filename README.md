# Content To Infographic - 使用说明

## 这是什么

一个将结构化内容（文字、知识、插件信息、产品介绍、数据对比等）转化为专业视觉海报的工具。

输入一段文字 → 输出专业信息图海报（9:16竖版）。

## 核心价值

把一段"看起来很专业但普通人懒得看"的文字内容，变成"一眼就能看懂的视觉海报"。

## 效果预览

| 样式1：深色科技风 | 样式2：渐变流体风 | 样式3：轻松学习风 |
|---|---|---|
| <img src="examples/style1-cn-preview.jpg" alt="样式1：深色科技风" width="260"> | <img src="examples/style2-cn-preview.jpg" alt="样式2：渐变流体风" width="260"> | <img src="examples/style3-cn-preview.jpg" alt="样式3：轻松学习风" width="260"> |

<details>
<summary>查看更多样式预览</summary>

| 样式4：宫崎骏风格 | 样式5：复古海报风 | 样式6：赛博霓虹风 |
|---|---|---|
| <img src="examples/style4-cn-preview.jpg" alt="样式4：宫崎骏风格" width="260"> | <img src="examples/style5-cn-preview.jpg" alt="样式5：复古海报风" width="260"> | <img src="examples/style6-cn-preview.jpg" alt="样式6：赛博霓虹风" width="260"> |

| 样式7：自然森系风 | 样式8：杂志编辑风 | 样式9：宫崎骏风格 II |
|---|---|---|
| <img src="examples/style7-cn-preview.jpg" alt="样式7：自然森系风" width="260"> | <img src="examples/style8-cn-preview.jpg" alt="样式8：杂志编辑风" width="260"> | <img src="examples/style9-cn-preview.jpg" alt="样式9：宫崎骏风格 II" width="260"> |

| 样式10：新海诚风格 | 样式11：素描风格 |
|---|---|
| <img src="examples/style10-cn-preview.jpg" alt="样式10：新海诚风格" width="260"> | <img src="examples/style11-cn-preview.jpg" alt="样式11：素描风格" width="260"> |

</details>

## 适用场景

| 场景 | 示例 |
|-----|------|
| 工具/插件介绍 | "把XX插件做成信息图" |
| 知识科普 | "做个AI知识点科普海报" |
| 数据对比 | "做个能力对比图" |
| 学习路线 | "做个AI学习路线图" |
| 方法论总结 | "把这个流程做成信息图" |

## ⚙️ 首次配置

使用前需在你的运行环境中设置环境变量：

| 环境变量 | 说明 |
|---------|------|
| `IMAGE_GEN_API_KEY` | 图片生成服务 API Key（**必填**） |
| `IMAGE_GEN_API_URL` | API 端点（可选，可替换为任意 OpenAI-compatible 图片生成接口） |
| `INFOGRAPHIC_FOOTER_BRAND` | 样式1-3默认落款品牌（可选） |

> ⚠️ 未配置 `IMAGE_GEN_API_KEY` 将无法生成图片。

示例：

```bash
export IMAGE_GEN_API_KEY="your-api-key"
export IMAGE_GEN_API_URL="https://api.openai.com/v1/images/generations"
export INFOGRAPHIC_FOOTER_BRAND="Your Community"
```

## 快速使用

### 第一步：选样式

| 样式 | 风格 | 落款 | 适合内容 |
|-----|------|-----|---------|
| 样式1 | 深色科技风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 工具/方法论/技术架构 |
| 样式2 | 渐变流体风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 趋势/创新/数据对比 |
| 样式3 | 轻松学习风 | 可自定义，如 By Your Brand ♦ YYYY.MM.DD | 知识/教程/避坑指南 |

### 第二步：把内容发给它

用户说"把这个做成信息图"，然后粘贴内容即可。

### 第三步：等它生成并返回图片

它会自动：分析内容 → 选样式 → 生成图片 → 压缩 → 返回本地图片路径。

## 进阶用法

### 直接指定样式
- "用样式1做这个" → 深色科技风
- "用样式2做这个" → 渐变流体风
- "用样式3做这个" → 轻松学习风

### 指定落款
- "用样式2，落款 Your Brand" → 样式2 + 自定义落款

也可以通过环境变量设置默认落款：

```bash
export INFOGRAPHIC_FOOTER_BRAND="Your Community"
```

样式1-3会使用 `By Your Community ♦ YYYY.MM.DD`；样式4-11默认不加落款。

## 技术细节（给开发者的）

### API配置
```
模型：gpt-image-2
示例端点：https://api.openai.com/v1/images/generations
Header：User-Agent: OpenAI/1.0
超时：300秒
尺寸：1024x1792（9:16竖版）

API Key 和实际端点由环境变量 IMAGE_GEN_API_KEY / IMAGE_GEN_API_URL 配置。如果使用代理、网关或其他 OpenAI-compatible 服务，请将 `IMAGE_GEN_API_URL` 改成对应的 `/images/generations` 端点。
```

### 核心Prompt公式
```
DENSE infographic 9:16 [背景],
[视觉风格],
[内容模块],
[高密度],
[落款]
```

### 交付方式
默认返回本地图片路径。若你的 Agent 环境支持发送附件，可直接使用该本地文件路径发送图片。

## 常见问题

**Q: 内容太长怎么办？**
A: 精简核心要点，每张图聚焦一个主题。超长内容可以分多张图。

**Q: 生成的图片文字看不清？**
A: Prompt中加高密度关键词，图片会更紧凑。

**Q: API超时了怎么办？**
A: 精简Prompt重试，超时时间已设300秒。

**Q: 用户想要不同风格怎么办？**
A: 换样式即可，三种样式覆盖大部分场景。

**Q: 提示 IMAGE_GEN_API_KEY is not set？**
A: 在你的运行环境中添加 `IMAGE_GEN_API_KEY` 环境变量。

## 样式一览

### 样式1：深色科技风
- 背景：深Navy
- 配色：橙色+白色+浅蓝
- 风格：网格、卡片阴影、monospace
- 示例：Claude插件生态、老金决策九步法

### 样式2：渐变流体风
- 背景：紫蓝渐变
- 配色：霓虹青+粉色光晕
- 风格：玻璃拟态、毛玻璃、柔光
- 示例：Multi-Agent架构图、AI趋势解读

### 样式3：轻松学习风
- 背景：白→浅黄渐变
- 配色：阳光黄+清新绿+天蓝
- 风格：手绘图标、圆角卡片、气泡提示
- 示例：AI学习路线图、知识科普
