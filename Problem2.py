from turtle import *

bob = Turtle()

bob.color("purple")
bob.pensize(5)
bob.speed(5)
bob.shape("turtle")

for x in range(4):
	bob.forward(100)
	bob.left(90)

mainloop()