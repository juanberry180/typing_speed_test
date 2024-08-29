from tkinter import Tk, Canvas, Label, Button, Entry, filedialog, ttk, font, Frame
import texts_example
import time

timer = None
input_box = None

light_beige = '#F5EDED'
beige = '#E2DAD6'
light_blue = '#7FA1C3'
blue = '#6482AD'


text_intro='''Thanks to this app you will measure your writing speed\n
After pressing START text will appear in the box below.'''

counter = 60

def start():
    global input_box
    text = texts_example.text_200
    canvas.itemconfig(text_to_copy, text=text)
    input_box = Entry(window, width=100, font=('Modern', 14, "normal"))
    input_box.focus()
    input_box.grid(row=6, column=0)
    count_down(10)


def reset():
    window.after_cancel(timer)
    canvas2.itemconfig(time_text, text='60')
    canvas.itemconfig(text_to_copy, text='')
    instruction2.config(text='Please enter your text in the box that will appear below'.upper())
    input_box.destroy()
    canvas.itemconfig('', text=str(counter))
    result.config(text='')

def count_down(counter):
    global timer
    global input_box
    if counter >= 0:
        canvas2.itemconfig(time_text, text=str(counter))
        timer = window.after(1000, count_down, counter - 1)
    else:
        text_entered = input_box.get()
        result_print(text_entered)

def result_print(text_entered):
     global input_box
     counted_words= len(text_entered.split(' '))
     result.config(text = f'You write {counted_words} words per minute.')
     instruction2.config(text = '')
     input_box.destroy()




window = Tk()
window.title('Speed writing checker application')
window.geometry('1500x1500')
window.configure(background=light_beige, padx=50, pady=50)

instruction = Label(window, text=text_intro.upper())
instruction.config(padx=5, pady=5, background=light_beige, fg=blue, font=('Arial',16,"bold"))
instruction.grid(row=0, column=0)

start_label = Button(text="START", width=15, command=start, padx=5, pady=5)
start_label.grid(row=1, column=0)

border_space = Label(window, text=' '.upper())
border_space.config(padx=1, pady=1, background=light_beige, fg=blue, font=('Arial',5,"bold"))
border_space.grid(row=2, column=0)

canvas = Canvas(width=1400, height=300, bg=beige, highlightthickness=0, borderwidth=5)
text_to_copy = canvas.create_text(20, 20, anchor="nw", text='', fill=blue, font=('Modern', 14, "normal"))
canvas.grid(row=3, column=0)

instruction2 = Label(window, text='Please enter your text in the box that will appear below'.upper())
instruction2.config(padx=5, pady=5, background=light_beige, fg=blue, font=('Arial',16,"bold"))
instruction2.grid(row=4, column=0)

border_space = Label(window, text=' '.upper())
border_space.config(padx=1, pady=1, background=light_beige, fg=blue, font=('Arial',5,"bold"))
border_space.grid(row=5, column=0)

border_space = Label(window, text=' '.upper())
border_space.config(padx=1, pady=1, background=light_beige, fg=blue, font=('Arial',5,"bold"))
border_space.grid(row=7, column=0)

canvas2 = Canvas(width=100, height=100, bg=beige, highlightthickness=0, borderwidth=20)
time_text = canvas2.create_text(45, 40, text=60, anchor="nw", fill=blue, font=('Modern', 50, "normal"))
canvas2.grid(row=8, column=0)

border_space = Label(window, text=' '.upper())
border_space.config(padx=1, pady=1, background=light_beige, fg=blue, font=('Arial',5,"bold"))
border_space.grid(row=9, column=0)

stop_label = Button(text="RESET", width=15, command=reset, padx=5, pady=5)
stop_label.grid(row=10, column=0)

result = Label(window, text='')
result.config(padx=5, pady=5, background=light_beige, fg=blue, font=('Arial', 16, "bold"))
result.grid(row=11, column=0)

window.mainloop()

