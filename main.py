
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✓'
time_count = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global cnt
    window.after_cancel(time_count)

    canvas.itemconfig(timer, text='00:00')
    lbl_timer.config(text='Timer', fg=GREEN)
    lbl_chck_mark.config(text='')

    cnt = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reset_time, cnt

    cnt += 1
    if cnt % 8 == 0:
        lbl_chck_mark.config(text=CHECK_MARK * (cnt//2))
        lbl_timer.config(text='Break', fg=PINK)
        countdown(LONG_BREAK_MIN*60)
    elif cnt % 2 == 0:
        lbl_chck_mark.config(text=CHECK_MARK * (cnt//2))
        lbl_timer.config(text='Break', fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        lbl_timer.config(text='Work', fg=GREEN)
        countdown(WORK_MIN*60)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(time_span):

    time_print = str(time.strftime('%M:%S', time.gmtime(time_span)))
    canvas.itemconfig(timer, text=time_print)

    if time_span > 0:
        global time_count
        time_count = window.after(1000, countdown, time_span - 1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
reset_time = False
cnt = 0


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1,row=1)

tomato_img = PhotoImage(file='tomato.png')

image = canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))



# Label
lbl_timer = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
lbl_timer.grid(column=1,row=0)


# Buttons
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2,row=2)


# Check mark
lbl_chck_mark = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
lbl_chck_mark.grid(column=1,row=3)


window.mainloop()