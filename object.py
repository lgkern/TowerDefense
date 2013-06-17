import os, sys
import pygame
import abc

class Object:
	__metaclass__ = abc.ABCMeta
	
	_currentPosition = [0,0]
	_alive = true
	
	def getPosition(self):
		return _currentPosition
	def destroy(self):
		_alive = false

	@abc.abstractmethod
	def draw(self):
		"""Implemented on each of the leaves"""
		return

class Enemy(Object):

	_healthPool
	_moveSpeed
	_reward

class Red(Enemy):
	def __init__(self):
		self._healthPool = 10
		self._moveSpeed = 2.0
		self._reward = 2

	def draw(self):
		"""Code to draw"""
		return

class Green(Enemy):
	def __init__(self):
		self._healthPool = 15
		self._moveSpeed = 1.0
		self._reward = 5

	def draw(self):
		"""Code to draw"""
		return

class Blue(Enemy):
	def __init__(self):
		self._healthPool = 5
		self._moveSpeed = 3.0
		self._reward = 1

	def draw(self):
		"""Code to draw"""
		return

class Tower(Object):
	__metaclass__ = abc.ABCMeta

	_attackMode
	_cost

	@abc.abstractmethod
	def attack(self):
		"""Implemented in each of the towers"""
		return

class CannonTower(Tower):
	def __init__(self):
		self._cost = 150
		self._attackMode = AttackClosest
		self._lastAttack = 0

	def attack(self):
		target = _attackMode.getTarget()
		return

	def draw(self):
		"""Code to draw"""
		return



class ArrowTower(Tower):
	def __init__(self):
		self._cost = 50
		self._attackMode = AttackClosest
		self._lastAttack = 0

	def attack(self):
		target = _attackMode.getTarget()
		return

	def draw(self):
		"""Code to draw"""
		return

class FrostTower(Tower):
	def __init__(self):
		self._cost = 75
		self._attackMode = AttackClosest
		self._lastAttack = 0

	def attack(self):
		target = _attackMode.getTarget()
		return

	def draw(self):
		"""Code to draw"""
		return
	
	
	

