from ursina import *
from random import randint

class Player(Entity):
	def __init__(self,x,speed,texture,rotation):
		super().__init__()
		self.model = "cube"
		self.color = color.random_color()
		self.scale_y = 2
		self.x = x
		self.speed = speed
		self.texture = texture
		self.rotation = rotation

	def update(self):
		self.x += held_keys['right arrow'] * time.dt * self.speed
		self.x-=held_keys['left arrow'] * time.dt * self.speed
		print(self.model)

	def input(self,key):
		if key == "space":
			self.color = color.random_color()
		if key == "0":
			Player.reset(self)

	def reset(self):
		self.color = color.random_color()
		self.rotation_z = 0
		self.x = x



app = Ursina()
x =-2
speed = 10
player = Player(x,speed,'brick',(40,2,2))

app.run()
