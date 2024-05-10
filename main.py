import pygame, sys
from settings import *
from level import *

class Game:
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Świat według Arii')
		self.clock = pygame.time.Clock()
		self.level = Level()

	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.level.run()		
			self.screen.fill('black')
			pygame.display.update()
			self.clock.tick(FPS)

Game().run()