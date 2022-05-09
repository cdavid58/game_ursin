from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math

app = Ursina()

def input(key):
	global bullets
	if key == "space":
		bullet = Bullet()
		bullets.append(bullet)


def update():
	global bullets
	player.rotation_z += held_keys['right arrow'] * player.d_angle
	player.rotation_z -= held_keys['left arrow'] * player.d_angle
	for bullet in bullets:
		bullet.x +=time.dt* bullet.dx
		bullet.y +=time.dt*bullet.dy


class Bullet(Entity):
	def __init__(self):
		super().__init__()
		self.parent = camera.ui
		self.model = "quad"
		self.color = color.green
		self.scale = (.02,.1)
		self.position = (0,0)
		self.z = player.z +.01
		self.rotation_z = player.rotation_z
		self.dx =.8*math.sin(player.rotation_z/180*math.pi)
		self.dy =.8*math.cos(player.rotation_z/180*math.pi)

class Player(Entity):
	def __init__(self):
		super().__init__()
		self.parent = camera.ui
		self.model = "cube"
		self.scale = (.02,.1)
		self.texture = "white_cube"
		self.position = (0,0)
		self.d_angle = 2

ground = Entity(model = 'plane',)

Sky()
player = Player()
bullets = []
app.run()   