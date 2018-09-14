class showError(Exception):#Exception是异常的顶级父类

	def __init__(self,len):
		super().__init__()
		self.len = len

try:
	name = input('请输入一个名字')
	if len(name) == 3:
		raise showError(len(name))
except showError as ret:
	print('需要%d个长度但是你输入了%d个长度'%(100,ret.len))
