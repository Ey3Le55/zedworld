'''
Entity Class (Sprite)
'''

import pygame as pyg

class Entity(pyg.sprite.Sprite):
	def __init__(self):
		pyg.sprite.Sprite.__init__(self)
