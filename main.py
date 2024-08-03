from turtle import Screen
from snake import Snake
from  food import  Food
from  scoreboard import Scoreboard
import time

#create the board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakesss")
screen.tracer(0)

#create the snake, food particle and the scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#move the snake using direction keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#have the snake moving continously
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #Increase this value if you want to slow down yowr snake
    snake.move()

    # detect collission with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
