import io, sys, codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

with codecs.open("C:/Work/Test/new-chat/index.html", "r", "utf-8") as f:
    html = f.read()

footer_start = html.index('class="footer"')
footer_tag_start = html.rfind('<', 0, footer_start)
old = html[footer_tag_start:]
end_tag = old.index('</div>') + 6

# 找到实际内容结束位置
old_footer = old[:end_tag]

new_footer = '<div class="footer" style="text-align:center;padding:20px 0 40px;">'
new_footer += '<div style="margin:16px auto;text-align:center;">'
new_footer += '<img src="mixuecodingQR.jpg" alt="QR" style="width:120px;height:120px;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.1);">'
new_footer += '<p style="margin:8px 0 0;font-size:0.85rem;color:#999;">扫码关注蜜学编程</p>'
new_footer += '</div>'
new_footer += '<p>英语启蒙小课堂 - 每天进步一点点</p></div>'

html = html.replace(old_footer, new_footer)

with codecs.open("C:/Work/Test/new-chat/index.html", "w", "utf-8") as f:
    f.write(html)
print("done")
