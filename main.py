import os, sys
import pygame
from pygame.locals import *
from lib.igame import iGame

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
		self._background.fill((50, 205, 50))
		# clock
		self._clock = pygame.time.Clock()
		# loop 
		self._runningGame = True
		self._side = 30
		self._margin = 2
		self._controler = iGame()
		self._myfont = pygame.font.SysFont("Arial",24)

	def running(self):
		return self._runningGame
	def stop(self):
		self._runningGame = False
	def drawBackground(self):
		self._screen.blit(self._background, (0, 0))
		return
	def drawPath(self):
		path = self._controler.getPath()
		for position in path:
			pygame.draw.rect(self._screen,(255,228,181),pygame.Rect(position[1]*self._side,position[0]*self._side,self._side,self._side))
		pygame.draw.rect(self._screen,(178,34,34),pygame.Rect(path[-1][1]*self._side,path[-1][0]*self._side,self._side,self._side))
		return
	def drawTowers(self):
		return
	def drawEnemies(self):
		return
	def drawGrid(self):
		for line in range(21):
			pygame.draw.rect(self._screen,(0,0,0),pygame.Rect(line*self._side,0,self._margin,600))
			pygame.draw.rect(self._screen,(0,0,0),pygame.Rect(0,line*self._side,600,self._margin))
		return
	def drawMenu(self):
		pygame.draw.rect(self._screen,(0,0,0),pygame.Rect(600,0,200,600))
		label = self._myfont.render("Available Towers",1,(135,206,250))
		self._screen.blit(label, (610, 20))
		return

	def loop(self):
		# window/mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.stop()	

		self.drawBackground()
		self.drawPath()
		self.drawTowers()
		self.drawEnemies()
		self.drawGrid()	
		self.drawMenu()

				
		self._clock.tick(60)	
		
		#pygame.draw.rect(self._screen,(0,0,0), pygame.Rect(20, 25, 40, 50))
		pygame.display.flip()
				
		
		

def main():
	# inicializacao
	game = GameWindow()
	
	while game.running():
		game.loop()
main()
