import tkinter as tk
from tkinter import messagebox
# 下载模块
import down

top = tk.Tk()
top.title('音乐下载器-美论有版权音乐网5ubq.com')

down_path = tk.StringVar(top)

info = lambda msg : messagebox.showinfo('小提示-美论有版权音乐网5ubq.com', msg)

def downMusic():
	input_urls = text.get('1.0', 'end-1c')
	if not input_urls:
		info('您的输入有误！')
	music_urls = input_urls.split('\n')
	for i in music_urls:
		down.down_music(i, down_path.get())
	info('下载完成')


label1 = tk.Label(top, text="音乐试听链接（多个地址请换行隔开）：")
text = tk.Text(top, height=10, width=60)
label2 = tk.Label(top, text="保存到本地路径（不填默认为当前目录）：")
entry = tk.Entry(top, width=60, textvariable=down_path)
down_button = tk.Button(top, text="点击下载", command=downMusic)

labelSpace1 = tk.Label(top, text=" ")
labelSpace2 = tk.Label(top, text=" ")
labelSpace3 = tk.Label(top, text=" ")
labelSpace4 = tk.Label(top, text=" ")

labelSpace1.pack()
label1.pack()
text.pack()
labelSpace2.pack()
label2.pack()
entry.pack()
labelSpace3.pack()
down_button.pack()
labelSpace4.pack()

tk.mainloop()
		