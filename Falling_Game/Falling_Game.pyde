pos = PVector(200,0)
speed = PVector(0,0)
pos_player = PVector(200,585)

def setup():
    size(400,600)
    speed.y = random(0,10)
    speed.x = random(0,5)

    
def draw():
    global pos
    global pos_player
    global score
    background(236,126,30)
    noStroke
#Falling Ball    
    fill(225,225,0)
    ellipse(pos.x,pos.y,40,40)
    pos.y += speed.y
    pos.x += speed.x

    if pos.x >= 385:
        speed.x = -speed.x
    elif pos.x <= 15:
        speed.x = -speed.x
    if pos.y >= 600:
        ellipse(200,0,40,40)    
    
#Player
    fill(255,102,255)
    ellipse(pos_player.x, pos_player.y, 30,30)
    pos_player.x = mouseX
    
    distance_1 = abs(pos.x - pos_player.x)
    distance_2 = abs(pos.y - pos_player.y)
    hypotenuse = sqrt(distance_1 ** 2 + distance_2 ** 2)
    
    if hypotenuse >= 0:
        ellipse(pos.x, pos.y, 40, 40)
            
    