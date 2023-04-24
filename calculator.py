from tkinter import *


def button_press(num):
    global text

    text = text + str(num)
    text_label.set(text)


def equals():
    global text
    try:
        total = str(eval(text))
        text_label.set(total)

        text = total

    except ZeroDivisionError:
        text_label.set("Error!")
        text = ""

    except SyntaxError:
        text_label.set("Syntax Error!")
        text = ""


def restart():
    global text

    text_label.set("")
    text = ""


window = Tk()
window.title("Calculator")
window.geometry("250x250")

text = ""
text_label = StringVar()

label = Label(window, textvariable=text_label, font=('consolas', 20), bg="white", width=24, height=1)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=1, width=4, font=35, command=lambda: button_press(1))
button1.grid(row=1, column=1)
button2 = Button(frame, text=2, height=1, width=4, font=35, command=lambda: button_press(2))
button2.grid(row=1, column=2)
button3 = Button(frame, text=3, height=1, width=4, font=35, command=lambda: button_press(3))
button3.grid(row=1, column=3)

button4 = Button(frame, text=4, height=1, width=4, font=35, command=lambda: button_press(4))
button4.grid(row=2, column=1)
button5 = Button(frame, text=5, height=1, width=4, font=35, command=lambda: button_press(5))
button5.grid(row=2, column=2)
button6 = Button(frame, text=6, height=1, width=4, font=35, command=lambda: button_press(6))
button6.grid(row=2, column=3)

button7 = Button(frame, text=7, height=1, width=4, font=35, command=lambda: button_press(7))
button7.grid(row=3, column=1)
button8 = Button(frame, text=8, height=1, width=4, font=35, command=lambda: button_press(8))
button8.grid(row=3, column=2)
button9 = Button(frame, text=9, height=1, width=4, font=35, command=lambda: button_press(9))
button9.grid(row=3, column=3)

button0 = Button(frame, text=0, height=1, width=4, font=35, command=lambda: button_press(0))
button0.grid(row=4, column=2)

minus = Button(frame, text="-", height=1, width=4, font=35, command=lambda: button_press("-"))
minus.grid(row=1, column=4)
plus = Button(frame, text="+", height=1, width=4, font=35, command=lambda: button_press("+"))
plus.grid(row=2, column=4)
multiplication = Button(frame, text="*", height=1, width=4, font=35, command=lambda: button_press("*"))
multiplication.grid(row=3, column=4)
division = Button(frame, text="/", height=1, width=4, font=35, command=lambda: button_press("/"))
division.grid(row=4, column=4)
equal = Button(frame, text="=", height=1, width=4, font=35, command=equals)
equal.grid(row=4, column=3)
float = Button(frame, text=".", height=1, width=4, font=35, command=lambda: button_press("."))
float.grid(row=4, column=1)

restart = Button(window, text="Res", height=1, width=12, font=35, command=restart)
restart.pack()
window.mainloop()
