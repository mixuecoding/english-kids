@echo off
cd /d "C:\Users\Administrator\Documents\Codex\2026-07-12\new-chat"
echo 🌟 英语启蒙小课堂服务器启动中...
echo.
echo 📱 在微信中打开：http://192.168.0.103:8888
echo.
echo ⚠️ 关闭此窗口将停止服务
echo.
python -m http.server 8888
pause
