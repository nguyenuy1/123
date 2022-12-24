for i in range(5):  
    forward(n / 5)
    right(144)  
    forward(n / 5)
    left(72)  
end_fill()
right(126)


def drawlight():  
    if r.randint(0, 30) == 0:  
        color('tomato')  
        circle(6)  
    elif r.randint(0, 30) == 1:
        color('orange')  
        circle(3)  
    else:
        color('dark green')  


color("dark green")  
backward(n * 4.8)


def tree(d, s): 
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


#tree(15, n)
backward(n / 2)

for i in range(200):  
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)
