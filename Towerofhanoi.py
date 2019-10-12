def move(f, t):
    print("Move disc from {} to {}!".format(f,t))

def moveVia(f, t, v):
    move(f, v)
    move(v,t)

def hanoi(n, h, t, f):
    if n == 0:
        pass
    else:
        hanoi((n-1), f, t, h)
        move(f, t)
        hanoi((n-1), h, f, t)

hanoi(4, "B", "C", "A")
