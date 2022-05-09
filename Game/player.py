from ursina import *


class Player(Entity):
	def __init__(self,texture,hp,mana,position):
		super().__init__()
		self.model = "cube"
		self.texture = texture
		self.hp = hp
		self.mana = mana
		self.coin = 0
		self.position = position


