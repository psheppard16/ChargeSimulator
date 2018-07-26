__author__ = 'psheppard16'
from AddParticle import *
from Measure import *
from MainMenu import *
from AddField import *
from Stage import *
from Option import *
class Window:
    def __init__(self):
        self.largestMagnitude = 0;
        self.currentMagnitude = 0;
        self.width = 625
        self.height = 500
        self.centerX = (self.width - 125) / 2
        self.centerY = self.height / 2
        self.fieldList = []
        self.particleList = []
        self.grid = True
        self.fieldLines = True
        self.fieldDensity = True
        self.cMenu = "start"
        self.rMenu = "mainMenu"
        self.root = tk.Tk()
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.root.resizable(False, False)
        self.mainMenu = MainMenu(self)
        self.addParticle = AddParticle(self)
        self.measure = Measure(self)
        self.addField = AddField(self)
        self.option = Option(self)
        self.stage = Stage(self)
        self.root.after(1, self.loop)
        self.root.mainloop()
    def loop(self):
        while(1):
            if self.cMenu != self.rMenu:
                self.clearWindow()
                if self.rMenu == "options":
                    self.option.f.pack(side=LEFT)
                if self.rMenu == "addCharge":
                    self.addParticle.f.pack(side=LEFT)
                if self.rMenu == "addField":
                    self.addField.f.pack(side=LEFT)
                if self.rMenu == "measure":
                    self.measure.f.pack(side=LEFT)
                if self.rMenu == "mainMenu":
                    self.mainMenu.f.pack(side=LEFT)
                    pass
                self.cMenu = self.rMenu
            self.stage.canvas.create_oval(self.centerX - 2, self.centerY - 2, self.centerX + 2, self.centerY + 2, fill="blue")
            if self.grid:
                for i in range(0, int(self.width / 10)):
                    self.stage.canvas.create_line(i * 10, 0, i * 10, self.height, fill="red", width=1)
                    self.stage.canvas.create_line(0, i * 10, self.width, i * 10, fill="red", width=1)
            for u in range(0, len(self.particleList)):
                self.stage.canvas.create_oval(self.centerX + self.particleList[u].x - 2,
                                              self.centerY - self.particleList[u].y - 2,
                                              self.centerX + self.particleList[u].x + 2,
                                              self.centerY - self.particleList[u].y + 2, fill="black")
            if self.fieldLines:
                largestMag = 0
                for k in range(0, int(self.width / 10)):
                    for j in range(0, int(self.width / 10)):
                        try:
                            x = self.centerX - k * 10
                            y = self.centerY - j * 10
                            sumX = 0
                            sumY = 0
                            try:
                                for m in range(0, len(self.particleList)):
                                    p = self.particleList[m]
                                    force = 9000000000 * p.charge / ((p.x - x) * (p.x - x) + (p.y - y) * (p.y - y))
                                    sumX += force * math.cos(math.atan2((y - p.y),(p.x - x)))
                                    sumY += force * math.sin(math.atan2((y - p.y),(p.x - x)))
                            except:
                                pass
                            for l in range(0, len(self.fieldList)):
                                f = self.fieldList[l]
                                sumX -= f.magnitude * math.cos(math.radians(f.angle))
                                sumY += f.magnitude * math.sin(math.radians(f.angle))
                            angle = math.atan2(sumY, sumX)
                            magnitude = math.hypot(sumX, sumY)
                            if magnitude > largestMag:
                                largestMag = magnitude
                            if self.fieldDensity:
                                if (sumX != 0 or sumY != 0) and self.largestMagnitude > 0:
                                    self.currentMagnitude -= magnitude
                                    if self.currentMagnitude <= 0:
                                        self.currentMagnitude = self.largestMagnitude / 15
                                        self.stage.canvas.create_line(self.centerX + x, self.centerY - y,
                                                                self.centerX + x - math.copysign(math.cos(angle), sumX),
                                                                self.centerY - y - math.copysign(math.sin(angle), sumY),
                                                                fill="green", width=1, arrow=tk.LAST)
                            else:
                                if sumX != 0 or sumY != 0:
                                    self.stage.canvas.create_line(self.centerX + x, self.centerY - y,
                                                                self.centerX + x - math.copysign(math.cos(angle), sumX),
                                                                self.centerY - y - math.copysign(math.sin(angle), sumY),
                                                                fill="green", width=1, arrow=tk.LAST)
                        except:
                            pass
                self.largestMagnitude = largestMag
                self.currentMagnitude = largestMag / 15
                self.fieldLinesChanged = False
            self.root.update()
            self.stage.canvas.delete("all")
    def clearWindow(self):
        self.option.hide()
        self.addField.hide()
        self.addParticle.hide()
        self.measure.hide()
        self.mainMenu.hide()


