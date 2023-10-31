from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
food = Food()
score = Scoreboard()
screen = Screen()

screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    #detect collision

    if snake.head.distance(food) < 15:
        print('omnom')
        food.new_location()
        snake.extend()
        score.increase()

    #detect collision with the wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        # game_is_on = False
        score.reset()
        snake.reset()
    #detect collision with the tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset()
            snake.reset()

    snake.move()
























screen.exitonclick()