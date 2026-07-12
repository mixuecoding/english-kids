# 英语启蒙小课堂

面向 4-8 岁儿童的英语学习网页应用。每天自动安排字母和单词学习任务，让暑假两个月轻松掌握 26 个字母 + 68 个核心单词。

**在线体验：** [mixuecoding.github.io/english-kids](https://mixuecoding.github.io/english-kids/)

## 功能

- 🔤 **自然拼读** — 26 个字母逐个学，每个字母配有示例单词和本地 MP3 发音
- 📝 **单词闪卡** — 7 大类 68 个核心单词（动物、颜色、数字、学校、食物、身体、家庭）
- 🎮 **每日测验** — 根据当天学习内容自动出题，答对奖励星星
- 📊 **进度追踪** — 26 字母 + 68 单词学习进度条，连续打卡天数统计
- 🔊 **纯音频播放** — 108 个 MP3 音频托管在 GitHub Pages，微信/安卓/iOS/桌面全兼容

## 每天自动安排

系统根据当天日期自动计算学习内容，每天学 2 个新字母 + 5 个新单词，暑假 60 天刚好学完。完成全部三个任务（字母、单词、测验）即打卡成功。

## 本地运行

```bash
python -m http.server 8080
# 打开 http://localhost:8080
```

## 技术

- 纯 HTML/CSS/JS，零依赖
- localStorage 存储学习进度
- edge-tts 生成 MP3 音频
- GitHub Pages 托管

## 音频生成

如需重新生成音频：

```bash
pip install edge-tts
python gen_mp3.py
```
