pos_x = 0
pos_y = 0
score = 0
ball = 40

def setup():
    global pos_x
    global pos_y
    global score
    pos_x = random(0, width)
    pos_y = random(0, height)

    size(600, 400)

def draw():
    background(210, 98, 176)
    fill(0)
    ellipse(pos_x, pos_y, ball, ball)
    fill(225, 225, 0)
    textSize(30)
    text(score, 50, 50)

def mousePressed():
    global pos_x
    global pos_y
    global score

    radius = ball / 2.0
    distance_x = abs(mouseX - pos_x)
    distance_y = abs(mouseY - pos_y)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        pos_x = random(0, width)
        pos_y = random(0, height)
        score += 1
