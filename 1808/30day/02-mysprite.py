import pygame

import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

	def __init__(self,imagename,speed=4):

		super().__init__()

		self.image = pygame.image.load(imagename)

		self.rect = self.image.get_rect()

		self.speed = speed

	def update(self):

		self.rect.y += self.speed





class EnemySprite(GameSprite):

	def __init__(self):

		self.imagename = "./images/enemy1.png"

		super().__init__(self.imagename)

		self.rect.bottom = 0

		maxvalue = SCREEN_RECT.width - self.rect.width

		self.rect.x = random.randint(0, maxvalue)

		self.speed = random.randint(1,8)

	def update(self):

		super().update()

		if self.rect.bottom >= SCREEN_RECT.height:

			self.kill()

			print("敌机摧毁")



class BackgroundSprite(GameSprite):

	def __init__(self,is_alt=False,):

		self.imagename = "./images/background.png"

		super().__init__(self.imagename)

		if is_alt:

			self.rect.y = -self.rect.height

	def update(self):

		super().update()

		if self.rect.top >= SCREEN_RECT.height:

			self.rect.y = -self.rect.height



class Hero(GameSprite):

	def __init__(self):

		self.imagename = "./images/hero1.png"

		super().__init__(self.imagename,0)

		self.rect.centerx = SCREEN_RECT.centerx

		self.rect.bottom = SCREEN_RECT.bottom - 80

		self.rect.x += self.speed

		self.bulletgroup = pygame.sprite.Group()

	def update(self):

		self.rect.x += self.speed

		self.rect.y += self.speed1

		if self.rect.left < 0:

			self.rect.left = 0

		if self.rect.right > SCREEN_RECT.right:

			self.rect.right = SCREEN_RECT.right

		if self.rect.top < 0:

			self.rect.top = 0

		if self.rect.bottom > SCREEN_RECT.bottom:

			self.rect.bottom = SCREEN_RECT.bottom

	def fire(self):

		print("发射子弹")

		

		bullet = Bullet()

		bullet.rect.bottom = self.rect.y +10

		bullet.rect.centerx = self.rect.centerx

		self.bulletgroup.add(bullet)



		bullet = Bullet()

		bullet.rect.bottom = self.rect.y +30

		bullet.rect.centerx = self.rect.centerx+50

		self.bulletgroup.add(bullet)

		

		bullet = Bullet()

		bullet.rect.bottom = self.rect.y +30

		bullet.rect.centerx = self.rect.centerx-50

		self.bulletgroup.add(bullet)

class Bullet(GameSprite):

	def __init__(self):

		self.imagename = "./images/plane.png"

		super().__init__(self.imagename,-3)

	def update(self):

		super().update()

		if self.rect.bottom < 0:

			self.kill()

	





















'''

class EnemySprite1(GameSprite):

	def __init__(self):

		self.imagename = "./images/enemy2.png"

		super().__init__(self.imagename)

	def update(self):

		super().update()

'''


