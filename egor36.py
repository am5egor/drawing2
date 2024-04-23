from turtle import *

speed(100)

def crug(x,y, radius, letter):
    color('black')
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    goto(x-50,y-5)
    pendown()
    write(letter, font=('Arial', 12, 'bold'))


def sqr(x,y, colour):
    global i
    penup()
    goto(x,y)
    pendown()
    color('black', colour)
    begin_fill()
    for j in range(4):
        forward(30)
        left(90)
    end_fill()
    color('white')
    penup()
    goto(x + 10,y - 0)
    pendown()
    if i == 9:
        i = -1
    write(i+1, font=('Arial', 17, 'bold'))

colors = ['yellow', 'green', 'blue', 'red', 'pink', 'purple', 'skyblue', 'brown', 'orange', 'black']

x = -200
for i in range(10):
    sqr(x,200, colors[i])
    x += 40




color('black')
penup()
goto(-200,170)
pendown()
write('заливка: z, x', font=('Arial', 17, 'bold'))

penup()
goto(-200, 140)
pendown()
write('ластик: c', font=('Arial', 17, 'bold'))

penup()
goto(270, 90)
pendown()
forward(90)
penup()
goto(270, 60)
pendown()
write('сейчас: A', font=('Arial', 17, 'bold'))

letters = ['A', 'S', 'D', 'F', 'G']


y = 110
radius = 3
for i in range(5):
    crug(310,y, radius, letters[i])

    radius += 2
    y += 20

color('black') 
penup()
goto(240,-195)
pendown()
begin_fill()
circle(5)
end_fill()
penup()
goto(240,-190)
pendown()

def strela():
    pensize(3)
    right(90)
    penup()
    forward(10)
    pendown()
    forward(30)
    left(120)
    forward(5)
    left(180)
    forward(5)
    right(60)
    forward(5)

for i in range(4):
    strela()
    left(120)
    penup()
    goto(240,-190)
    pendown()


penup()
goto(175,-140)
pendown()
write('Управление стрелками', font=('Arial', 10, 'bold'))



def move(x,y):
    Dobbi.penup()
    Dobbi.goto(x,y)
    Dobbi.pendown()

def move_left():
    Dobbi.goto(Dobbi.xcor()-5, Dobbi.ycor())

def move_right():
    Dobbi.goto(Dobbi.xcor()+5, Dobbi.ycor())

def move_up():
    Dobbi.goto(Dobbi.xcor(), Dobbi.ycor()+5)

def move_down():
    Dobbi.goto(Dobbi.xcor(), Dobbi.ycor()-5)

def p_col1():
    Dobbi.color('yellow')

def p_col2():
    Dobbi.color('green')

def p_col3():
    Dobbi.color('blue')

def p_col4():
    Dobbi.color('red')

def p_col5():
    Dobbi.color('pink')

def p_col6():
    Dobbi.color('purple')

def p_col7():
    Dobbi.color('skyblue')

def p_col8():
    Dobbi.color('brown')

def p_col9():
    Dobbi.color('orange')

def p_col0():
    Dobbi.color('black')

def s_col1():
    scr.bgcolor('yellow')

def s_col2():
    scr.bgcolor('green')

def s_col3():
    scr.bgcolor('blue')

def s_col4():
    scr.bgcolor('red')

def s_col5():
    scr.bgcolor('pink')

def s_col6():
    scr.bgcolor('purple')

def s_col7():
    scr.bgcolor('skyblue')

def s_col8():
    scr.bgcolor('brown')

def s_col9():
    scr.bgcolor('orange')

def s_col0():
    scr.bgcolor('black')



Dobbi = Turtle()

Dobbi.shape('circle')
Dobbi.pensize(2)

scr = Dobbi.getscreen()
scr.listen()

scr.onscreenclick(move)
scr.onkey(move_left, 'Left')
scr.onkey(move_right, 'Right')
scr.onkey(move_up, 'Up')
scr.onkey(move_down, 'Down')

choise = 'pen'

def bruh():
    scr.onkey(None, '1')
    scr.onkey(None, '2')
    scr.onkey(None, '3')
    scr.onkey(None, '4')
    scr.onkey(None, '5')
    scr.onkey(None, '6')
    scr.onkey(None, '7')
    scr.onkey(None, '8')
    scr.onkey(None, '9')
    scr.onkey(None, '0')
    scr.onkey(None, 'q')

    print('a')

    scr.onkey(p_col1, '1')
    scr.onkey(p_col2, '2')
    scr.onkey(p_col3, '3')
    scr.onkey(p_col4, '4')
    scr.onkey(p_col5, '5')
    scr.onkey(p_col6, '6')
    scr.onkey(p_col7, '7')
    scr.onkey(p_col8, '8')
    scr.onkey(p_col9, '9')
    scr.onkey(p_col0, '0')
    scr.onkey(both, 'q')
    scr.onkey(choise_beckground, 'r')

def background():
    scr.onkey(None, '1')
    scr.onkey(None, '2')
    scr.onkey(None, '3')
    scr.onkey(None, '4')
    scr.onkey(None, '5')
    scr.onkey(None, '6')
    scr.onkey(None, '7')
    scr.onkey(None, '8')
    scr.onkey(None, '9')
    scr.onkey(None, '0')
    scr.onkey(None, 'q')

    print('b')

    scr.onkey(s_col1, '1')
    scr.onkey(s_col2, '2')
    scr.onkey(s_col3, '3')
    scr.onkey(s_col4, '4')
    scr.onkey(s_col5, '5')
    scr.onkey(s_col6, '6')
    scr.onkey(s_col7, '7')
    scr.onkey(s_col8, '8')
    scr.onkey(s_col9, '9')
    scr.onkey(s_col0, '0')
    scr.onkey(both, 'q')
    scr.onkey(choise_bruh, 'e')

def choise_bruh():
    global choise
    choise = 'pen'

def choise_beckground():
    global choise
    choise = 'scr'


def both():
    if choise == 'pen':
        bruh()
    else:
        background()




def p_radius1():
    Dobbi.pensize(1)

def p_radius2():
    Dobbi.pensize(5)

def p_radius3():
    Dobbi.pensize(10)

def p_radius4():
    Dobbi.pensize(15)

def p_radius5():
    Dobbi.pensize(20)

scr.onkey(p_radius1, 'a')
scr.onkey(p_radius2, 's')
scr.onkey(p_radius3, 'd')
scr.onkey(p_radius4, 'f')
scr.onkey(p_radius5, 'g')

def begin_fill():
    Dobbi.begin_fill()

def end_fill():
    Dobbi.end_fill()

scr.onkey(begin_fill, 'z')
scr.onkey(end_fill, 'x')

def cleare():
    Dobbi.clear()

scr.onkey(cleare, 'c')

both()

done()