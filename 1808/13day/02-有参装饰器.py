from time import ctime, sleep

def timefun(func):
	def wrappedfunc():
		print('%s called at %s'%(func.__name__,ctime()))
			func()
		return wrappedfunc

@timefun
def foo():
	print('i am foo')

