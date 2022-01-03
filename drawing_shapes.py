import turtle
from random import randint

class GeometricSystem:
  def __init__(self, random_color_mode = True):
    self.random_color_mode = random_color_mode
    self.color = False
    turtle.speed(0)
    turtle.colormode(255)
    turtle.pensize(1)
  def set_color(self, random_color_mode=True, red=False, green=False, blue=False):
    if random_color_mode:
      self.random_color_mode = True
    else:
      self.random_color_mode = False
      self.pencolor = turtle.color(red, green, blue)
  def refresh_color(self):
    if self.random_color_mode:
      turtle.pencolor = turtle.color(randint(100, 220), randint(100, 220), randint(100, 220))
      turtle.fillcolor = turtle.pencolor
  def draw_orbit(self, radius):
    self.refresh_color()
    turtle.penup()
    turtle.setheading(0)
    turtle.setposition(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
  def pick_position(self, orbit_radius, degrees=False):
    turtle.penup()
    turtle.setposition(0, -orbit_radius)
    turtle.setheading(0)
    if degrees:
      turtle.circle(orbit_radius, degrees)
    else:
      turtle.circle(orbit_radius, randint(0, 360))
  def draw_simple_figure(self, sides, length):
    self.refresh_color()
    heading = 0
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(length / 2)
    turtle.setheading(0)
    turtle.backward(length / 2)
    turtle.pendown()
    turtle.begin_fill()
    for side_index in range(sides):
      heading = 0 + side_index * 360 / sides
      turtle.setheading(heading)
      turtle.forward(length)
    turtle.end_fill()
    turtle.penup()
  def draw_triangle(self, length):
    self.draw_simple_figure(3, length)
  def draw_square(self, length):
    self.draw_simple_figure(4, length)
  def draw_pentagon(self, length):
    self.draw_simple_figure(5, length)
  def draw_hexagon(self, length):
    self.draw_simple_figure(6, length)
  def draw_spiral_system(self, figures):
    original_offset = randint(0, 360)
    for orbit_index in range(figures):
      offset_degree = (360 / figures) / 5 * orbit_index + original_offset
      self.draw_orbit(30 * (orbit_index + 1))
      for i in range(5):
        self.pick_position(30 * (orbit_index + 1), (i + 1) * 360 / 5 + offset_degree)
        self.draw_simple_figure(3 + orbit_index, 10)
      

geometric_system = GeometricSystem()
geometric_system.draw_spiral_system(7)
