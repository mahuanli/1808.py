def test1(num):
	def g1():
		print('买了佛雷')
		num()
	return g1

@test1
def test1():
	print('哈哈哈哈')

test1()
