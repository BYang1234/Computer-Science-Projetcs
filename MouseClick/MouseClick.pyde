pos_x_1 = 0
pos_y_1 = 0
pos_x_2 = 0
pos_y_2 = 0
score_1 = 0
score_2 = 0
winner = None


def setup():
    global pos_x_1
    global pos_y_1
    global score_1
    global score_2
    global pos_x_2
    global pos_x_2
    
    pos_x_1 = random(0, width/2)
    pos_y_1 = random(0, height)
    pos_x_2 = random(width/2, width)
    pos_y_2 = random(0,height)

    size(600, 400)

def draw():
    background(210, 98, 176)
    fill(128,90,178)
    rect(0,0,width/2,height)
    fill(0)
    ellipse(pos_x_1, pos_y_1, 40, 40)
    fill(12,75,68)
    ellipse(pos_x_2, pos_y_2, 40 ,40)
    fill(225, 225, 0)
    textSize(30)
    text(score_1, 50, 50)
    fill(225,225,0)
    textSize(30)
    text(score_2, 350,50)

def mousePressed():
    global pos_x_1
    global pos_y_1
    global score_1
    global pos_x_2
    global pos_y_2
    global score_2
    global winner

#Player 1
    radius = 40 / 2.0
    distance_x_1 = abs(mouseX - pos_x_1)
    distance_y_1 = abs(mouseY - pos_y_1)
    hypotenuse = sqrt(distance_x_1 ** 2 + distance_y_1 ** 2)

    if hypotenuse <= radius:
        pos_x_1 = random(0, width/2)
        pos_y_1 = random(0, height)
        score_1 += 1     
#Player 2        
    radius = 40 / 2.0
    distance_x_2 = abs(mouseX - pos_x_2)
    distance_y_2 = abs(mouseY - pos_y_2)
    hypotenuse = sqrt(distance_x_2 ** 2 + distance_y_2 ** 2)
    
    if hypotenuse <= radius:
        pos_x_2 = random(width/2,width)
        pos_y_2 = random(0,height)
        score_2 += 1
        
    if winner == None:
        if score_1 == 10:
            winner = "Player 1"
        elif score_2 == 10:
            winner = "Player 2"
    