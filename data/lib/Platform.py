'''
Platform Class
'''

from pygame import Surface, Color, Rect
from data.lib.Entity import Entity

class Platform(Entity):
	def __init__(self, x, y, texture):
		Entity.__init__(self)
		self.image = texture.convert_alpha()
		self.rect = Rect(x, y, 16, 16)

	def update(self):
		pass

