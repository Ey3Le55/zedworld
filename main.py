'''
Main Loop
'''

import pygame as pyg
import random as r
from pygame import Surface, Color
from pygame.locals import *
from data.lib.Player import Player
from data.lib.Bullet import Bullet
from data.lib.Camera import *
from data.lib.Level import Level
from data.lib.Enemy import Enemy
from data.config import *
from data.levels import *
from data.assets.textures.Textures import *
from data.assets.fonts.Fonts import *

pyg.init()
GLOBAL_QUIT = False

SCREEN = pyg.display.set_mode(DISPLAY)

CURRENT_LEVEL = level2

# initialize font
font = pyg.font.SysFont('Helvetica', 32)

timer = pyg.time.Clock()

# Main Menu
def main_menu():
	global GLOBAL_QUIT
	main_surface = Surface(MAIN_SURFACE)
	pyg.display.set_caption("ZedWorld")
	RUNNING = True

	while RUNNING:
		for event in pyg.event.get():
			if event.type == QUIT:
				RUNNING = False
				GLOBAL_QUIT = True
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				RUNNING = False
				GLOBAL_QUIT = True
			if event.type == KEYDOWN and event.key == K_UP:
				UP = True
			if event.type == KEYDOWN and event.key == K_DOWN:
				DOWN = True
			if event.type == KEYDOWN and event.key == K_LEFT:
				pass
			if event.type == KEYDOWN and event.key == K_RIGHT:
				pass
			if event.type == KEYUP and event.key == K_UP:
				UP = False
			if event.type == KEYUP and event.key == K_DOWN:
				DOWN = False
			if event.type == KEYUP and event.key == K_RIGHT:
				pass
			if event.type == KEYUP and event.key == K_LEFT:
				pass

		main_surface.blit()

		pyg.transform.scale(main_surface, DISPLAY, SCREEN)

# FPS Screen
def show_fps(true):
	if true == True:
		fps = font.render("FPS: {0}".format(str(int(timer.get_fps()))), True, pyg.Color('white'))
		fpsRect = fps.get_rect()
		fpsRect.midtop = (80, 10)
		SCREEN.blit(fps, fpsRect)

# Main loop
def main(current_level, level_name):
	global GLOBAL_QUIT
	global CURRENT_LEVEL
	main_surface = Surface(MAIN_SURFACE)
	pyg.display.set_caption("ZedWorld: " + level_name)

	level = Level(current_level)
	level.init()

	#Player globals
	UP = DOWN = LEFT = RIGHT = SHOOT = False
	HP = 5
	POWER_UP = None
	SPAWN = level.spawn
	PLAYER = Player(SPAWN)
	enemies = []
	bullets = []

	#Background color
	bg = Surface((16, 16))
	bg.convert()
	bg.fill(Color("#455a64"))

	total_level_width = len(level.level[0]) * 16
	total_level_height = len(level.level) * 16

	camera = Camera(complex_camera, total_level_width, total_level_height)
	level.entities.add(PLAYER)

	RUNNING = True

	fps_pressed = 0
	showFps = False

	pyg.key.set_repeat(150,100)

	while RUNNING:

		for event in pyg.event.get():
			if event.type == QUIT:
				RUNNING = False
				GLOBAL_QUIT = True
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				RUNNING = False
				GLOBAL_QUIT = True  # Temp
			if event.type == KEYDOWN and event.key == K_UP:
				UP = True
			if event.type == KEYDOWN and event.key == K_DOWN:
				DOWN = True
			if event.type == KEYDOWN and event.key == K_LEFT:
				LEFT = True
			if event.type == KEYDOWN and event.key == K_RIGHT:
				RIGHT = True
			if event.type == KEYDOWN and event.key == K_z:
				SHOOT = True
				bullets.append(Bullet((PLAYER.rect.x, PLAYER.rect.y), PLAYER))
				level.entities.add(bullets[len(bullets) - 1])
			if event.type == KEYDOWN and event.key == K_F3:
				fps_pressed += 1
				if fps_pressed == 1:
					if not showFps:
						showFps = True
					else:
						showFps = False
			if event.type == KEYUP and event.key == K_F3:
				fps_pressed = 0
			if event.type == KEYUP and event.key == K_UP:
				UP = False
			if event.type == KEYUP and event.key == K_DOWN:
				DOWN = False
			if event.type == KEYUP and event.key == K_RIGHT:
				RIGHT = False
			if event.type == KEYUP and event.key == K_LEFT:
				LEFT = False
			if event.type == KEYUP and event.key == K_z:
				SHOOT = False
			# DEBUG
			if event.type == KEYDOWN and event.key == K_1:
				CURRENT_LEVEL = test1
				RUNNING = False
			if event.type == KEYDOWN and event.key == K_2:
				CURRENT_LEVEL = level2
				RUNNING = False
			if event.type == KEYDOWN and event.key == K_0:
				for spawn in level.zspawn:
					enemies.append(Enemy(spawn))
					level.entities.add(enemies[len(enemies)-1])

		# draw background
		for y in range(20):
			for x in range(20):
				main_surface.blit(bg, (x * 16, y * 16))

		# update camera
		camera.update(PLAYER)

		# update player, draw everything else
		if HP != 0:
			PLAYER.update(UP, DOWN, LEFT, RIGHT, level.platforms, SHOOT, POWER_UP)

		for enemy in enemies:
			enemy.move_towards_player(PLAYER)
			enemy.update(level.platforms)

		for i in range(0,len(bullets)):
			if bullets[i].destroyed:
				level.entities.remove(bullets[i])
			else:
				bullets[i].update(level.platforms)

		# draw entities of level
		for e in level.entities:
			main_surface.blit(e.image, camera.apply(e))

		pyg.transform.scale(main_surface, DISPLAY, SCREEN)

		# fps counter
		show_fps(showFps)
		pyg.display.flip()
		timer.tick(60)

#main_menu()
while not GLOBAL_QUIT:
	main(CURRENT_LEVEL.level, CURRENT_LEVEL.name)
