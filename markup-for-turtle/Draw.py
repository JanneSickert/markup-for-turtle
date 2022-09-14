import turtle

# Bsp: 155, 'red'
def rectangle(a, border_color):
    t = turtle.Turtle()
    t.penup()
    t.left(90)
    t.forward(int(a/2))
    t.left(90)
    t.forward(int(a/2))
    t.left(180)
    t.pendown()
    t.color(border_color)
    for i in range(4):
        t.forward(a)
        t.right(90)

# Bsp: 150, 'blue'
def rectangle_with_color(a, fill_color_value):
    t = turtle.Turtle()
    t.penup()
    t.left(90)
    t.forward(int(a/2))
    t.left(90)
    t.forward(int(a/2))
    t.left(180)
    t.pendown()
    t.fillcolor(fill_color_value)
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.right(90)
    t.end_fill()

# Bsp: 300, '#F0F'
def circle(r, border_color):
    t = turtle.Turtle()
    t.penup()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.pendown()
    t.color(border_color)
    t.circle(r)

# Bsp: 50, '#FF0'
def circle_with_color(r, fill_color_value):
    t = turtle.Turtle()
    t.penup()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.pendown()
    t.fillcolor(fill_color_value)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def two_colors_circle(r, fill, border):
    circle(r, border)
    r -= 1
    circle(r, border)
    r -= 1
    circle(r, border)
    r -= 1
    circle_with_color(r, fill)

def two_colors_rechteck(r, fill, border):
    rectangle(r, border)
    r -= 1
    rectangle(r, border)
    r -= 1
    rectangle(r, border)
    r -= 1
    rectangle_with_color(r, fill)