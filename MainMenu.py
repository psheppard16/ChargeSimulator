__author__ = 'psheppard16'
from tkinter import *
class MainMenu:
    def __init__(self, parent):
        self.window = parent
        self.parent = parent
        self.root = parent.root
        self.f = Frame(self.root, bg="green", width=125, height =500)
        self.f.pack_propagate(0)
        self.options = Button(self.root, text="Options", command=self.options)
        self.options.pack(in_=self.f)
        self.addCharge = Button(self.root, text="Add a particle", command=self.addCharge)
        self.addCharge.pack(in_=self.f)
        self.clearCharges = Button(self.root, text="Clear charges", command=self.clearCharges)
        self.clearCharges.pack(in_=self.f)
        self.addField = Button(self.root, text="Add a field", command=self.addField)
        self.addField.pack(in_=self.f)
        self.clearFields = Button(self.root, text="Clear Fields", command=self.clearFields)
        self.clearFields.pack(in_=self.f)
        self.measure = Button(self.root, text="Measure field", command=self.measure)
        self.measure.pack(in_=self.f)
        self.f.pack(side=LEFT)

    def options(self):
        self.window.rMenu = "options"

    def addField(self):
        self.window.rMenu = "addField"

    def measure(self):
        self.window.rMenu = "measure"

    def clearCharges(self):
        for i in self.parent.particleList:
            self.parent.particleList.remove(i)

    def clearFields(self):
        for i in self.parent.fieldList:
            self.parent.fieldList.remove(i)

    def addCharge(self):
        self.window.rMenu = "addCharge"

    def hide(self):
        self.f.pack_forget()