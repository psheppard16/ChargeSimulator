__author__ = 'psheppard16'
import tkinter as tk
from tkinter import *
import math
class Measure:
    def __init__(self, parent):
        self.window = parent
        self.parent = parent
        self.root = parent.root
        self.magnitudeT = StringVar()
        self.magnitudeT.set("" + "N/C")
        self.angleT = StringVar()
        self.angleT.set("" + "deg")
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
        self.magnitudeB = Label(self.root, text="The magnitude is:")
        self.magnitudeB.pack(in_=self.f)
        self.magnitudeL = Label(self.root, textvariable=self.magnitudeT)
        self.magnitudeL.pack(in_=self.f)
        self.angleB = Label(self.root, text="The angle is:")
        self.angleB.pack(in_=self.f)
        self.angleL = Label(self.root, textvariable=self.angleT)
        self.angleL.pack(in_=self.f)
        self.enter = Button(self.root, text="Enter", command=self.enter)
        self.enter.pack(in_=self.f)
        self.cancel = Button(self.root, text="Cancel", command=self.cancel)
        self.cancel.pack(in_=self.f)
        self.f.pack(side=LEFT)

    def enter(self):
        try:
            x = float(self.xBox.get())
            y = float(self.yBox.get())
            sumX = 0
            sumY = 0
            for i in range(0, len(self.parent.particleList)):
                p = self.parent.particleList[i]
                force = 9000000000 * p.charge / ((p.x - x) * (p.x - x) + (p.y - y) * (p.y - y))
                sumX += force * math.cos(math.atan((p.y - y) / (p.x - x)))
                sumY += force * math.sin(math.atan((p.y - y) / (p.x - x)))
            for j in range(0, len(self.parent.fieldList)):
                f = self.parent.fieldList[j]
                sumX += f.magnitude * math.cos(math.radians(f.angle))
                sumY += f.magnitude * math.sin(math.radians(f.angle))
            angle = math.degrees(math.atan(sumY / sumX))
            magnitude = math.hypot(sumX, sumY)
            self.angleT.set(str(round(angle, 2)) + "deg")
            self.magnitudeT.set(str(round(magnitude, 2)) + "N/C")
        except:
            print("incorrect inputs")

    def cancel(self):
        self.window.rMenu = "mainMenu"
    def hide(self):
        self.f.pack_forget()