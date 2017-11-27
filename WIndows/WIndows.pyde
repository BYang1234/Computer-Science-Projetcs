def setup():
    size(400, 400)
    
def draw():
    background(255)
    
    # building
    stroke(0)
    strokeWeight(5)
    fill(255)
    rect(125, 50, 150, 300)
    
    # window
    global x
    stroke(0)
    strokeWeight(2)
    fill(128)
    for y in range(63,303,47) and x in range(124,303,10):
        rect(x, y, 30, 40)
        
     