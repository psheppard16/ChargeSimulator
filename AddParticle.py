__author__ = 'psheppard16'
from tkinter import *
from Particle import *
class AddParticle:
    def __init__(self, parent):
        self.window = parent
        self.parent = parent
        self.root = parent.root
        self.f = Frame(self.root, bg="green", width=125, height =500)
        self.f.pack_propagate(0)
        self.xBoxL = Label(self.root, text="X Location:")
        self.xBoxL.pack(in_=self.f)
        self.xBox = Entry(self.root, text="enter x Location", width=100)
        self.xBox.pack(in_=self.f)
        self.yBoxL = Label(self.root, text="Y Location:")
        self.yBoxL.pack(in_=self.f)
        self.yBox = Entry(self.root, text="enter y Location", width=100)
        self.yBox.pack(in_=self.f)
        self.chargeL = Label(self.root, text="Charge:")
        self.chargeL.pack(in_=self.f)
        self.charge = Entry(self.root, text="enter charge", width=100)
        self.charge.pack(in_=self.f)
        self.enter = Button(self.root, text="Enter", command=self.enter)
        self.enter.pack(in_=self.f)
        self.cancel = Button(self.root, text="Cancel", command=self.cancel)
        self.cancel.pack(in_=self.f)
        self.f.pack(side=LEFT)

    def enter(self):
        try:
            x = float(self.xBox.get())
            y = float(self.yBox.get())
            charge = float(self.charge.get())
            particle = Particle(x, y, charge)
            self.parent.particleList.append(particle)
        except:
            print("incorrect inputs")

    def cancel(self):
        self.window.rMenu = "mainMenu"

    def hide(self):
        self.f.pack_forget()