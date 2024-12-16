def x2_minus3x_plus4(num):
    return (num)**2-3*(num)+4
def ax2_bx_c(a,b,c,num):
    return (a*num**2)+ b*num + c

 # peter = ax2_bx_c(1,1,1,4)

#print(peter)

import turtle
turtle.teleport(0,x2_minus3x_plus4(0))

for i in range(1,30):
                turtle.goto(i, x2_minus3x_plus4(i))
