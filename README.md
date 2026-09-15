# LemonFumo

基于 [Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 的个人博客。

## 本地预览

```bash
hugo server
```

打开 <http://localhost:1313/>

## 写文章

```bash
hugo new content posts/文章标题.md
```

文章的 front matter 格式：

```yaml
---
title: "标题"
date: 2026-09-15
draft: false
tags: ["标签"]
categories: ["分类"]
summary: "列表页显示的摘要"
---
```

## 目录结构

```text
hugo.yaml              站点配置（站名、作者、导航、社交、外观）
content/
  posts/               文章
  about.md             关于页
  archives.md          归档页
  search.md            搜索页
static/                头像、logo 等静态资源
themes/PaperMod/       主题（已内置，未用 submodule）
.github/workflows/     自动部署到 GitHub Pages
```

## 常用配置位置

| 想改什么 | 改哪里 |
| --- | --- |
| 站名 / 描述 | `hugo.yaml` 的 `title`、`params.description` |
| 顶栏导航 | `hugo.yaml` 的 `menu.main` |
| 社交图标 | `hugo.yaml` 的 `params.socialIcons` |
| 头像 / logo | 替换 `static/` 下的文件 |
| 明暗默认主题 | `hugo.yaml` 的 `params.defaultTheme`（auto/light/dark） |
| 文章页目录 | `params.ShowToc`、`params.TocOpen` |

## 部署

推送到 `main` 分支后，GitHub Actions 自动构建并发布到 GitHub Pages。

工作流文件：`.github/workflows/hugo.yaml`
