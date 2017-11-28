pos = PVector(50,50)
speed = PVector(3,2)

def setup():
    frameRate(60)
    size(600, 600)
    background(255)
    
def draw():
    global pos
    global speed
    
    pos.add(speed)
    
    if pos.x > width:
        pos.x = width
        speed.x = -speed.x
    elif pos.x < 0:
        pos.x = 0
        speed.x = -speed.x
        
    if pos.y > height:
        pos.y = height
        speed.y = -speed.y
    elif pos.y < 0 :
        pos.y = 0
        speed.y = -speed.y
        
    background(255)
    ellipse(pos.x, pos.y, 30, 30)
