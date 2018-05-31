'''
Player Class
'''

import pygame as pyg
from data.lib.Entity import Entity
from pygame import Rect
from data.assets.textures.Textures import *

class Player(Entity):
	# initialize local variables
	def __init__(self, spawn):
		Entity.__init__(self)
		self.state = 0
		self.xfall = 0
		self.yfall = 0
		self.onGround = False
		self.image = player_tex[self.state]
		self.image.convert_alpha()
		self.rect = Rect(spawn[0], spawn[1], 13, 18)

	def update(self, up, down, left, right, platforms, shoot, power_up):
		self.power_up = power_up
		self.image = player_tex[self.state]

		if up:
			# only jump if on the ground
			if self.onGround:
				self.yfall -= 4

		elif not up:
			self.yfall += 0.175
			if self.yfall > 50:
				self.yfall = 50

		if down:
			pass

		if left:
			self.xfall = -3
			self.state = 1

		if right:
			self.xfall = 3
			self.state = 0

		if shoot:
			pass

		if not self.onGround:
			self.yfall += 0.175
			# terminal velocity
			if self.yfall > 50:
				self.yfall = 50

		if not (left or right or shoot):
			self.xfall = 0

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


