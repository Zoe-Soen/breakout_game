import os


os.chdir('/Users/Zoe.Su/Documents/Zoe的学习资料/Python/100 days of Code- The Complete Python Pro Bootcamp for 2023/exercise code/day-87-breakout-game')

# screen：
TITLE_STR = 'Breakout Game'
SCREEN_W = 600
SCREEN_H = 800
SCREEN_COLOR = 'black'

# btns
BTN_COLORS = ['blue', 'red']
ALIGNMENT = "center"
BTN_FONT = ("Courier", 20, "normal")

# blocks：
BLOCK_SHAPE = 'square'
BLOCK_COLOR_G = ['yellow', 'green', 'orange', 'red']
ROW = 8
COL = 9
BLOCK_SIZE = 20
PAD = 5
BLOCK_TOP_LINE = int(SCREEN_H / 2 - BLOCK_SIZE / 2 - PAD - 35)

# paddle：
PADDLE_SHAPE = 'square'
PADDLE_COLOR = 'white'
PADDLE_STARTING_POS = (0, -int(SCREEN_H / 2) + BLOCK_SIZE + PAD) 
PADDLE_DISTANCE = 20
PADDLE_RIGHT = 90
PADDLE_LEFT = 270

# ball：
BALL_SHAPE = 'circle'
BALL_COLOR = 'white'
BALL_DISTANCE = 20
BALL_STARTING_X = 0
BALL_STARTING_Y = -int(SCREEN_H / 2) + BLOCK_SIZE * 2 + PAD

# scoreboard：
SCOREBOARD_COLOR = "white"
LIVES_POS = (110, 370) #SCREEN_H / 2 * 3)
SCORE_POS = (220, 370) #SCREEN_H / 2 * 3)
MSG_POS = (0, -50)

# font
ALIGNMENT = "center"
FONT = "Courier"
FONT_SIZE = [16, 20, 36]
FONT_MODE = "normal"


