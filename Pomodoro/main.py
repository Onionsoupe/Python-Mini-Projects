from tkinter import *
import time
import math

from nltk import align

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
counter=0
time_window= None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global counter
    window.after_cancel(time_window)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, font=("Courier", 30, "bold"), bg=YELLOW)
    check_label.config(text="")
    counter=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global counter
    counter += 1
    if counter%8==0:
        count_down(20*60)
        timer_label.config(text="Break",fg=RED, font=("Courier",30,"bold"),bg=YELLOW)
    elif counter%2==0:
        count_down(5*60)
        timer_label.config(text="Break", fg=PINK, font=("Courier", 30, "bold"), bg=YELLOW)
    else:
        count_down(25*60)
        timer_label.config(text="Work", fg=GREEN, font=("Courier", 30, "bold"), bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins, secs = divmod(count, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text,text=timer)
    if count != 0:
        global time_window
        time_window = window.after(1000, count_down, count -1)
        return count
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(counter/2)):
            mark+="✔"
        check_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#timer label
timer_label = Label(text="Timer",fg=GREEN, font=("Courier",30,"bold"),bg=YELLOW)
timer_label.grid(column=1,row=0)
canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW,highlightthickness=0)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

check_label = Label(fg=GREEN, font=("Courier",18,"bold"),bg=YELLOW)
check_label.grid(column=1,row=4)


window.mainloop()
