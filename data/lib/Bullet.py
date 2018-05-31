'''
Bullet Class
'''

import pygame as pyg
from data.lib.Entity import Entity
from pygame import Rect
from pygame import Surface
from data.assets.textures.Textures import *
import random as r
import math as m

class Bullet(Entity):
	# initialize local variables
	def __init__(self, spawn, player):
		Entity.__init__(self)
		self.destroyed = False
		self.state = player.state
		self.xfall = 0
		self.yfall = 0
		self.onGround = False
		self.image = Surface((6,1))
		self.image.fill((250,220,80))
		self.rect = Rect(spawn[0]+5, spawn[1]+14, 6, 1)

	def update(self, platforms):
		if self.state == 0:
			self.xfall = r.random()*2+10
		if self.state == 1:
			self.xfall = -(r.random()*2+10)


		self.rect.left += self.xfall
		self.collide(self.xfall, 0, platforms)
		self.rect.top += self.yfall
		self.onGround = False
		self.collide(0, self.yfall, platforms)

	# collision detection
	def collide(self, xfall, yfall, platforms):
		for p in platforms:
			if pyg.sprite.collide_rect(self, p):
				self.destroyed = True