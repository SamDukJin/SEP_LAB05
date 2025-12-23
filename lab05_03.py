import turtle as t
import time

# ---------------- Disk ----------------
import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

        self.t = t.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

    def showDisk(self):
        self.t.penup()

        # Center the disk horizontally
        self.t.goto(self.dxpos - self.dwidth / 2, self.dypos)

        self.t.setheading(0)
        self.t.pendown()
        self.t.color("black", "white")
        self.t.begin_fill()

        # Draw FULL rectangle (4 sides)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)

        self.t.end_fill()
        self.t.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        self.t.clear()
        self.showDisk()

    def clearDisk(self):
        self.t.clear()



# ---------------- Pole ----------------
class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=120):
        self.pname = name
        self.stack = []
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

        self.t = t.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

    def showpole(self):
        self.t.penup()
        self.t.goto(self.pxpos, self.pypos)
        self.t.setheading(0)
        self.t.pendown()

        for _ in range(2):
            self.t.forward(self.pthick)
            self.t.left(90)
            self.t.forward(self.plength)
            self.t.left(90)

        self.t.penup()

    def pushdisk(self, disk):
        new_y = self.pypos + (len(self.stack) * disk.dheight)
        disk.newpos(self.pxpos + self.pthick / 2, new_y)
        self.stack.append(disk)
        time.sleep(0.3)

    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            disk.clearDisk()
            return disk
        return None


# ---------------- Hanoi ----------------
class Hanoi(object):
    def __init__(self, n=3):
        self.startp = Pole("A", -150, 0)
        self.workspacep = Pole("B", 0, 0)
        self.destinationp = Pole("C", 150, 0)

        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range(n):
            disk = Disk(
                "d" + str(i + 1),
                0,
                i * 20,
                20,
                (n - i) * 30
            )
            self.startp.pushdisk(disk)

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, w, d):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, d, w)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, s, d)

    def solve(self):
        self.move_tower(len(self.startp.stack),
                        self.startp,
                        self.workspacep,
                        self.destinationp)


# ---------------- Run ----------------
screen = t.Screen()
screen.title("Tower of Hanoi")

h = Hanoi(4)
h.solve()

screen.mainloop()
