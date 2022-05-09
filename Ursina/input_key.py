from ursina import *
from random import randint

def update():
	global speed
	cube.texture="white_cube"
	if held_keys['w']:
		cube.z += time.dt * speed
	elif held_keys['s']:
		cube.z -= time.dt * speed
	elif held_keys['a']:
		cube.x -= time.dt * 25
	elif held_keys['d']:
		cube.x += time.dt * 25
	elif held_keys['q']:
		cube.rotation_y -= time.dt * speed
	elif held_keys['e']:
		cube.rotation_y += time.dt * speed




cube = Entity(model = "cube", color=color.green,rotation=(50,50,0))
speed = 100
app = Ursina()
app.run()

