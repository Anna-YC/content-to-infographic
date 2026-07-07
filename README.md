# Content To Infographic - 使用说明

## 这是什么

一个将结构化内容（文字、知识、插件信息、产品介绍、数据对比等）转化为专业视觉海报的工具。

输入一段文字 → 输出专业信息图海报（9:16竖版）。

## 核心价值

把一段"看起来很专业但普通人懒得看"的文字内容，变成"一眼就能看懂的视觉海报"。

## 适用场景

| 场景 | 示例 |
|-----|------|
| 工具/插件介绍 | "把XX插件做成信息图" |
| 知识科普 | "做个AI知识点科普海报" |
| 数据对比 | "做个能力对比图" |
| 学习路线 | "做个AI学习路线图" |
| 方法论总结 | "把这个流程做成信息图" |

## ⚙️ 首次配置

使用前需在你的运行环境中配置生图服务凭证。推荐放在本机 `.env` 文件里，不要提交到仓库。

脚本会自动读取 `GPT_IMAGE_CONFIG` 指定的 `.env` 文件；未指定时读取 `~/.config/gpt-image/.env`。环境变量已存在时，以当前环境变量为准。

常用非敏感配置：

| 环境变量 | 说明 |
|---------|------|
| `GPT_IMAGE_MODEL` | 图像模型名称 |
| `GPT_IMAGE_CURL_MAX_TIME` | 请求超时秒数 |
| `GPT_IMAGE_QUALITY` | 生图质量，默认 `medium` |
| `INFOGRAPHIC_FAST_MODE` | 快速模式，适合测试和草稿 |
| `INFOGRAPHIC_IMAGE_SIZE` | 覆盖默认尺寸 |
| `INFOGRAPHIC_COMPRESS_JPG` | 是否压缩为 JPG，默认 `1` |
| `INFOGRAPHIC_FOOTER_BRAND` | 样式1-3默认落款品牌（可选） |

> ⚠️ 凭证和服务地址只放在本机配置中，不要写入公开文档或提交到仓库。

示例：

```bash
export GPT_IMAGE_MODEL="gpt-image-2"
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

### 生成配置
```
图像模型：由 GPT_IMAGE_MODEL 控制
超时：由 GPT_IMAGE_CURL_MAX_TIME 控制
尺寸：1024x1792（INFOGRAPHIC_IMAGE_SIZE）
质量：medium（GPT_IMAGE_QUALITY）
快速模式：INFOGRAPHIC_FAST_MODE=1 时默认 864x1536 + low

凭证和服务地址由本机环境变量或 `.env` 文件提供，公开仓库不保存这些配置。
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

**Q: 生成超时了怎么办？**
A: 精简Prompt重试，或把 `GPT_IMAGE_CURL_MAX_TIME` 设置为 `900`。

**Q: 生成速度太慢怎么办？**
A: 草稿和测试用 `INFOGRAPHIC_FAST_MODE=1`；正式发布图再用 `GPT_IMAGE_QUALITY=high INFOGRAPHIC_IMAGE_SIZE=1024x1792`。如果不需要 JPG，可设置 `INFOGRAPHIC_COMPRESS_JPG=0` 跳过本地压缩。

**Q: 用户想要不同风格怎么办？**
A: 换样式即可，三种样式覆盖大部分场景。

**Q: 提示缺少凭证怎么办？**
A: 在本机 `.env` 或运行环境中设置生图服务凭证，不要把凭证提交到仓库。

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
