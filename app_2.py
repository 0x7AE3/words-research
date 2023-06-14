import tkinter as tk
import math
import time
import word_methods

root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')

center = (350, 350)
size = (700, 700)
radius = 100

canvas.create_oval(center[0] - radius, center[1] - radius,
                   center[0] + radius, center[1] + radius, width=3)

n = 20
angle = math.sqrt(2) / 2
delay = 0.2  # seconds between adding points

canvas.pack()

for point_num in range(1, n + 1):
    arc_length = point_num * angle - int(point_num * angle)
    # print(arc_length)
    # (x - 350)^2 + (y - 350)^2 = 75^2
    p1 = (
        3 / 4 * radius * math.cos(-(arc_length * 2 * math.pi - math.pi / 2)) + 350, 3 / 4 * radius *
        math.sin(-(arc_length * 2 * math.pi - math.pi / 2)) + 350)
    p2 = (
        5 / 4 * radius * math.cos(-(arc_length * 2 * math.pi - math.pi / 2)) + 350, 5 / 4 * radius *
        math.sin(-(arc_length * 2 * math.pi - math.pi / 2)) + 350)
    # print(p1, p2)
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='green')
    # canvas.create_line(200, 200, 300, 400, fill='red')
    word = wordmethods.word(angle, point_num)
    print(word)
    canvas.update()
    time.sleep(delay)



root.mainloop()
