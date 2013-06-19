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
		self._totalGold = 100
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
		if self._currentWave == 1:
			return [Red]
		elif self._currentWave == 2:
			return [Red,Blue]
		else:
			return [Red,Blue,Green]

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

	def getRemainingLife(self):
		return self._remainingLife
	
	
