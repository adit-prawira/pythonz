from turtle import Turtle
INITIAL_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT= 180
class Snake:
    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]
    
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
        self.head.forward(MOVE_STEP)
        
    def valid_heading(self, direction, opposite):
        if(self.head.heading() != opposite):
            self.head.setheading(direction)
    
    def up(self):
        self.valid_heading(direction = UP, opposite = DOWN)
    def down(self):
        self.valid_heading(direction = DOWN, opposite = UP)
    def right(self):
        self.valid_heading(direction = RIGHT, opposite = LEFT)
    def left(self):
        self.valid_heading(direction = LEFT, opposite = RIGHT)
    
    def grow(self):
        tail_post =len(self.segs)-1
        tail = self.segs[tail_post]
        new_x = tail.xcor()
        new_y = tail.ycor()
        
        seg = Turtle("square")
        seg.color("azure")
        seg.penup()
        seg.goto(new_x, new_y)
        self.segs.append(seg)