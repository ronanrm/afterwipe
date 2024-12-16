import DrawingPanel

panel = DrawingPanel.DrawingPanel(400,400)

#for i in range(5):
    #panel.draw_oval(0,0, 125-6*i, 125-6*i)

# for i in range (10)
    #panel.draw_rect(10, 10+10*i,  110-10*i, 10)

#panel.stroke_width = 5
#panel.draw_rect(100,100,100,50, "black")
#panel.fill_rect(100,100,100,50, "blue")
for i in range(50):
    # panel.draw_oval(0+8*i,0+8*i,50,50,'red')
    panel.fill_oval(10+8*i, 10+8*i, 50,50, 'red')
    panel.fill_rect(0,0,400,400,'white')
    



