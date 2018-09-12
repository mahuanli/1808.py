class Ananil(object):







	def eat (self):
		print('吃')
	def sleep (self):
		print('睡')


class cat(Ananil):
	pass
class dog(Ananil):
	pass
class person(Ananil):
	pass

bsm = cat
pp = dog
bsm.eat()
hsm.sleep()

pp.eat()
pp.sleep()

