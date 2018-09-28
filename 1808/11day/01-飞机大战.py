






























		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#定制器
		self.enemy_group = pygame.sprite.Group()
	def start_game(self):
		print('开始游戏...')
		while True:
			self.clock.tick(68)#每秒刷新68次
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()

			pygame.display.update()#更新


	def __create__sprites(self):#创建精灵
		bgs = BackGroundSprint()
		bgs1 = BackGroundSprint(False)#这个隐藏在屏幕上面
		self.bgsg = pygame.sprite.Group(bgs,bgs1)

	def __event_handler(self):
		""""事件监听""""

		for event in pygame.event.get


















































