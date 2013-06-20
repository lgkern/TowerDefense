import os, sys
from pygame.locals import *
from mapControler import MapControler
from objects import *
from lib.objects import Red, Green, Blue

class iGame:
#	_totalGold = 100
#	_remainingLife = 50
#	_currentWave = 0
	def __init__(self):
		self._totalGold = 1000
		self._remainingLife = 50
		self._map = MapControler()
		self._currentWave = 0
	
	def placeTower(self, towerType, x, y):
		reqGold = towerType.towerCost()
		if reqGold <= self._totalGold:
			if self._map.addTower(towerType, x, y):
				self._totalGold -= reqGold
				return True
		return False

	def getNextWave(self):
		self._currentWave += 1
		return self._wave(self._currentWave)
		
	def _wave(self, waveNumber):
		if waveNumber == 0:
			return []
		else:
			waveNumber -= 1
			if self._currentWave % 3 == 0:
				return [Red] + self._wave(waveNumber)
			elif self._currentWave % 3 == 1:
				return [Red,Blue] + self._wave(waveNumber)
			else:
				return [Red,Blue,Green] + self._wave(waveNumber)
			
	def enemiesScore(self):
		return self._map.enemiesKilled();	

	def spawnEnemy(self, enemyType):
		self._map.addEnemy(enemyType)
		return True

	def getPath(self):
		return self._map.getPath()
	
	def drawTowers(self, screen):
		self._map.drawAllTowers(screen)
		return

	def drawEnemies(self, screen):
		self._map.drawAllEnemies(screen)
		return

	def getTotalGold(self):
		return self._totalGold

	def moveEnemies(self):
		enemiesReached = self._map.moveEnemies()
		self._remainingLife -= enemiesReached
		return
	def attackTowers(self):
		self._map.attackTowers()
		return
	def getRemainingLife(self):
		return self._remainingLife
	
	
