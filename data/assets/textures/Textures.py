'''
Textures
'''

import pygame as pyg

# Player Textures
player_tex_r = pyg.image.load('data/assets/textures/playerr.png')
player_tex_l = pyg.image.load('data/assets/textures/playerl.png')
player_tex = [player_tex_r,
			  player_tex_l]

# Zombie Textures
zombie_1 = pyg.image.load('data/assets/textures/zombies/zombie1.png')
zombie_2 = pyg.image.load('data/assets/textures/zombies/zombie2.png')
zombie_3 = pyg.image.load('data/assets/textures/zombies/zombie3.png')
zombie_4 = pyg.image.load('data/assets/textures/zombies/zombie4.png')
zombie_5 = pyg.image.load('data/assets/textures/zombies/zombie5.png')
zombie_6 = pyg.image.load('data/assets/textures/zombies/zombie6.png')
zombie_7 = pyg.image.load('data/assets/textures/zombies/zombie7.png')
zombie_8 = pyg.image.load('data/assets/textures/zombies/zombie8.png')
zombie_9 = pyg.image.load('data/assets/textures/zombies/zombie9.png')


# Platform Textures
tiles_1 = pyg.image.load('data/assets/textures/tiles_1.png')
wood_1 = pyg.image.load('data/assets/textures/wood_1.png')
road_1 = pyg.image.load('data/assets/textures/road_1.png')
road_2 = pyg.image.load('data/assets/textures/road_2.png')
platform_tex = [tiles_1,
			 wood_1,
			 road_1,
			 road_2]

# Platform Top Textures
tiles_top_1 = pyg.image.load('data/assets/textures/tiles_top_1.png')
wood_top_1 = pyg.image.load('data/assets/textures/wood_top_1.png')
road_top_1 = pyg.image.load('data/assets/textures/road_top_1.png')
road_top_2 = pyg.image.load('data/assets/textures/road_top_2.png')
platform_top_tex = [tiles_top_1,
				 wood_top_1,
				 road_top_1,
				 road_top_2]

# Platform Floor Textures
wood_floor_1 = pyg.image.load('data/assets/textures/wood_floor_1.png')
platform_floor_tex = [wood_floor_1]