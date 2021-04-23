import turtle
import time
import random

WIDTH, HEIGHT = 900, 700
COLORS = ['hotpink', 'greenyellow', 'deeppink', 'aqua', 'gold', 'dimgray', 'blueviolet', 'lime', 'royalblue', 'orangered', 'coral' , 'orange' , 'magenta' , 'deepskyblue' , 'chocolate' , 'crimson']

def get_number_of_racers():
	racers = 0
	while True:
		racers = input('Please Enter the number of racers (2 - 16): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print(' Try Again with the correct input (numeric)!')
			continue

		if 2 <= racers <= 16:
			return racers
		else:
			print('Try Again with the correct input range (2 - 16)!')

# turtle movement forward in the race and return the winner
def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 10)
			racer.forward(distance)
#
			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]


#racer moving methods for the game
def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.shapesize(2,2,4)
		racer.left(90)
		#set the racer's position on the screen getting x and y values
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.penup()
		turtles.append(racer)

	return turtles

# Setting up screen for the game
def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Welcome to the turtle race!')
	screen.bgcolor("#FFF7FA")

racers = get_number_of_racers()
init_turtle()

#randermize the racers in the game
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(10)


