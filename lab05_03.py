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

<<<<<<< Updated upstream
class Pole(object):
   def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
      self.pname = name
      self.stack = []
      self.toppos = 0
      self.pxpos = xpos
      self.pypos = ypos
      self.pthick = thick
      self.plength = length

   def showpole(self):
      t.penup()
      t.goto(self.pxpos, self.pypos)
      t.setheading(0)
      t.pendown()
      
      for _ in range(2):
         t.forward(self.pthick)
         t.left(90)
         t.forward(self.plength)
         t.left(90)
         
      t.penup()
      t.goto(self.pxpos, self.pypos)
      t.setheading(0)

   def pushdisk(self, disk):
      new_y = self.pypos + (len(self.stack) * disk.dheight)
      disk.newpos(self.pxpos + self.pthick/2, new_y)
      
      self.stack.append(disk)
      disk.showdisk()

   def popdisk(self):
      if len(self.stack) > 0:
         disk = self.stack.pop()
         disk.cleardisk()
         return disk
      return None

=======
>>>>>>> Stashed changes
