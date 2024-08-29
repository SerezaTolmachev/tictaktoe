import random
import tkinter

tk = tkinter.Tk()
tk.geometry('900x700')

canvas = tkinter.Canvas(tk, width=900, height=700)


A = [450, 50]
B = [100, 600]
C = [800, 600]
SIZE = 10
colors = ['red', 'green', 'blue']

for num, dot in enumerate((A, B, C)):
    canvas.create_oval(dot[0] - SIZE, dot[1] - SIZE, dot[0] + SIZE, dot[1] + SIZE, fill=colors[num])

size = 2
random_dot = [random.randint(0, 900), random.randint(0, 700)]
canvas.create_oval(random_dot[0] - size, random_dot[1] - size, random_dot[0] + size, random_dot[1] + size, fill='black')
last_dot = random_dot

for i in range(10000):
    aim = random.choice((A, B, C))
    new = (aim[0] + last_dot[0])/2, (aim[1] + last_dot[1])/2
    canvas.create_oval(new[0] - size, new[1] - size, new[0] + size, new[1] + size, fill='black')
    last_dot = new














































tk.mainloop()