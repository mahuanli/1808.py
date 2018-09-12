"""
class person():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def eat(self):
		print('吃')
	def sleep(self):
		print('睡')


class binge(person)
	def music(self):
		print('听音乐')

class xiaoyuan(person)
	def look(self):
		print('看电影')

bg = binge()
xy = xiaoyuan()

bg.eat()
bg.sleep()
bg.music()

xy.eat()
xy.sleep()
xy.look()
"""








class person():

	def __init__(self,name):
		self.name = name

class yuange(person):
	def eat(self):
		print('香菜')
class yuange(person):
	def eat(self):
		print('不吃香菜')

class A(person):
	def yuange(self):
		print('嗷嗷嗷啊')

class C(yuange,A):
	pass

xy_C = c
xy_C.eat()

print(C. __mro__)
























