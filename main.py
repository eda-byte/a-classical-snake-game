from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("My Snake Game.")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on= True
possibilities=[]
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.score_writer()

    #detect collision with food
    head_x = snake.head.xcor()  # Get the x-coordinate of the snake's head
    head_y = snake.head.ycor()  # Get the y-coordinate of the snake's head

    if -299 <= head_x <= 299 and -299 <= head_y <= 299:
# and snake.head.distance(snake.segments)>=20

       # last_segment = self.segments[seg_len - 1]

       if snake.head.distance(food)<15:
            #food.hideturtle()
             #score.score_table()
            ##score.score_writer()
            food.refresh()
            score.clear()
            score.increase_score()
            snake.snake_longer()
            #len_seg=int(snake.segments[len(snake.segments)-1])
            #snake.snake_longer(len_seg-1)

       for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on=False
                score.the_end()



    else:
        score.clear()
        score.the_end()
        break

    #detect snake collison


screen.exitonclick()
