import os, sys
import pygame
from pygame.locals import *
from lib.igame import iGame
from lib.objects import ArrowTower, FrostTower, CannonTower

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

		#Map Settings
		self._side = 30
		self._margin = 2
		self._controler = iGame()

		#Menu Settings
		self._myfont = pygame.font.SysFont("Arial",22)
		self._towerTypes = []
		# type | color | y pos | selected
		self._towerTypes.append([ArrowTower,(153,204,50), 630, False])
		self._towerTypes.append([CannonTower,(139,101,8), 680, False])
		self._towerTypes.append([FrostTower,(77,77,255), 730, False])
		
		self._nextWave = 300
		self._nextMove = 10
		
		self.started = False
		
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
		self._controler.drawTowers(self._screen)
		return
		 
		 
	def drawEnemies(self):
		self._controler.drawEnemies(self._screen)
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
		for tower in self._towerTypes:
			if tower[3]:
				pygame.draw.rect(self._screen,(255,255,255),pygame.Rect(tower[2]-1,50-1,42,42))
			pygame.draw.rect(self._screen,tower[1],pygame.Rect(tower[2],50,40,40))		
		labelGold = self._myfont.render("Current Gold: "+str(self._controler.getTotalGold()),1,(255,255,0))
		self._screen.blit(labelGold, (610, 450))

		labelLife = self._myfont.render("Remaining Life: "+str(self._controler.getRemainingLife()),1,(255,0,0))
		self._screen.blit(labelLife, (610, 300))
		
		pygame.draw.rect(self._screen,(255,255,255),pygame.Rect(650,245,100,30))
		
		labelLife = self._myfont.render("START",1,(0,0,0))
		self._screen.blit(labelLife, (660, 250))
		
		return
	
	def towerInMenu(self, x, y):
		# 
		true = False
		if y in range(50,90):
			for tower in self._towerTypes:
				if x in range(tower[2], tower[2]+40):
					tower[3] = True
					true = True
				else:
					# deseleciona caso nao tenha clicado
					tower[3] = False
		
		if true:
			return True
		return False

	def towerInGrid(self,x,y):
		# se alguma torre do menu estiver selecionada
		for tower in self._towerTypes:
			if tower[3]:
				# ve se a posicao x,y esta num grid e pega suas coordenadas
				posX = int(x/30)*30
				posY = int(y/30)*30
				print posX
				print posY
				# desenha a torre no grid
				self._controler.placeTower(tower[0], posX, posY)
				tower[3] = False
		return

	def moveEnemies(self):
		self._controler.moveEnemies()
		return

	def attackTowers(self):
		self._controler.attackTowers()
		return
		
	def spawnEnemies(self):
		enemyWave = self._controler.getNextWave()
		map(self._controler.spawnEnemy, enemyWave)

	def spawnControl(self):
		self._nextWave -= 1
		if self._nextWave == 0:
			self._nextWave = 300
			self.spawnEnemies()	

	def moveControl(self):
		self.attackTowers()
		self._nextMove -= 1
		if self._nextMove == 0:
			self._nextMove = 10
			self.moveEnemies()
	
	def startButtonPress(self, x, y):
		if x in range(650,750):
			if y in range(245,275):
				return True
		return False
	def loop(self):
		# window/mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.stop()	
			if event.type == pygame.MOUSEBUTTONDOWN:
				#self.stop()
				x, y = event.pos
				if self.startButtonPress(x,y):
					self.started = True
				else:
					if self.towerInMenu(x, y):
						print "Tower Selected"
					else:
						# if some is selected
						self.towerInGrid(x,y)

		if self.started :
			self.spawnControl()
			self.moveControl()
			self._clock.tick(60)	
		self.drawBackground()
		self.drawPath()
		self.drawMenu()
		self.drawTowers()
		self.drawEnemies()		
		self.drawGrid()	
		#pygame.draw.rect(self._screen,(0,0,0), pygame.Rect(20, 25, 40, 50))
		pygame.display.flip()
			
		
		

def main():
	# inicializacao
	game = GameWindow()
	
	while game.running():
		game.loop()
main()
