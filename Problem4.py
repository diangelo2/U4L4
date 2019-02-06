from turtle import *

bob = Turtle()
pop = Turtle()

bob.color("blue")
bob.pensize(5)
bob.speed(5)
bob.shape("turtle")

pop.color("green")
pop.pensize(5)
pop.speed(5)
pop.shape("turtle")

for x in range(1):
	bob.circle(100)

for y in range(3):
	pop.forward(100)
	pop.left(120)

mainloop()