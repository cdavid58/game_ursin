from ursina import * 

app = Ursina()

# Entity(model="quad",texture="img/pelea",position=(0,0,0),scale=5)
faucet_running = Animation("img/pelea",position=(0,0,0),scale=5,
		fps = 8,loop=True,autoplay = True
)


app.run()