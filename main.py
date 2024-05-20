import pygame, sys
from settings import *
from level import *

class Game:
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('Świat według Arii')
		self.clock = pygame.time.Clock()
		self.level = Level()
		main_audio = pygame.mixer.Sound('audio/ARIASWORLD.wav')
		main_audio.play(loops=-1)

	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		
			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

Game().run()