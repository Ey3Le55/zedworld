'''
Level Class
'''

import pygame as pyg
from data.lib.Platform import Platform
from data.assets.textures.Textures import *

class Level(object):
	def __init__(self, level):
		self.level = level
		self.platforms = []
		self.back_platforms = []
		self.entities = pyg.sprite.Group()
		self.spawn = []
		self.zspawn = []

	def init(self):
		x = y = 0
		for row in self.level:
			for col in row:
				if col == "P":
					p = Platform(x, y, wood_1)
					self.platforms.append(p)
					self.entities.add(p)
				if col == "F":
					p = Platform(x, y, wood_floor_1)
					self.platforms.append(p)
					self.entities.add(p)
				if col == "B":
					p = Platform(x, y, wood_top_1)
					self.back_platforms.append(p)
					self.entities.add(p)
				if col == "S":
					self.spawn = [x, y]
				if col == "Z":
					self.zspawn.append([x, y])
				x += 16
			y += 16
			x = 0