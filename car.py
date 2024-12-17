import DrawingPanel

animation_scene = DrawingPanel.DrawingPanel(800,600)
tree_x = 320

car_x = 50 

def car(color,x,y):
    animation_scene.fill_rect(x,y,69,15, color)
    animation_scene.fill_rect(x+15, y-10, 30, 15, color)
    animation_scene.fill_oval(x+7, y+7, 10,10,'black')
    animation_scene.fill_oval(x+52, y+7, 10,10,'black')
def background():
    animation_scene.fill_rect(0,368, 1000, 435, 'green')
    animation_scene.fill_rect(0,0, 800, 368, 'blue')
def tree(x):
    animation_scene.fill_rect(x, 150, 50, 218, 'brown')
    animation_scene.fill_oval(x-20 ,100, 100,100,'green')
def sun(x,y):
        animation_scene.fill_oval(x,y, 60,60,'yellow')
def smoke(x,y):
    animation_scene.fill_oval(270+x, 340+y, 20,20,'grey')
for i in range(681):
    background()
    tree(tree_x)
    sun(50+i ,50-i)
    car('orange' ,car_x + i , 350)
    animation_scene.sleep(10)
    if car_x + i == 251: # car stops at colision
        car(301,350)
        
        
        
    



    


