class yang():

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def sleep(self):
		print('睡午觉觉觉')
	def eat(self):
		print('草莓蛋糕,青草沙拉,菠萝布丁')
	def play(self):
		print('搓麻将,斗地主,吃鸡,王者荣耀')

	def __str__(self):
		msg = ('我的名字是%s,我的年龄是%d'%(self.name,self.age))
		return msg
xiaomei = yang('小美',21)
xiaomei.sleep()
xiaomei.eat()
xiaomei.play()
print(xiaomei)
