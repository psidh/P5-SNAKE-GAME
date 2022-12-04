from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
# ___________________________________________________

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game International")
screen.tracer(0)
starting_position = [(00,0), (-20,0), (-40,0)]


# ___________________________________________________

snake = Snake()  #  Calling the class Snake
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# ___________________________________________________

on = True
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision

    if snake.head.distance(food) < 15:

        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # detect collision with wall

    if snake.head.xcor() > 280 or     snake.head.xcor() < -280     or snake.head.ycor() > 280     or snake.head.ycor() < -280 :
        on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            on = False
            scoreboard.game_over()


# ____ _________________________________________________




screen.exitonclick()