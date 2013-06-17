import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class GameWindow:
	def __init__(self):
		# inicializacao
		pygame.init()
		# window init
		self._screen = pygame.display.set_mode((800,600))
		pygame.display.set_caption("Tower Defense")
		# mouse init
		pygame.mouse.set_visible(1)
		self._background = pygame.Surface(self._screen.get_size())
		self._background = self._background.convert()
		self._background.fill((250, 150, 50))
		# clock
		self._clock = pygame.time.Clock()
		# loop 
		self._runningGame = True
	def running(self):
		return self._runningGame
	def stop(self):
		self._runningGame = False

def main():
	# inicializacao
	game = GameWindow()
	
	while game.running():
		# window/mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.stop()
			
				
		game._clock.tick(60)	
		game._screen.blit(game._background, (0, 0))
		pygame.draw.rect(game._screen,(0,0,0), pygame.Rect(20, 25, 40, 50))
		pygame.display.flip()
main()
