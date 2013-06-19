import os, sys
import abc

class Object:
	__metaclass__ = abc.ABCMeta
	
	_currentPosition = [0,0]
	_alive = True
	
	def getPosition(self):
		return _currentPosition
	def destroy(self):
		_alive = false

	@abc.abstractmethod
	def draw(self):
		"""Implemented on each of the leaves"""
		return

	def getDistance(self, x, y):
		return math.sqrt(math.pow(self._currentPosition[0]-x,2)+math.pow(self._currentPosition[1]-y,2))

class Enemy(Object):
	__metaclass__ = abc.ABCMeta
	_healthPool = 0
	_moveSpeed = 0.0
	_reward = 0

	def getHealth(self):
		return self._healthPool

	def inflictDamage(self, damage):
		self._healthPool -= damage
		if self._healthPool <= 0:
			_alive = False

class Red(Enemy):
	def __init__(self, position):
		self._currentPosition = position
		self._healthPool = 10
		self._moveSpeed = 2.0
		self._reward = 2

	def draw(self):
		"""Code to draw"""
		return

class Green(Enemy):
	def __init__(self, position):
		self._currentPosition = position
		self._healthPool = 15
		self._moveSpeed = 1.0
		self._reward = 5

	def draw(self):
		"""Code to draw"""
		return

class Blue(Enemy):
	def __init__(self, position):
		self._currentPosition = position
		self._healthPool = 5
		self._moveSpeed = 3.0
		self._reward = 1
		

	def draw(self):
		"""Code to draw"""
		return

class Tower(Object):
	__metaclass__ = abc.ABCMeta

	_attackMode = False
	_cost = 0

	@abc.abstractmethod
	def attack(self):
		"""Implemented in each of the towers"""
		return

	@staticmethod
	@abc.abstractmethod
	def towerCost(self):
		"""Implemented in each of the towers"""
		return

class CannonTower(Tower):
	def __init__(self, x, y):
		self._currentPosition = [x,y]
		self._cost = 150
		self._attackMode = AttackClosest(x,y)
		self._lastAttack = 0

	def attack(self):
		target = _attackMode.getTarget()
		return

	def draw(self):
		pygame.draw.rect(self._screen,(139,101,8),pygame.Rect(self._currentPosition[0],self._currentPosition[1],30,30))
		return

	@staticmethod
	def towerCost(self):
		return 150;

class ArrowTower(Tower):
	def __init__(self, x, y):
		self._currentPosition = [x,y]
		self._cost = 50
		self._attackMode = AttackClosest(x,y)
		self._lastAttack = 0

	def attack(self):
		target = _attackMode.getTarget()
		return

	def draw(self):
		pygame.draw.rect(self._screen,(153,204,50),pygame.Rect(self._currentPosition[0],self._currentPosition[1],30,30))
		return

	@staticmethod
	def towerCost(self):
		return 50;

class FrostTower(Tower):
	def __init__(self, x, y):
		self._currentPosition = [x,y]
		self._cost = 75
		self._attackMode = AttackClosest(x,y)
		self._lastAttack = 0

	def attack(self):
		target = _attackMode.getTarget()
		return

	def draw(self):
		pygame.draw.rect(self._screen,(77,77,255),pygame.Rect(self._currentPosition[0],self._currentPosition[1],30,30))
		return

	@staticmethod
	def towerCost(self):
		return 75;

class Attack:
	_x = 0
	_y = 0

	def inRange(self, enemy):
		return enemy.getDistance(_x,_y) < 4
	
class AttackClosest(Attack):
	def __init__(self, position):
		self._x = position[0]
		self._y = position[1]

	def getTarget(self, enemies):
		closest = 1000
		target = False
		if enemies:
			for enemy in enemies:
				if enemy.getDistance(_x,_y) < closest:
					if inRange(enemy):
						closest = enemy.getDistance()
						target = enemy
		return target	

		if enemies:
			return enemies[0]
		return false

class AttackLowest(Attack):
	def __init__(self, position):
		self._x = position[0]
		self._y = position[1]

	def getTarget(self, enemies):
		lowestHealth = 1000
		target = False
		if enemies:
			for enemy in enemies:
				if enemy.getHealth() < lowestHealth:
					if inRange(enemy):
						lowestHealth = enemy.getHealth()
						target = enemy
		return target	
	


