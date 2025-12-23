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
