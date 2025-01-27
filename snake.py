from turtle import Screen, Turtle
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segments = []  # Instance attribute olarak tanımlandı
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)



    def add_segments(self,position):
      #  if
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)
    def snake_longer(self):
        seg_len = len(self.segments)
        last_segment_position = self.segments[seg_len - 1].position()
        self.add_segments(last_segment_position)
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):#(start=,stop=,step=):
           new_x= self.segments[seg_num-1].xcor()
           new_y=self.segments[seg_num-1].ycor()
           self.segments[seg_num].goto(new_x,new_y)

        self.segments[0].forward(20)
       # self.segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

