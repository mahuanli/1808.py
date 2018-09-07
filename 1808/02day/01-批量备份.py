import os
name = input("请输入名字")
files = os.listdir(name)
os.chdir(name)
for i in files:
	p = i.rfind(".")
	newname = i[:p]+"精品"+i[p:]
	os.rename(i,newname)
