year = int(input("输入年份"))

if year%4 == 0 and year%100 !=0:
	print("是闰年")
elif year%400 == 0:
	print("是闰年")
else:
	print("平年")
