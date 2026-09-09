# Taryn / Portfolio

从一个真实问题，到一个可用的 AI 作品。

访问地址：https://iamnottaryn.github.io/taryn-portfolio/

## 内容

- 个人项目：AI 产品思考陪练、JD 翻译官
- 实习 Demo：体验课游戏化首页、个性化复习、超市场景单词认读、AI 抠图工具
- 自用 Skill：Product Thinking 简介和使用案例
- 联系邮箱

## 如何修改

`site/index.html` 是网站的唯一主文件，包含样式和弹窗交互，可直接用浏览器打开。网站不需要安装依赖或运行构建。

修改后运行 `python3 scripts/check_site.py`，更新 CHANGELOG.md，然后创建一个说明清楚的 Git 提交并推送到 main。GitHub Actions 会自动发布到 GitHub Pages。每次发布状态可在 Actions 和 Deployments 中查看。

## 如何回滚

优先使用 `git revert <需要撤销的提交>`，然后推送到 main。网页会自动重新发布，原有历史仍会保留。不要使用强制推送或清空提交历史。

版本标签 `v1.0.0` 标记首次公开初稿。

## 当前版本限制

已包含产品思考陪练的真实截图。其余五件作品的真实截图，以及抠图前后对比图片尚待补充，页面中已明确标注。所有项目入口均已填写，但目标项目的可用性取决于各自托管服务。
