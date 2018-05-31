'''
Enemy Class
'''

import pygame as pyg
from data.lib.Entity import Entity
from pygame import Rect
from data.assets.textures.Textures import *
import random as r
import math as m

class Enemy(Entity):
	# initialize local variables
	def __init__(self, spawn):
		Entity.__init__(self)
		self.type = 0
		self.time = 0
		self.state = 0
		self.xfall = 0
		self.yfall = 0
		self.onGround = False
		self.image = player_tex[self.state]
		self.image.convert_alpha()
		self.rect = Rect(spawn[0], spawn[1], 13, 18)
		self.speed = 2.7

	def update(self, platforms):
		self.image = player_tex[self.state]

		self.rect.left += self.xfall
		self.collide(self.xfall, 0, platforms)
		self.rect.top += self.yfall
		self.onGround = False
		self.collide(0, self.yfall, platforms)

	# collision detection
	def collide(self, xfall, yfall, platforms):
		for p in platforms:
			if pyg.sprite.collide_rect(self, p):
				if xfall > 0:
					self.rect.right = p.rect.left
				if xfall < 0:
					self.rect.left = p.rect.right
				if yfall > 0:
					self.rect.bottom = p.rect.top
					self.onGround = True
					self.yfall = 0
				if yfall < 0:
					self.rect.top = p.rect.bottom
				if self.rect.top == p.rect.bottom:
					self.yfall += 0.35
					if self.yfall > 100:
						self.yfall = 100

	def move_towards_player(self, player):
		# find normalized direction vector (dx, dy) between enemy and player
		try:
			dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
			dist = m.hypot(dx, dy)
			dx, dy = dx / dist, dy / dist
		except:
			pass

		if self.time == 120:
			self.time = 0
		self.time += 1

		# move along this normalized vector towards the player at current speed
		random_direction = 0
		if dist < 170:
			if r.randint(0,100) < 90:
					self.rect.x -= dx * self.speed

			if r.randint(0,10) > 5:
				if self.rect.y - player.rect.y > 0 and self.onGround:
					self.yfall -= r.random()+1.8

		self.yfall += 0.175

		if self.onGround:
			self.yfall -= 0.8

		if self.yfall > 50:
			self.yfall = 50

		if dx > 0:
			self.state = 1
		elif dx < 0:
			self.state = 0
