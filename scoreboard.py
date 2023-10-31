from turtle import Turtle

# file = open('data.txt')
# content = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open('data.txt') as file:

            self.highest_score =  int(file.read())

        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.goto(x=0, y=260)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Eat a food", align='center',font=('Courier', 18, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align='center', font=('Courier', 18, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align='center', font = ('Courier', 24, 'normal'))
    #

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode = 'w') as data:
                data.write(str(self.highest_score))

        self.score = 0
        self.update_score()
