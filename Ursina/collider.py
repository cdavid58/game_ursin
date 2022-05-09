from ursina import * 

def update():
	global dx
	box_1.texture = "brick"
	box_2.texture = "brick"
	ball.x += time.dt + dx
	hit_info = ball.intersects()
	if hit_info.hit:
		dx =-dx
		print(hit_info.entity)
		if hit_info.entity in boxes:
			destroy(hit_info.entity)


dx = .05
boxes = []
ball = Entity(model="sphere",color = color.white,scale = .5, position= (0,0,0),collider = "box")
box_1 = Entity(model = "cube",color = color.cyan,texture="white_cube",scale=(2,4,2),position=(4,0,0),collider="box")
box_2 = duplicate(box_1,x=-4)
boxes.append(box_1)
boxes.append(box_2)
app = Ursina()
app.run()


