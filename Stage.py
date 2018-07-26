__author__ = 'psheppard16'
from tkinter import *
class Stage:
    def __init__(self, parent):
        self.window = parent
        self.root = parent.root
        self.canvas = Canvas(self.root, bg="gray", width=500, height =500)
        self.canvas.place(x=125, y=0)
