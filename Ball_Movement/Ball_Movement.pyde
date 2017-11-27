x = 50
y = 50
xSpeed = 0
ySpeed = 0

def setup():
    global x
    global y
    global xSpeed 
    global ySpeed
    size(600,600)
    background(134,154,155)   
    
    
    ellipse(x,y,30,30)
    xSpeed += 10
    x += xSpeed
    ellipse(x,y,30,30)

