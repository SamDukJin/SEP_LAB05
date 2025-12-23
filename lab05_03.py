import turtle as t

class Disk(object):
   def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
      self.dname = name
      self.dxpos = xpos
      self.dypos = ypos
      self.dheight = height
      self.dwidth = width
      self.t = t.t()
      self.t.speed(0)
      self.t.hidet()
   
   def showDisk(self):
      self.t.penup()
      self.t.goto(self.dxpos, self.dypos)
      self.t.pendown()
      self.t.begin_fill()
      self.t.color("black", "white")
      for _ in range(2):
         self.t.forward(self.dwidth)
         self.t.left(90)
         self.t.forward(self.dheight)
         self.t.left(90)
      self.t.end_fill()
   
   
   def newpos(self,xpos,ypos):
      self.t.clear()
      self.dxpos = xpos
      self.dypos = ypos
      self.showDisk()
   
   def clearDisk(self):
      self.t.clear()

class Hanoi(object):
    """Hanoi class to solve Tower of Hanoi puzzle"""
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        
        for i in range(n):
            disk = Disk("d" + str(i), 0, i * 20, 20, (n - i) * 30)
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
        n = len(self.startp.stack)
        self.move_tower(n, self.startp, self.workspacep, self.destinationp)