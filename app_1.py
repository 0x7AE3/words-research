import tkinter as tk
import math
import time
import word_methods


class Demo:
    def __init__(self, size=(700, 700), center=(350, 350), radius=100):
        self.size = size
        self.center = center
        self.radius = radius

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=700, width=700, bg='#263D42')

        self.angle = math.pi / 12  # default angle
        self.n = 32  # default number of points
        self.delay = 1

        self.reset = False

        self.angle_label = tk.Label(self.root, text=f'Angle: {round(self.angle, 2)}')
        self.n_label = tk.Label(self.root, text=f'Number of Points: {self.n}')

        self.create_objects()
        self.create_buttons()

        self.my_var = tk.StringVar()
        self.my_var.set(self.n)
        self.label = tk.Label(self.root, textvariable=self.my_var, fg='red')

    def run(self):
        self.canvas.pack()

        self.angle_button.pack(side=tk.LEFT)
        self.angle_input.pack(side=tk.LEFT)
        self.n_button.pack(side=tk.RIGHT)
        self.n_input.pack(side=tk.RIGHT)

        self.angle_label.place(x=4 / 5 * self.size[0], y=1 / 8 * self.size[1])
        self.n_label.place(x=4 / 5 * self.size[0], y=1 / 8 * self.size[1] + 20)

        self.start_button.place(x=4 / 5 * self.size[0], y=7 / 8 * self.size[1])
        self.pause_button.place(x=4 / 5 * self.size[0], y=7 / 8 * self.size[1] + 20)
        self.reset_button.place(x=4 / 5 * self.size[0], y=7 / 8 * self.size[1] + 20 + 20)

        self.label.place(x=1 / 5 * self.size[0], y=7 / 8 * self.size[1])

        self.root.mainloop()

    def create_objects(self):
        self.canvas.create_oval(self.center[0] - self.radius, self.center[1] - self.radius,
                                self.center[0] + self.radius, self.center[1] + self.radius, width=3)
        self.canvas.create_line(self.center[0] + 3 / 4 * self.radius, self.center[1], self.center[0] + 5/4 * self.radius,
                                self.center[1], fill='red')
        # for i in range(1, self.n + 1):
        #     arc_length = i * self.angle - int(i * self.angle)
        #     print(arc_length)
        #     # (x - 350)^2 + (y - 350)^2 = 75^2
        #     p1 = (
        #         3 / 4 * self.radius * math.cos(-(arc_length * 2 * math.pi - math.pi / 2)) + 350, 3 / 4 * self.radius *
        #         math.sin(-(arc_length * 2 * math.pi - math.pi / 2)) + 350)
        #     p2 = (
        #         5 / 4 * self.radius * math.cos(-(arc_length * 2 * math.pi - math.pi / 2)) + 350, 5 / 4 * self.radius *
        #         math.sin(-(arc_length * 2 * math.pi - math.pi / 2)) + 350)
        #     print(p1, p2)
        #     self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='green')
        #     self.canvas.update()
        #     # self.canvas.create_line(200, 200, 300, 400, fill='red')
        #     # time.sleep(1)

    def create_buttons(self):
        # noinspection PyAttributeOutsideInit
        self.angle_input = tk.Entry(self.root, width=20)

        def angle_button_command():
            try:
                _angle = eval(self.angle_input.get(), {'pi': math.pi, 'sqrt': math.sqrt})
            except SyntaxError:
                _angle = self.angle
            if type(_angle) is float or type(_angle) is int:
                self.angle = _angle
                self.angle_label['text'] = f'Angle: {round(self.angle, 2)}'

        # noinspection PyAttributeOutsideInit
        self.angle_button = tk.Button(self.root, text='Angle', width=20, command=angle_button_command)

        # noinspection PyAttributeOutsideInit
        self.n_input = tk.Entry(self.root, width=20)

        def n_button_command():
            try:
                _n = eval(self.n_input.get())
            except SyntaxError:
                _n = self.n
            if type(_n) is int:
                self.n = _n
                self.n_label['text'] = f'Number of Points: {self.n}'

        # noinspection PyAttributeOutsideInit
        self.n_button = tk.Button(self.root, text='Number of Points', width=20, command=n_button_command)

        def start_button_command():
            for i in range(1, self.n + 1):
                if self.reset:
                    self.reset = False
                    return

                arc_length = i * self.angle - int(i * self.angle)
                # print(arc_length)
                # (x - 350)^2 + (y - 350)^2 = 75^2
                p1 = (
                    3 / 4 * self.radius * math.cos(-(arc_length * 2 * math.pi)) + 350,
                    3 / 4 * self.radius *
                    math.sin(-(arc_length * 2 * math.pi)) + 350)
                p2 = (
                    5 / 4 * self.radius * math.cos(-(arc_length * 2 * math.pi)) + 350,
                    5 / 4 * self.radius *
                    math.sin(-(arc_length * 2 * math.pi)) + 350)
                # print(p1, p2)
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='green')
                # canvas.create_line(200, 200, 300, 400, fill='red')
                word = wordmethods.word(self.angle, i)
                print(i, word)
                self.my_var.set(word)
                self.canvas.update()
                time.sleep(self.delay)

        # noinspection PyAttributeOutsideInit
        self.start_button = tk.Button(self.root, text='Start', width=20, command=start_button_command)

        def pause_button_command():
            pass

        # noinspection PyAttributeOutsideInit
        self.pause_button = tk.Button(self.root, text='Pause', width=20, command=pause_button_command)

        def reset_button_command():
            self.reset = True
            self.canvas.delete('all')
            self.create_objects()
            self.create_objects()
            self.canvas.update()

        # noinspection PyAttributeOutsideInit
        self.reset_button = tk.Button(self.root, text='Reset', width=20, command=reset_button_command)


demo = Demo()
demo.run()
