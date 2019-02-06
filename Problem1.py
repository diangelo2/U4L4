from turtle import *

bob = Turtle()

bob.color("blue")
bob.pensize(5)
bob.speed(5)
bob.shape("turtle")

for x in range(1):
	bob.forward(80)
	bob.left(50)
	bob.forward(200)
	bob.right(150)
	bob.forward(50)
	bob.circle(25)
	bob.backward(300)

mainloop()