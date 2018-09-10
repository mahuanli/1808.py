class Teacher():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def teach(self):
		print('教书育人')
	def sleep(self):
		print('睡午觉')
	def eat(self):
		print('吃早点')
	def __str__(self):
		msg = '我叫%s,年龄%d'%(self.name,self.age)
		return msg

xiaoyuan = Teacher('小源',30)
xiaoyuan.teach()
xiaoyuan.sleep()
xiaoyuan.eat()
print(xiaoyuan)
