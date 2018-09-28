import pygame

from mysprite import *

pygame.init()

#创建游戏主窗口

screen = pygame.display.set_mode((480,700))

#绘制背景图像

bg = pygame.image.load("./images/background.png")

#绘制在屏幕

#screen.blit(bg,(0,0))

#pygame.display.update()



#绘制图像

hero = pygame.image.load("./images/hero1.png")

#绘制在屏幕

herorect = pygame.Rect(200,500,120,120)

#screen.blit(hero,herorect)

#pygame.display.update()

#创建游戏时钟对象

clock = pygame.time.Clock()



enemy = EnemySprite()

enemy.speed = 2

enemy1 = EnemySprite1()

enemy1.rect.x = 150

enemy1.speed = 1

enemy2 = EnemySprite1()

enemy2.rect.x = 300

enemy2.speed = 3

enemygroup = pygame.sprite.Group(enemy,enemy1,enemy2)







while True:

	clock.tick(60)

	herorect.y -= 3

	screen.blit(bg,(0,0))

	screen.blit(hero,herorect)



	if herorect.bottom <= 0:

		herorect.top = 700

	enemygroup.update()

	enemygroup.draw(screen)

# 事件监听

	for event in pygame.event.get():

	# 判断用户是否点击了关闭按钮

		if event.type == pygame.QUIT:

			print("退出游戏...")

			pygame.quit()

			# 直接退出系统

			exit()

	pygame.display.update()
