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
		enemies.append(eval(color+"(_path[0])"))
		return True

	def addTower(self, towerType, x, y):
		if availableSlot(x,y):		
			self._tower.append(eval(towerType+"("+x+","+y+")")) #)ArrowTower(x,y))
			return True
		return False
	
	def	availableSlot(self, x, y):
		try:
			_path.index([x,y])
			return False
		finally:
			slotFree = True
			for tower in towers:
				if tower.getPosition() == [x,y]:
					slotFree = False
			return slotFree

								
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


"""
		if color == "red":
			enemies.append(Red(_path[0]))
		elif color == "blue":
			enemies.append(Blue(_path[0]))
		elif color == "green":
			enemies.append(Green(_path[0]))"""

"""			elif towerType == "cannon":
				tower.append(CannonTower(x,y))
			elif towerType == "frost":
				tower.append(FrostTower(x,y))
			else:
				return False"""

