from turtle import ht,write,color,pd,pu,goto,circle,begin_fill,end_fill,speed,screensize
import random

ht()
screensize(800,800)

#the leaves
pu()
color("dark green")
begin_fill()
goto(0,-100)
pd()
goto(-225,-100)
goto(-125,-25)
goto(-175,-25)
goto(-75,50)
goto(-125,50)
goto(-25,125)
goto(-75,125)
goto(0,200)
#the other half
goto(75,125)
goto(25,125)
goto(125,50)
goto(75,50)
goto(175,-25)
goto(125,-25)
goto(225,-100)
goto(0,-100)
end_fill()

#the trunk
pu()
color("brown")
begin_fill()
goto(-25,-100)
pd()
goto(-25,-250)
goto(25,-250)
goto(25,-100)
end_fill()

#star
color("yellow")
begin_fill()
pu()
goto(0,200)
pd()
goto(-10,215)
goto(-40,215)
goto(-10,235)
goto(0,265)
goto(10,235)
goto(40,215)
goto(10,215)
goto(0,200)
end_fill()

#words
pu()
goto(30,200)
pd()
color("black")
write("祝段焱轩小朋友圣诞节快乐")

#balls

#number of balls
a=random.randint(4,10)
#colours
l=["red","purple","green","pink","orange","yellow","blue","cyan","gray","maroon"]
#sets of x and y
cx=[-150,-100,-50,0,50,100,150,-90,-50,0,50,90,-40,0,40]
cy=[-75,-75,-75,-75,-75,-75,-75,0,0,0,0,0,75,75,75]

#for each ball
for i in range(a):
    pu()
    #random position
    b=random.randint(0, 14)
    #random colour
    c=random.randint(0, 9)
    color(l[c])
    begin_fill()
    #use index
    y=cy[b]
    x=cx[b]
    goto(x,y)
    pd()
    #circle r=15
    circle(15)
    end_fill()

#generate balls in completely random position
#always goes out of the tree so it's not called
def genballrand():
    for i in range(a):
        pu()
        #random xy
        b=random.randint(0, 9)
        c=random.randint(0, 9)
        color(l[b])
        begin_fill()
        y=b*25-100
        x=c*25-75
        goto(x,y)
        pd()
        circle(15)
        end_fill()
