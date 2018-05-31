'''
Menu Class
'''

import pygame as pyg
from data.config import *

class Menu(object):
	def __init__(self):
		self.surface = pyg.display.set_mode(DISPLAY)
		self.font = pyg.font.SysFont('Helvetica', 32)

