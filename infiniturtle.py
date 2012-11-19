while 1==1:
	import turtle
	import random
	a = random.randint(1,4)
	if a == 1:
		turtle = turtle.left(90)
	elif a == 2:
		turtle = turtle.right(90)
	else:
		turtle.forward(5)
