__author__ = 'psheppard16'
from Field import*
from tkinter import *
class AddField:
    def __init__(self, parent):
        self.window = parent
        self.parent = parent
        self.root = parent.root
        self.f = Frame(self.root, bg="green", width=125, height =500)
        self.f.pack_propagate(0)
        self.magnitudeL = Label(self.root, text="Magnitude:")
        self.magnitudeL.pack(in_=self.f)
        self.magnitude = Entry(self.root, text="enter magnitude", width=100)
        self.magnitude.pack(in_=self.f)
        self.angleL = Label(self.root, text="Angle:")
        self.angleL.pack(in_=self.f)
        self.angle = Entry(self.root, text="enter angle", width=100)
        self.angle.pack(in_=self.f)
        self.enter = Button(self.root, text="Enter", command=self.enter)
        self.enter.pack(in_=self.f)
        self.cancel = Button(self.root, text="Cancel", command=self.cancel)
        self.cancel.pack(in_=self.f)
        self.f.pack(side=LEFT)
    def enter(self):
        try:
            magnitude = int(self.magnitude.get())
            angle = int(self.angle.get())
            field = Field(magnitude, angle)
            self.parent.fieldList.append(field)
        except:
            print("incorrect inputs")

    def cancel(self):
        self.window.rMenu = "mainMenu"

    def hide(self):
        self.f.pack_forget()
