'''
from mulitipocessing import process
import time
num = 0
def test(a):
	global num
	for i in range(10):
		print('老王',a)
		num+=1
		time.sleep(1)

p = process(target=test,args=('老宋',))#创建子进程
p.start()#子进程启动


p.join(3)#超时三秒
print(num)
print('哈哈哈')
'''





















from multiprocessing import Pool
from time import sleep

def work(arg):
	for i in range(5):
		print('老王',arg)
		sleep(1)

p = Pool()
for i in range(5):
	p.apply_async(work,(i,))
	print('加入成功')

p.close()
p.join()
print('哈哈哈')
