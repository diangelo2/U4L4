from turtle import *

screen = Screen()
screen.bgcolor("green")

bob = Turtle()

bob.color("yellow")
bob.pensize(2)
bob.speed(0)
bob.shape("turtle")

for x in range(10):
	bob.forward(15)
	bob.left(10)
	bob.backward(15)
	bob.left(10)

mainloop()