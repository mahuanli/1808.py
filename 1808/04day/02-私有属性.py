class person():

	def __init__(self,name):
		self.name = name
		self.__mimi = '我有99个对象'
		self.__sifangqian = 100
	def getMi(self):
		return self.__mimi
	def getMoney(self):
		return self.__sifangqian

lz = person('小源')
print(lz.getmi())

print(lz.getMoney())
