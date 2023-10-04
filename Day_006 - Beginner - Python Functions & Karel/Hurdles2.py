def turn_right():
	turn_left()
	turn_left()
	turn_left()


def jump():
	move()
	turn_left()
	move()
	turn_right()
	move()
	turn_right()
	move()
	turn_left()


def quick_jump():
	turn_left()
	move()
	turn_right()
	move()
	turn_right()
	move()
	turn_left()


while not at_goal():
	while wall_in_front() != True:
		move()
	if wall_in_front() == True:
		quick_jump()
