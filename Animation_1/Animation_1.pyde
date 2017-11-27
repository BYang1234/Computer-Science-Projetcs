x = 100
speed = 10
def setup():
    size(400,400)

def draw():
    global x
    global speed
    background(255)
    noStroke
    fill(0,0,150)
    if x >= 400:
        speed = -speed * 0.95
    elif x <= 0:
        speed = -speed * 0.95   
    x += speed
    ellipse(x,100,40,40)
    