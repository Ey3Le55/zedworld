'''
Camera Class
'''

from pygame.locals import Rect

SUR_WIDTH = 200 #228
SUR_HEIGHT = 150 #171
HALF_WIDTH = int(SUR_WIDTH / 2)
HALF_HEIGHT = int(SUR_HEIGHT / 4)
MAIN_SURFACE = (SUR_WIDTH, SUR_HEIGHT)

class Camera(object):
	def __init__(self, camera_func, width, height):
		self.camera_func = camera_func
		self.state = Rect(0, 0, width, height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
	l, t, _, _ = target_rect
	_, _, w, h = camera
	return Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
	l, t, _, _ = target_rect
	_, _, w, h = camera
	l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

	l = min(0, l)  # stop scrolling at the left edge
	l = max(-(camera.width - SUR_WIDTH), l)  # stop scrolling at the right edge
	t = max(-(camera.height - SUR_HEIGHT), t)  # stop scrolling at the bottom
	t = min(0, t)  # stop scrolling at the top
	return Rect(l, t, w, h)