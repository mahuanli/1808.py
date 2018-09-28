import pygame
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,spend = 1):
		super().__init_()
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_ret()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed

class EnemySprite(GameSprite):
	def __init__(self):
		imagename = './images/enemy1.png'
		super().__init__(imagename,10)
