import os, sys
import abc
import pygame
import math

class Object:
	__metaclass__ = abc.ABCMeta
	
	_currentPosition = [0,0]
	_alive = True
	
	def getPosition(self):
		return self._currentPosition
	def destroy(self):
		_alive = False
	
	def isAlive(self):
		return _alive

	@abc.abstractmethod
	def draw(self, screen):
		"""Implemented on each of the leaves"""
		return

	def getDistance(self, x, y):
		return math.sqrt(math.pow(self._currentPosition[0]-int(x/30),2)+math.pow(self._currentPosition[1]/30-int(y/30),2))

class Enemy(Object):
	__metaclass__ = abc.ABCMeta
	_healthPool = 0
	_moveSpeed = 0.0
	_reward = 0

	def getHealth(self):
		return self._healthPool
	
	def isAlive(self):
		return _alive
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

	def draw(self, screen):
		if int(9*self._healthPool/10) > 0:
			pygame.draw.rect(screen,(0,255,0),pygame.Rect(self._currentPosition[1]*30+12,self._currentPosition[0]*30-10,int(9*self._healthPool/10),3))
		pygame.draw.circle(screen,(255,0,0),(self._currentPosition[1]*30+15,self._currentPosition[0]*30+5),5)
		return
	def move(self, newPosition):
		if self._healthPool > 0:
			self._currentPosition = newPosition
	
	def getMoveSpeed(self):
		return self._moveSpeed

class Green(Enemy):
	def __init__(self, position):
		self._currentPosition = position
		self._healthPool = 15
		self._moveSpeed = 1.0
		self._reward = 5

	def draw(self, screen):
		if int(9*self._healthPool/15) > 0:
			pygame.draw.rect(screen,(0,255,0),pygame.Rect(self._currentPosition[1]*30+22,self._currentPosition[0]*30-10,int(9*self._healthPool/15),3))
		pygame.draw.circle(screen,(0,255,0),(self._currentPosition[1]*30+25,self._currentPosition[0]*30+5),5)

	def move(self, newPosition):
		if self._healthPool > 0:
			self._currentPosition = newPosition
	def getMoveSpeed(self):
		return self._moveSpeed

		return

class Blue(Enemy):
	def __init__(self, position):
		self._currentPosition = position
		self._healthPool = 5
		self._moveSpeed = 3.0
		self._reward = 1
		

	def draw(self, screen):
		if int(9*self._healthPool/5) > 0:
			pygame.draw.rect(screen,(0,255,0),pygame.Rect(self._currentPosition[1]*30+2,self._currentPosition[0]*30-10,int(9*self._healthPool/5),3))
		pygame.draw.circle(screen,(0,0,255),(self._currentPosition[1]*30+5,self._currentPosition[0]*30+5),5)

	def move(self, newPosition):
		if self._healthPool > 0:
			self._currentPosition = newPosition

		return
	def getMoveSpeed(self):
		return self._moveSpeed

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
		self._attackMode = AttackClosest([x,y])
		self._lastAttack = 0
		self._color = (139,101,8)
		self._damage = 10

	def attack(self, enemies):
		target = self._attackMode.getTarget(enemies)
		if target:
			print "ATTACK BY CANON"
			target.inflictDamage(self._damage)
		return

	def draw(self, screen):
		pygame.draw.rect(screen,(139,101,8),pygame.Rect(self._currentPosition[0],self._currentPosition[1],30,30))
		return

	@staticmethod
	def towerCost():
		return 150;

class ArrowTower(Tower):
	def __init__(self, x, y):
		self._currentPosition = [x,y]
		self._cost = 50
		self._attackMode = AttackClosest([x,y])
		self._lastAttack = 0
		self._color = (153,204,50)
		self._damage = 10

	def attack(self, enemies):
		target = self._attackMode.getTarget(enemies)
		if target:
			print "ATTACK BY ARROW"
			target.inflictDamage(self._damage)
		return

	def draw(self, screen):
		pygame.draw.rect(screen,(153,204,50),pygame.Rect(self._currentPosition[0],self._currentPosition[1],30,30))
		return

	@staticmethod
	def towerCost():
		return 50;

class FrostTower(Tower):
	def __init__(self, x, y):
		self._currentPosition = [x,y]
		self._cost = 75
		self._attackMode = AttackClosest([x,y])
		self._lastAttack = 0
		self._color = (77,77,255)
		self._damage = 10

	def attack(self, enemies):
		target = self._attackMode.getTarget(enemies)
		if target:
			print "ATTACK BY FROST"
			target.inflictDamage(self._damage)
		return

	def draw(self, screen):
		pygame.draw.rect(screen,(77,77,255),pygame.Rect(self._currentPosition[0],self._currentPosition[1],30,30))
		return

	@staticmethod
	def towerCost():
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
				if enemy.getDistance(self._x,self._y) < closest and enemy.getHealth() > 0:
					print "HERE"
					print enemy.getDistance(self._x,self._y)
					print "__________"
					if self.inRange(enemy):
						print "KKKKKKKKKKKKKKKKKKKKK"
						closest = enemy.getDistance(self._x,self._y)
						target = enemy
		return target	
	
		if enemies:
			return enemies[0]
		return false
		
	def inRange(self, enemy):
		return enemy.getDistance(self._x,self._y) < 7
		
		
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
	


