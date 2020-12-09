
while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
    elif wall_on_right():
       turn_left()
        