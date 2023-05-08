# breakout game in python By E.Rey  

from tkinter import Tk, Canvas
import random
import time
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas_height = 400
canvas_width  = 500
canvas = Canvas(tk, width=canvas_width, height=canvas_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball_id = canvas.create_oval(10, 10, 25, 25, fill='purple')
canvas.move(ball_id, 245, 100)
starts = [-3, -2, -1, 1, 2, 3]
random.shuffle(starts)
ball_x = starts[0]
ball_y = -3

paddle_id = canvas.create_rectangle(0, 0, 100, 10, fill='green')
canvas.move(paddle_id, 200, 300)
paddle_x = 0

def draw_ball():
    global ball_x, ball_y
    canvas.move(ball_id, ball_x, ball_y)
    pos = canvas.coords(ball_id)
    if pos[1] <= 0:
        ball_y = 3
    if pos[3] >= canvas_height:
        ball_y = -3
    if hit_paddle(pos) == True:
        ball_y = -3
    if pos[0] <= 0:
        ball_x = 3
    if pos[2] >= canvas_width:
        ball_x = -3
            
def hit_paddle(pos):
    paddle_pos = canvas.coords(paddle_id)
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
            return True
    return False

def turn_left(evt):
    global paddle_x
    paddle_x = -2
        
def turn_right(evt):
    global paddle_x
    paddle_x = 2
        
def draw_paddle():
    global paddle_x
    canvas.move(paddle_id, paddle_x, 0)
    pos = canvas.coords(paddle_id)
    if pos[0] <= 0:
        paddle_x = 0
    elif pos[2] >= canvas_width:
        paddle_x = 0

canvas.bind_all('<KeyPress-Left>' , turn_left)
canvas.bind_all('<KeyPress-Right>', turn_right)      
while True:
    draw_ball()
    draw_paddle()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)






