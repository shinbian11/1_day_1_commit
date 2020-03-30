#GUI 만들기
from tkinter import *
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import urllib.request


class Calculator: #계산기
    def input_value(self, val):
        self.entry_value.insert("end", val)

    def clear_all(self):
        self.entry_value.delete(0, "end")

    def get_result(self):
        try:
            #return_value = eval(self.entry_value.get())  # 내장함수
            #https://api.mathjs.org/
            api_url = "http://api.mathjs.org/v4/?expr="
            expr = self.entry_value.get().replace("+", "%2B")
            url = api_url+expr
            print(url)
            url_data = urllib.request.urlopen(url)
            print(url_data)
            return_value = url_data.read().decode('utf-8')

            # write entry value to file
            f = open("calc_log.txt", "w")
            f.write(self.entry_value.get())
            f.close()
        except SyntaxError or NameError:
            self.entry_value.delete(0, "end")  # entry_value에 있는 거 다 삭제
            self.entry_value.insert(0, 'Input Error, Press AC Button')
        else:
            self.entry_value.delete(0, "end")
            self.entry_value.insert(0, return_value)

    def get_last_log(self):
        # read entry value from file
        f = open("calc_log.txt", "r")
        read_value = f.read()
        self.entry_value.delete(0, "end")
        self.entry_value.insert(0, read_value)

    def __init__(self, main):
        main.title("Simple calculator")
        main.geometry()
        self.entry_value = Entry(main, justify=RIGHT)
        self.entry_value.grid(row=0, column=0, columnspan=4)
        self.entry_value.focus_set()

        # Generating Buttons
        Button(main, text="=", width=22, command=lambda: self.get_result()).grid(row=5, column=2, columnspan=3)
        Button(main, text='AC', width=10, command=lambda: self.clear_all()).grid(row=4, column=0)
        Button(main, text='<', width=10, command=lambda: self.get_last_log()).grid(row=0, column=3)
        Button(main, text='+', width=10, command=lambda: self.input_value('+')).grid(row=1, column=3)
        Button(main, text='-', width=10, command=lambda: self.input_value('-')).grid(row=2, column=3)
        Button(main, text='x', width=10, command=lambda: self.input_value('*')).grid(row=3, column=3)
        Button(main, text='/', width=10, command=lambda: self.input_value('/')).grid(row=4, column=3)
        Button(main, text='.', width=10, command=lambda: self.input_value('.')).grid(row=4, column=2)
        Button(main, text='(', width=10, command=lambda: self.input_value('(')).grid(row=5, column=0)
        Button(main, text=')', width=10, command=lambda: self.input_value(')')).grid(row=5, column=1)
        Button(main, text='7', width=10, command=lambda: self.input_value(7)).grid(row=1, column=0)
        Button(main, text='8', width=10, command=lambda: self.input_value(8)).grid(row=1, column=1)
        Button(main, text='9', width=10, command=lambda: self.input_value(9)).grid(row=1, column=2)
        Button(main, text='4', width=10, command=lambda: self.input_value(4)).grid(row=2, column=0)
        Button(main, text='5', width=10, command=lambda: self.input_value(5)).grid(row=2, column=1)
        Button(main, text='6', width=10, command=lambda: self.input_value(6)).grid(row=2, column=2)
        Button(main, text='1', width=10, command=lambda: self.input_value(1)).grid(row=3, column=0)
        Button(main, text='2', width=10, command=lambda: self.input_value(2)).grid(row=3, column=1)
        Button(main, text='3', width=10, command=lambda: self.input_value(3)).grid(row=3, column=2)
        Button(main, text='0', width=10, command=lambda: self.input_value(0)).grid(row=4, column=1)

        # create initial blank file
        f = open("calc_log.txt", "w")
        f.close()

class ScienceCalculator(Calculator): #Calculator를 상속받는 과학계산기
    def get_sqrt(self):
        try:
            return_value = eval(self.entry_value.get())
        except SyntaxError or NameError:
            self.entry_value.delete(0, "end")
            self.entry_value.insert(0, 'Input Error, Press AC Button')
        else:
            calc_value = math.sqrt(return_value)
            self.entry_value.delete(0, "end")
            self.entry_value.insert(0, calc_value)
    def get_pow(self):
        try:
            return_value = eval(self.entry_value.get())
        except SyntaxError or NameError:
            self.entry_value.delete(0, "end")
            self.entry_value.insert(0, 'Input Error, Press AC Button')
        else:
            calc_value = math.pow(return_value, 2)
            self.entry_value.delete(0, "end")
            self.entry_value.insert(0, calc_value)

    def __init__(self, main):
        super().__init__(main)
        main.title("Science calculator")
        Button(main, text="루트", width = 10, command=lambda:self.get_sqrt()).grid(row=5, column=0)
        Button(main, text="제곱", width = 10, command=lambda:self.get_pow()).grid(row=5, column=1)

class GraphCalculator(ScienceCalculator): #ScienceCalculator를 상속
    x = []
    y = []
    fig = Figure(figsize=(3, 3), dpi=100)
    ax = fig.add_subplot(111)
    canvas = None

    def __init__(self, main):
        super().__init__(main)
        main.title("Graph Calculator")

    def get_sqrt(self):
        super().get_sqrt()
        for t in np.linspace(0, 100, 100):
            self.x.append(t)
            self.y.append(math.sqrt(t))
        self.ax.plot(self.x, self.y)
        self.canvas = FigureCanvasTkAgg(self.fig, main)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=4)

    def get_pow(self):
        super().get_pow()
        for t in np.linspace(0, 100, 100):
            self.x.append(t)
            self.y.append(math.pow(t, 2))
        self.ax.plot(self.x, self.y)
        self.canvas = FigureCanvasTkAgg(self.fig, main)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=4)


#main
main = Tk()
#calc = Calculator(main)
#calc = ScienceCalculator(main)
calc = GraphCalculator(main)
main.mainloop()