import time
from turtle import Screen
from tkinter import *
from elements import Blocks, Ball, Scoreboard, Paddle, Buttons, Pen
from config import *


# ==================================================================
def new_game():
    pen.clear()
    scoreboard = Scoreboard()
    blocks = Blocks()
    paddle = Paddle()
    ball = Ball()

    screen.onkey(fun=paddle.go_left, key='Left')
    screen.onkey(fun=paddle.go_right, key='Right')

    run(scoreboard, blocks, paddle, ball)


def run(scoreboard, blocks, paddle, ball):
    game_is_on = True
    while game_is_on:
        if len(blocks.all_blocks) > 0 and scoreboard.lives > 0:
            screen.update()
            time.sleep(ball.move_speed)
            ball.move()

            if (ball.xcor() <= -int(SCREEN_W / 2) + 20):
                ball.bounce_right()

            if (ball.xcor() >= int(SCREEN_W / 2) - 20):
                ball.bounce_left()
            
            if (ball.distance(paddle) < 60) and (ball.ycor() <= BALL_STARTING_Y):
                ball.bounce_up() 
                if ball.x_move > 0:
                    ball.bounce_right()
                else:
                    ball.bounce_left()
            
            if (ball.ycor() <= -420) and (ball.xcor() < int(paddle.xcor() - (paddle.width / 2) - 20) or ball.xcor() > int(paddle.xcor() + (paddle.width / 2) + 20)):
                scoreboard.count_lives()
                ball.reset_position()
                paddle.reset_position()
        
            if ball.ycor() < BLOCK_TOP_LINE:
                for item in blocks.all_blocks[::-1]:
                    if ball.distance(item['brick']) < 40 and (item['x_from'] <= ball.xcor() < item['x_to']):
                        item['brick'].hideturtle()
                        scoreboard.count_point(item['point'])
                        blocks.all_blocks.remove(item)
                        ball.bounce_down()
                        
                        if ball.x_move > 0:
                            ball.bounce_right()
                        else:
                            ball.bounce_left() 
                        break
            else:
                ball.bounce_down()
                if ball.x_move > 0:
                    ball.bounce_right()
                else:
                    ball.bounce_left()
        else:
            game_is_on = False
            if len(blocks.all_blocks) == 0:
                pen.color = 'white'
                pen.goto(0,100)
                pen.write(f'Congratulations! All blocks cleared!', align=ALIGNMENT, font=(FONT, FONT_SIZE[2], FONT_MODE))
                pen.goto(0,60)
                pen.write(f'Score: {scoreboard.score}', align=ALIGNMENT, font=(FONT, FONT_SIZE[1], FONT_MODE))
            else:
                pen.goto(0,100)
                pen.write(f'Game Over!', align=ALIGNMENT, font=(FONT, FONT_SIZE[2], FONT_MODE))
                pen.goto(0,60)
                pen.write(f'Score: {scoreboard.score}', align=ALIGNMENT, font=(FONT, FONT_SIZE[1], FONT_MODE))

            scoreboard.clear()
            blocks.clear_blocks()
            paddle.goto(1000,1000)
            ball.goto(1000,1000)    
            restart_btn = Buttons('Restart', 'white', 0, 0, restart)
            restart_btn.show_btn()

def restart():
    pen.clear()
    new_scoreboard = Scoreboard()
    new_blocks = Blocks()
    new_paddle = Paddle()
    new_ball = Ball()    
    screen.onkey(fun=new_paddle.go_left, key='Left')
    screen.onkey(fun=new_paddle.go_right, key='Right')
    run(new_scoreboard, new_blocks, new_paddle, new_ball)      

# ==================================================================
screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.bgcolor(SCREEN_COLOR)
screen.title(TITLE_STR)
screen.tracer(0)
screen.listen()

pen = Pen()
pen.write('Welcome to Breakout Game!', align=ALIGNMENT, font=(FONT, FONT_SIZE[2], FONT_MODE))
start_btn = Buttons('Start Play', 'white', 0, 20, new_game)

# ==================================================================           
screen.mainloop()