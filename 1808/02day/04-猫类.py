class cat:

	def eat(self):

		print("吃")

	def sleep(self):

		print("睡")

	def play(self):

		print("玩")

	def introduce(self):

		print("我年龄是%d  身高是%d"%(self.age,self.height))





z = cat()

x = cat()

z.eat()

z.sleep()

z.play()



z.age = 20

z.height = 170

x.age = 23

x.height = 180

z.introduce()

x.introduce()
