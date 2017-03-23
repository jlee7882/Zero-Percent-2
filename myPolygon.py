def polygon( t ,side, distance):
    angle = 360 / side
    t.begin_fill()
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    t.end_fill()
