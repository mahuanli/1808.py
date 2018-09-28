list = [{"name":"冯帅","age":98},{"name":"马欢丽小仙女","age":16}]
f = open("data.data","w")
f.write(str(list))
f.close()

f1 = open("data.data","r")
