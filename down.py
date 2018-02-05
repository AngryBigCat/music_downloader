#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import base64
import re
from bs4 import BeautifulSoup
from urllib import request

def down_music(url, path = '.'):
	html = request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	# 找到音乐地址
	result = soup.find(id="musicSrc").get('src')
	# 将音乐地址解码
	music_url = base64.b64decode(result)
	# 获取音乐正式链接，使用正则匹配音乐编号及后缀
	re_match = re.match(b'^.*/([\w]+\.mp3)$', music_url)
	# 如果未找到
	if re_match == None:
		print('未找到这首歌曲:%s' % music_url.decode('utf-8'))
		exit()
	# 打开音乐链接
	music_data = request.urlopen(music_url.decode('utf-8'))
	# 将参数转换为绝对路径
	current_dir = os.path.abspath(path)
	# 如果找不到用户输入的文件夹路径，那就创建
	if not os.path.isdir(current_dir):
		os.mkdir(current_dir)
	# 找到音乐名
	music_name = soup.find(class_="song").span.get_text()
	# 音乐名与音乐编号及后缀连接，组成下载时的音乐名
	music = music_name + '-' + re_match.group(1).decode('utf-8')
	# 将绝对路径与音乐名相连
	down_music = os.path.join(current_dir, music)
	#下载文件
	with open(down_music, 'wb') as f:
		f.write(music_data.read())

	print("%s 下载完成" % music)






		