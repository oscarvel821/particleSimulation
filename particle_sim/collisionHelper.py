def circle_sweep_and_prune(circles) -> None:
    possible_collision = []
    #sorting by the x axis
    sorted_list = sorted(circles, key=lambda circles : circles.x)
    active = []

    active.append(sorted_list[0])

    for i in range(1, len(sorted_list)):
        next_circle = sorted_list[i]
        flag = False

        for circle in active:

            if not (next_circle.x - next_circle.radius > circle.x + circle.radius):
                possible_collision.append([circle, next_circle])
                flag = True

        if flag:
            active.append(next_circle)
        else:
            active = [next_circle]

    return possible_collision




