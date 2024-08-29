import math
import time
import tkinter as tk


class Hero:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.id = canvas.create_oval(80, 80, 120, 120, fill="red")

    def shoot(self, event, main):
        fireball = Fireball(self.canvas, self.id, event)
        main.fireballs.append(fireball)


class Fireball:
    def __init__(self, canvas: tk.Canvas, master, event):
        self.speed_x, self.speed_y = 0, 0
        self.canvas = canvas
        self.size = 34
        master_pos = canvas.coords(master)
        self.id = canvas.create_oval(master_pos[0], master_pos[1], master_pos[2] - self.size,
                                     master_pos[3] - self.size, fill='yellow')

        vector = event.x - master_pos[0], event.y - master_pos[1]
        len_v = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        vector = vector[0] / len_v, vector[1] / len_v

        self.speed_x = vector[0] * 5
        self.speed_y = vector[1] * 5

    def update(self):
        self.canvas.move(self.id, self.speed_x, self.speed_y)


class MainWindow:
    def __init__(self):
        self.x, self.y, self.w, self.h = 100, 100, 200, 200
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry(f'{self.w}x{self.h}+{self.x}+{self.y}')
        self.canvas = tk.Canvas(self.root, width=self.w, height=self.h, bg="black")
        self.canvas.pack()
        self.hero = Hero(self.canvas)
        self.fireballs = []
        self.speed_x, self.speed_y = 0, 0

        self.root.bind_all("<Button-1>", lambda event: self.hero.shoot(event, self))
        self.root.bind_all("<B3-Motion>", self.move)
        self.root.bind_all("<ButtonRelease-3>", self.stop)

    def update(self):
        self.root.geometry(f'{self.w}x{self.h}+{self.x}+{self.y}')
        self.canvas.config(width=self.w, height=self.h)
        self.x += self.speed_x
        self.y += self.speed_y
        self.x = int(self.x)
        self.y = int(self.y)

    def draw(self):
        """Обрисовывать на холсте игру"""
        self.hero = Hero(self.canvas)
        for fb in self.fireballs:
            fb.update()
            result = self.check_contact(fb)
            if result == "delete":
                self.canvas.delete(fb.id)
                self.fireballs.remove(fb)

    def check_contact(self, fb: Fireball):
        x, y, w, h = self.canvas.coords(fb.id)
        if x >= self.w:
            self.w += 10
            return "delete"
        if x <= 0:
            self.x -= 10
            self.w += 10
            return "delete"
        if y >= self.h:
            self.h += 10
            return "delete"
        if y <= 0:
            self.y -= 10
            self.h += 10
            return "delete"

    def move(self, event: tk.Event):
        master_pos = self.canvas.coords(self.hero.id)
        vector = event.x - master_pos[0], event.y - master_pos[1]
        len_v = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        vector = vector[0] / len_v, vector[1] / len_v

        self.speed_x = vector[0] * 6
        self.speed_y = vector[1] * 6

    def stop(self, event):
        self.speed_x, self.speed_y = 0, 0


if __name__ == '__main__':
    m = MainWindow()
    while True:
        time.sleep(0.01)
        m.update()
        m.draw()

        m.root.update()
        m.root.update_idletasks()