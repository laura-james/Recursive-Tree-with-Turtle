from turtle import *



def tree(levels, trunkLen, angle, shrinkFactor):
    if levels > 0:
        color(0+(levels)*12,0,0+(levels)*12)
        width(levels)
        fd(trunkLen)
        rt(angle)
        tree(levels-1, trunkLen*shrinkFactor, angle, shrinkFactor)
        lt(2*angle)
        tree(levels-1, trunkLen*shrinkFactor, angle, shrinkFactor)
        rt(angle)
        bk(trunkLen)
speed(100)
#https://stackoverflow.com/questions/56528067/how-can-i-change-the-size-of-my-python-turtle-window
setup(800,800) 
colormode(255)
tracer(0)
lt(90)
pu()
goto(0,-200)
pd()


tree(12,70,23,0.9)

update()
done()
