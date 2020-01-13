import turtle
import random


def key_box():
    turtle.up()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    turtle.forward(250)
    for i in range(0, 4):
        turtle.left(90)
        turtle.forward(500)
    turtle.left(90)
    draw_lines()
    draw_lines()
    turtle.right(90)


def draw_lines():
    for i in range(0, 4):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(500)
        turtle.back(500)
        turtle.right(90)
    turtle.forward(100)
    turtle.left(90)


def move_spaces():
    turtle.up()
    turtle.back(100)
    turtle.down()


def fill_box(color):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    for i in range(0, 4):
        turtle.fd(100)
        turtle.left(90)
    turtle.right(90)
    turtle.end_fill()


def next_line():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)


def main():
    turtle.tracer(0)
    key_box()

    fill_box("blue")
    move_spaces()
    fill_box("#e1df9d")
    move_spaces()
    fill_box("blue")
    move_spaces()
    fill_box("red")
    move_spaces()
    fill_box("red")
    move_spaces()
    next_line()

    fill_box("red")
    move_spaces()
    fill_box("blue")
    move_spaces()
    fill_box("red")
    move_spaces()
    fill_box("red")
    move_spaces()
    fill_box("blue")
    move_spaces()
    next_line()

    fill_box("#e1df9d")
    move_spaces()
    fill_box("blue")
    move_spaces()
    fill_box("black")
    move_spaces()
    fill_box("#e1df9d")
    move_spaces()
    fill_box("#e1df9d")
    move_spaces()
    next_line()

    fill_box("blue")
    move_spaces()
    fill_box("red")
    move_spaces()
    fill_box("#e1df9d")
    move_spaces()
    fill_box("blue")
    move_spaces()
    fill_box("red")
    move_spaces()
    next_line()

    fill_box("blue")
    move_spaces()
    fill_box("#e1df9d")
    move_spaces()
    fill_box("blue")
    move_spaces()
    fill_box("red")
    move_spaces()
    fill_box("#e1df9d")
    move_spaces()
    next_line()

    # for i in range(0, 5):
    #     fill_box()
    #     move_spaces()

    turtle.done()


if __name__ == '__main__':
    main()
