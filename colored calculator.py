from tkinter import*

def press(num):
    
    global equation_label
    equation_label=equation_label + str(num)
    equation_button.set(equation_label)

def equals():
    
    global equation_label

    try:

        total = str(eval(equation_label))

        equation_button.set(total)

        equation_label = total

    except SyntaxError:

        equation_button.set("syntax error")

        equation_label = ""

    except ZeroDivisionError:

        equation_button.set("arithmetic error")

        equation_label = ""
def clear():
    global equation_label
    equation_button.set("")
    equation_label= ""


window =Tk()

window.title("calculator")
window.geometry("450x540")
window.resizable(width=False,
                 height=False)
img=PhotoImage(file='C:\\Users\\StarCloud\\Downloads\\calculator icon.png')

window.iconphoto(False,img)

equation_label= ""
equation_button=StringVar()

label = Label(window, textvariable=equation_button, font=('consolas',20), bg='gold', width=26, height=2)

label.pack()
frame=Frame(window)
frame.pack()


b1 = Button(frame, text=1, width=9, height=5, font=('Broadway',11),bg='red',
          command=lambda:press("1"))

b1.grid(row=0, column=0)

b1 = Button(frame, text=2, width=9, height=5, font=('Broadway',11),bg='green',
          command=lambda:press("2"))

b1.grid(row=0, column=1)

b1 = Button(frame, text=3, width=9, height=5, font=('Broadway',11),bg='blue',
          command=lambda:press("3"))

b1.grid(row=0, column=2)

b1 = Button(frame, text='+', width=9, height=5, font=('Broadway',11),bg='purple',
          command=lambda:press("+"))

b1.grid(row=0, column=3)

b1 = Button(frame, text=4, width=9, height=5, font=('Broadway',11),bg='red',
          command=lambda:press("4"))

b1.grid(row=1, column=0)

b1 = Button(frame, text=5, width=9, height=5, font=('Broadway',11),bg='green',
          command=lambda:press("5"))

b1.grid(row=1, column=1)


b1 = Button(frame, text=6, width=9, height=5, font=('Broadway',11),bg='blue',
          command=lambda:press("6"))

b1.grid(row=1, column=2)

b1 = Button(frame, text='-', width=9, height=5, font=('Broadway',11),bg='purple',
          command=lambda:press("-"))

b1.grid(row=1, column=3)


b1 = Button(frame, text=7, width=9, height=5, font=('Broadway',11),bg='red',
          command=lambda:press("7"))

b1.grid(row=2, column=0)

b1 = Button(frame, text=8, width=9, height=5, font=('Broadway',11),bg='green',
          command=lambda:press("8"))

b1.grid(row=2, column=1)

b1 = Button(frame, text=9, width=9, height=5, font=('Broadway',11),bg='blue',
          command=lambda:press("9"))

b1.grid(row=2, column=2)

b1 = Button(frame, text='*', width=9, height=5, font=('Broadway',11),bg='purple',
          command=lambda:press("*"))

b1.grid(row=2, column=3)

b1 = Button(frame, text=0, width=9, height=5, font=('Broadway',11),bg='red',
          command=lambda:press("0"))

b1.grid(row=3, column=0)

b1 = Button(frame, text='.', width=9, height=5, font=('Broadway',11),bg='green',
          command=lambda:press("."))

b1.grid(row=3, column=1)

b1 = Button(frame, text="/", width=9, height=5, font=('Broadway',11),bg='purple',
          command=lambda:press("/"))

b1.grid(row=3, column=3)


b1 = Button(frame, text='=', width=9, height=5, font=('Broadway',11),bg='blue',
          command=equals)

b1.grid(row=3, column=2)

clear = Button(window, text='clear', height=4, width=12,font=35, foreground='blue',bg='silver',
                 command=clear)
clear.pack()



window.mainloop()
















