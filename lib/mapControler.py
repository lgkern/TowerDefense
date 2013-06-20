import os, sys
import objects 

class MapControler:
	_enemies = []
	_towers = []
	_path = []
	def __init__(self):
		self._enemies = []
		self._towers = []
		self._path = []
		self._generateMap()

	def addEnemy(self, color): 
		self._enemies.append(color(self._path[0]))
		return True

	def addTower(self, towerType, x, y):
		if self.availableSlot(y,x):		
			self._towers.append(towerType(x,y))
			return True
		return False
	def	availableSlot(self, x, y):
		try:
			self._path.index([x,y])
			return False
		finally:
			slotFree = True
			for tower in self._towers:
				if tower.getPosition() == [x,y]:
					slotFree = False
			return slotFree

	def moveEnemies(self):	
		
		amountEnd = 0
		i = 0
		for enemy in self._enemies:			
			if not moveEnemy(self._path, enemy):
				amountEnd += 1
				self._enemies.pop(i)
			else: 
				if not self._enemies[i].isAlive:
					self._enemies.pop(i)
			i+=1
		return amountEnd;

	def _deleteDead(self):
		for i in range(len(self._enemies)):
			if not self._enemies[i].isAlive:
				self._enemies.pop(i)
								
	def _generateMap(self):
		#assuming a 20x20 initial grid #hue
		self._path.append([0,11])
		self._path.append([1,11])
		self._path.append([2,11])
		self._path.append([3,11])
		self._path.append([4,11])
		self._path.append([5,11])
		self._path.append([6,11])
		self._path.append([7,11])
		self._path.append([8,11])
		self._path.append([9,11])
		self._path.append([9,12])
		self._path.append([9,13])
		self._path.append([9,14])
		self._path.append([9,15])
		self._path.append([10,15])
		self._path.append([11,15])
		self._path.append([12,15])
		self._path.append([12,14])
		self._path.append([12,13])
		self._path.append([12,12])
		self._path.append([12,11])
		self._path.append([13,11])
		self._path.append([14,11])
		self._path.append([15,11])
		self._path.append([16,11])
		self._path.append([17,11])
		self._path.append([18,11])
		self._path.append([19,11])

	def getPath(self):
		return self._path
	
	def enemiesAlive(self):
		return self._enemies

	def drawAllTowers(self,screen):
		for tower in self._towers:
			tower.draw(screen)	

	def drawAllEnemies(self,screen):
		for enemy in self._enemies:
			enemy.draw(screen)
			print enemy._moveSpeed
			print enemy._healthPool
			print "\n"	
			
	def attackTowers(self):
		for tower in self._towers:
			tower.attack(self._enemies)
		return

def moveEnemy(path, enemy):
	currentPosition = path.index(enemy.getPosition())
	if path[-1] == path[currentPosition]:
		enemy.destroy()
		return False
	enemy.move(path[currentPosition+1])	
	return True
	
