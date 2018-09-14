class Cat():
	def __init__(self):
		print('init')
		self.name = name
		self.money = 1000
	def __str__(self):
		print('str')
		return 'str'
	def __del__(self):
		print('del')
	def __new__(cls):
		return super().__new__(cls)
cat = Cat
print(cat.name)

