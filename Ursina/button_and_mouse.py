from ursina import *
from random import randint

app = Ursina()

def PrintText():
	print_on_screen("Hello word", position=(randint(-3,3),randint(-3,3)*.1))

def Colors():
	b.color = color.random_color()

b = Button(text="A button",color = color.azure,text_color = color.random_color(),
				scale = .25,icon="sword",
				text_origin=(0.5,0))
b.on_click = PrintText
b.tooltip = Tooltip("Click me")


app.run()


