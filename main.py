<<<<<<< HEAD
import pygame, sys
from settings import *

class Game:
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Świat według Arii')
		self.clock = pygame.time.Clock()

	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
=======
import pygame, sys
from settings import *

class Game:
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Świat według Arii')
		self.clock = pygame.time.Clock()

	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
>>>>>>> 048b25f0300d79159682f15716b965358e51cbc9
	game.run()