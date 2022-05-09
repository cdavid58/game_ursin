from ursina import *
from random import randint

# app = Ursina()
# cube = Entity(model = "cube",scale= 2,position = (5,1,3.5),color = color.red)
# text = Text(text="this is a red cube",scale=2)
# app.run()

# def update():
# 	# cube.x = cube.x  + time.dt * 2
# 	red = randint(0,255)
# 	blue = randint(0,255)
# 	green = randint(0,255)
# 	cube.color = color.rgb(red,green,blue)
# 	cube.x += time.dt
# 	cube.rotation_z += time.dt * 100
# 	cube.rotation_x += time.dt * 100
# 	cube.rotation_y += time.dt * 100

def update():
	global speed 
	cube.x += time.dt * speed
	if abs(cube.x) > 3:
		speed *= -1



app = Ursina()
speed = 1
cube = Entity(model = "cube", color=color.red, scale = 2)
app.run()