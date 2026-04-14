from turtle import *
tracer(0)
screensize(2000, 2000)
rt(315)
k = 20
for i in range(7):
    fd(12*k)
    rt(45)
    fd(6*k)
    rt(135)

up()
for x in range(-50 , 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')



update()
done()
#40