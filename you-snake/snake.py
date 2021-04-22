from turtle import Turtle
INITIAL_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
class Snake:
    def __init__(self):
        self.segs = []
        self.create_snake()
    
    def create_snake(self):
        for coordinate in INITIAL_POSITIONS:
            seg = Turtle("square")
            seg.color("azure")
            seg.penup()
            seg.goto(coordinate)
            self.segs.append(seg)
            
    def move(self):
        for seg_num in range(len(self.segs)-1, 0, -1):
            # the algorithm to follow/got to the preceding segment's latest coordinate
            new_x = self.segs[seg_num-1].xcor()
            new_y = self.segs[seg_num-1].ycor()
            self.segs[seg_num].goto(new_x, new_y)
        
        # updates the head position
        head = self.segs[0]
        head.forward(MOVE_STEP)
    
    def up(self):
        self.segs[0].setheading(90)
    def down(self):
        self.segs[0].setheading(270)
    def right(self):
        self.segs[0].setheading(0)
    def left(self):
        self.segs[0].setheading(180)
        