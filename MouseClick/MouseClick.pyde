pos_x = 0
pos_y = 0
score = 0

def setup():
    global pos_x
    global pos_y
    
    size(800,400)
    pos_x = random(0,width)
    pos_y = random(0,height)
    
def draw():
    background(143,53,78)
    fill(225,225,0)
    ellipse(pos_x,pos_y,40,40)
    
    fill(223,45,9)
    textSize(40)
    text(score,50,50)
    
def mousePressed():
      global pos_x
      global pos_y
      global score
      pos_x = random(0, width)
      pos_y = random(0, height)
      score += 1
      