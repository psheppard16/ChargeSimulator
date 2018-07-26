from tkinter import *
class Option:
    def __init__(self, parent):
        self.window = parent
        self.parent = parent
        self.root = parent.root
        self.f = Frame(self.root, bg="green", width=125, height =500)
        self.f.pack_propagate(0)
        self.gridF = StringVar()
        self.gridF.set("Display grid true")
        self.gridB = Button(self.root, textvariable=self.gridF, command=self.grid)
        self.gridB.pack(in_=self.f)
        self.fieldF = StringVar()
        self.fieldF.set("Display field true")
        self.fieldB = Button(self.root, textvariable=self.fieldF, command=self.field)
        self.fieldB.pack(in_=self.f)
        self.fieldDF = StringVar()
        self.fieldDF.set("Field density true")
        self.fieldDB = Button(self.root, textvariable=self.fieldDF, command=self.fieldD)
        self.fieldDB.pack(in_=self.f)
        self.cancel = Button(self.root, text="Cancel", command=self.cancel)
        self.cancel.pack(in_=self.f)
        self.f.pack(side=LEFT)

    def grid(self):
        print("button pressed")
        if self.parent.grid:
            self.parent.grid = False
            self.gridF.set("Display grid false")
        else:
            self.parent.grid = True
            self.gridF.set("Display grid true")

    def field(self):
        if self.parent.fieldLines:
            self.parent.fieldLines = False
            self.fieldF.set("Display field false")
        else:
            self.parent.fieldLines = True
            self.fieldF.set("Display field true")

    def fieldD(self):
        if self.parent.fieldDensity:
            self.parent.fieldDensity = False
            self.fieldDF.set("Field density false")
        else:
            self.parent.fieldDensity = True
            self.fieldDF.set("Field density true")

    def cancel(self):
        self.window.rMenu = "mainMenu"

    def hide(self):
        self.f.pack_forget()