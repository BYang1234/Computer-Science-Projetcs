#Bryan
x = 100
speed = 0.75
y = 355
def setup():
    size(400,400)
def draw():
    global x
    global speed
    global y 
    background(253,37,11)
    noStroke
    fill(255,255,102)
    ellipse(200,y,300,300)
    fill(225)
    ellipse(x,250,400,50)
    fill(225)
    ellipse(x,100,350,25)
    if x >= 100:
        speed = speed
        x += speed
        y += 0.25
   
    
