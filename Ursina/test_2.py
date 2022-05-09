from ursina import *

def update():
	global m 

	m += 1
	num_frame = 200
	n = m%num_frame
	if n < num_frame//2:
		cube.y += time.dt
	else:
		cube.y -= time.dt
	# camera.position = (0,0,0)
	cube.texture = "white_cube"

m = 0
cube = Entity(model ="cube",scale=2,color=color.gray,rotation = (45,45,0))

app = Ursina()
app.run()