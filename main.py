import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.16
SHORT_BREAK_MIN = 0.08
LONG_BREAK_MIN = 0.08
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text=" ")
    global reps
    reps = 0
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_min_sec)
        timer_label.config(text="Work", fg=GREEN)


def count_down(count):
    start_button.config(state="disabled")
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            current_text = checkmark_label.cget("text")
            new_text = current_text + "✅"
            checkmark_label.config(text=new_text)
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)
window.mainloop()
