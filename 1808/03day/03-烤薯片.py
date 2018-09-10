import random
class shupian():
	def __init__(self):
		self.status = "生的"
		self.times = 0
		self.zls = []#佐料
	def __str__(self):
		msg = "我叫薯片,我烤的程度是%s,我的作料%s"%(self.status,self.zls)
		return msg
	def kao(self,time):
		self.times+=time
		if self.times >= 1 and self.times <= 2:
			self.status = "生的"
		elif self.times >= 3 and self.times <= 5:
			self.status = "半生不熟"
		elif self.times >= 6 and self.times <= 8:
			self.status = "8分熟"
		elif self.times >= 9 and self.times <= 12:
			self.status = "正好"
		elif self.times > 12:
			self.status = "烤焦了"
	def addzl(self,zl):
		self.zls.append(zl)

keke = shupian()
zls = ['盐巴','辣椒','白糖']
for i in range(10):
	keke.kao(random.randint(1,3))
	if zls:

		s = random.choice(zls)
		zls.remove(s)
		keke.addzl(s)
	print(keke)










