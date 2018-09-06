import os
dir = input("亲你个输入批量重命名的文件夹名字")
files = os.listdir(dir)#列表
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"腾讯"+i[position]
	oldname = dir+"/"+i#movie/吃鸡.py
	newname = dir+"/"+newname

	os.rename(oldname,newname)
