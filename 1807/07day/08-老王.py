name = input("请输入名字")
money = int(input("请输入金钱"))
if name=="老王" and money>=1000:
	print("钻石王老五")
elif name=="老王" and money<=500:
	print("穷逼王老五")
else:
	print("不知道")
