from turtle import Turtle
import turtle
import random
from config import *


class Blocks(Turtle):

    def __init__(self):
        super().__init__()

        self.all_blocks = []
        self.shape(BLOCK_SHAPE)
        self.reset()

    def reset(self):   
        self.clear()
        for row in range(ROW):
            if row <= 1:
                color = BLOCK_COLOR_G[-1]
                point = 7
            elif 1 < row <= 3:
                color = BLOCK_COLOR_G[-2]
                point = 5
            elif 3 < row <= 5:
                color = BLOCK_COLOR_G[-3]
                point = 3
            elif 5 < row <= 7:
                color = BLOCK_COLOR_G[-4]
                point = 1

            for col in range(COL):
                brick = Turtle()
                brick.shape("square")
                brick.penup()
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.color(color)
                
                x_loc = -int(SCREEN_W / 2) + int(BLOCK_SIZE * 3 / 2 + PAD) + int(col * (BLOCK_SIZE * 3 + PAD))
                y_loc = BLOCK_TOP_LINE - int(row * (BLOCK_SIZE + PAD))
                brick.goto(x_loc, y_loc)

                item = {
                    'row': row,
                    'col': col, 
                    'brick': brick, 
                    'color':color, 
                    'point': point,
                    'x_from': int(x_loc - BLOCK_SIZE * 3 / 2 - PAD), 
                    'x_to': int(x_loc + BLOCK_SIZE * 3 / 2), 
                    'yline': int(y_loc - BLOCK_SIZE / 2)
                    }

                self.all_blocks.append(item)
    
    def clear_blocks(self):
        for block in self.all_blocks:
            block['brick'].hideturtle()
            # block['brick'].goto(1000, 1000)
        self.all_blocks = []


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.lives = 3 
        self.score = 0 
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(LIVES_POS)
        self.write(f"Lives: {self.lives}/3", align=ALIGNMENT, font=(FONT, FONT_SIZE[0], FONT_MODE))
        self.goto(SCORE_POS)
        self.write(f"| Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE[0], FONT_MODE))
        
    def count_lives(self):
        self.lives -= 1
        self.update_scoreboard()
        
    def count_point(self, point):   
        self.score += point
        self.update_scoreboard()
    
    def reset(self):
        self.lives = 3 
        self.score = 0 
        self.update_scoreboard()


class Buttons(Turtle):
    def __init__(self, text, color, xloc, yloc, fun):
        super().__init__()

        self.text = text
        self.x = xloc
        self.y = yloc
        self.fun = fun

        self.hideturtle()
        self.color(color)
        self.penup()
        self.lives = 3 
        self.score = 0 
        self.show_btn()
        turtle.onscreenclick(self.btnclick)
    
    def show_btn(self):
        self.goto(self.x, self.y)
        self.write(self.text, align=ALIGNMENT, font=BTN_FONT)
    
    def hide_btn(self):
        self.clear()
        
    def btnclick(self, xloc, yloc):
        if (self.x - 100 < xloc < self.x + 100) and (self.y - 20 < yloc < self.y + 20):
            self.hide_btn()
            self.fun()


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.up()
        self.hideturtle()
        self.goto(0, 100)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=1) 
        self.speed(0)
        self.penup()
        self.reset_position()

        self.move_speed = 0.02
        self.x_move = random.choice([10, -10])
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def bounce_down(self):
        self.y_move = -int(10 * (random.uniform(0.85, 1.15)))
        self.move_speed *= 0.95
    
    def bounce_up(self):
        self.y_move = int(10 * (random.uniform(0.85, 1.15)))

    def bounce_left(self):
        self.x_move = -int(10 * (random.uniform(0.85, 1.15)))
    
    def bounce_right(self):
        self.x_move = int(10 * random.uniform(0.85, 1.15))

    def reset_position(self):
        self.goto(BALL_STARTING_X, BALL_STARTING_Y)
        self.move_speed = 0.02
        self.x_move = random.choice([10, -10])
        self.y_move = 10


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.speed(0)
        self.stretch_len = 6
        self.width = BLOCK_SIZE * self.stretch_len
        self.shapesize(stretch_wid=1, stretch_len=self.stretch_len) 
        self.color(PADDLE_COLOR)
        self.reset_position()
                
    def go_right(self):
        new_xcor = self.xcor() + PADDLE_DISTANCE
        new_ycor = self.ycor()
        if new_xcor <= int(SCREEN_W / 2 -  20 * 6 / 2):
            self.goto(new_xcor, new_ycor)

    def go_left(self):
        new_xcor = self.xcor() - PADDLE_DISTANCE
        new_ycor = self.ycor()
        if new_xcor >= -int(SCREEN_W / 2 - 20 * 6 / 2):
            self.goto(new_xcor, new_ycor)

    def reset_position(self):
        self.goto(PADDLE_STARTING_POS)


if __name__ == '__main__':
    pass
    