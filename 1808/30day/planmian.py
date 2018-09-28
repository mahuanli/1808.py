import pygame

from mysprite import *



class PlaneGame(object):

	"""飞机大战主游戏"""

	def __init__(self):

		print("游戏初始化")

		self.screen = pygame.display.set_mode(SCREEN_RECT.size)

		self.clock = pygame.time.Clock()

		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)

		pygame.time.set_timer(HERO_FIRE_EVENT, 300)

	def start_game(self):

		print("开始游戏...")

		while True:

			# 1. 设置刷新帧率

			self.clock.tick(60)

			# 2. 事件监听

			self.__event_handler()

			# 3. 碰撞检测

			self.__check_collide()

			# 4. 更新精灵组

			self.__update_sprites()

			# 5. 更新屏幕显示

			pygame.display.update()

	def __create_sprites(self):

		bg1 = BackgroundSprite()

		bg2 = BackgroundSprite()

		bg2.rect.y = -bg2.rect.height

		self.backgroup = pygame.sprite.Group(bg1,bg2)

		

		self.enemygroup = pygame.sprite.Group()

		self.hero = Hero()

		self.herogroup = pygame.sprite.Group(self.hero)

		#self.bulletgroup = pygame.sprite.Group()

	def __event_handler(self):

		"""事件监听"""

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				PlaneGame.__game_over()

			elif event.type == CREATE_ENEMY_EVENT:

				print("敌机出场...")

				enemy = EnemySprite()

				self.enemygroup.add(enemy)

			elif event.type == HERO_FIRE_EVENT:

				self.hero.fire()

		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_RIGHT]:

			self.hero.speed = 8

			self.hero.speed1 = 0

		elif keys_pressed[pygame.K_LEFT]:

			self.hero.speed = -8

			self.hero.speed1 = 0

		elif keys_pressed[pygame.K_UP]:

			self.hero.speed = 0

			self.hero.speed1 = -4

		elif keys_pressed[pygame.K_DOWN]:

			self.hero.speed = 0

			self.hero.speed1 = 4

		else:

			self.hero.speed = 0

			self.hero.speed1 = 0

	def __check_collide(self):

		"""碰撞检测"""

		pygame.sprite.groupcollide(self.hero.bulletgroup, self.enemygroup, True, True)

		enemies = pygame.sprite.spritecollide(self.hero, self.enemygroup, True)

		if len(enemies) > 0:

			self.hero.kill()

			PlaneGame.__game_over()

	def __update_sprites(self):

		"""更新精灵组"""

		self.backgroup.update()

		self.backgroup.draw(self.screen)

		self.enemygroup.update()

		self.enemygroup.draw(self.screen)

		self.herogroup.update()

		self.herogroup.draw(self.screen)

		self.hero.bulletgroup.update()

		self.hero.bulletgroup.draw(self.screen)

	@staticmethod

	def __game_over():

		"""游戏结束"""



		print("游戏结束")

		pygame.quit()

		exit()

if __name__ == '__main__':

# 创建游戏对象

	game = PlaneGame()



# 开始游戏

	game.start_game()
