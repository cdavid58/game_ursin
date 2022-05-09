from ursina import *

# def update():
# 	global dx
# 	e1.x += dx

# 	if abs(e1.x) >= 3:
# 		dx =-dx

app = Ursina()

# e1 = Entity(model = "circle", scale=1, color = color.green,position=(0,-1,0) )
# e2 = Entity(model = "circle", scale=1, color = color.red,position=(0,1,0) )
# e2.add_script(SmoothFollow(target=e1,offset=(0,2,0)))
# dx = .1

def update():
	global dy 
	player.y += dy
	up = False
	if abs(player.y) >= 3.5:
		player.rotation_z = 80
		dy =-dy
	



player =Entity(model="quad",scale =1,x=-4.5,texture="img/head.png")
e=[None]*50
e[0] = Entity(model="circle",scale=.3,color = color.green)
e[0].add_script(SmoothFollow(target=player,offset=(.3,0,0)))
dy = .08
for i in range(1,50):
	e[i] = Entity(model="circle",scale=.3,color = color.green)
	e[i].add_script(SmoothFollow(target=e[i - 1],offset=(.2,0,0)))	

app.run()
