class An():
	def __init__(self):
		self.__age = 15

	def getAn(self):
		return self.__age

	def __getAn(self):
		return 98
	def getAn(self):
		return self.__getAn()

class dog(An):
	pass
class cat(An):
	pass
