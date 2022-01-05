import turtle
import math
from random import randint

class GeometricSystem:
  def __init__(self, random_color_mode = True):
    self.random_color_mode = random_color_mode
    self.color = False
    # turtle.setworldcoordinates(-200, -200, 200, 200)
    turtle.penup()
    turtle.speed(0)
    turtle.hideturtle()
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
  def prepare_to_draw_simple_polygon(self, sides, length):
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(length / (2 * math.tan(math.pi/sides)))
    turtle.setheading(0)
    turtle.backward(length / 2)
  def draw_simple_polygon(self, sides, length):
    self.refresh_color()
    self.prepare_to_draw_simple_polygon(sides, length)
    heading = 0
    turtle.pendown()
    turtle.begin_fill()
    for side_index in range(sides):
      heading = 0 + side_index * 360 / sides
      turtle.setheading(heading)
      turtle.forward(length)
    turtle.end_fill()
    turtle.penup()
  def draw_triangle(self, length):
    self.draw_simple_polygon(3, length)
  def draw_square(self, length):
    self.draw_simple_polygon(4, length)
  def draw_pentagon(self, length):
    self.draw_simple_polygon(5, length)
  def draw_hexagon(self, length):
    self.draw_simple_polygon(6, length)
  def draw_star(self, position, length, fill=True):
    self.refresh_color()
    turtle.penup()
    turtle.setposition(position[0] - length * math.sqrt(3) / 2 - length / 2, position[1])
    if fill:
      turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(-30)
    turtle.forward(length)
    turtle.setheading(-60)
    turtle.forward(length)
    turtle.setheading(60)
    turtle.forward(length)
    turtle.setheading(30)
    turtle.forward(length)
    turtle.setheading(150)
    turtle.forward(length)
    turtle.setheading(120)
    turtle.forward(length)
    turtle.setheading(240)
    turtle.forward(length)
    turtle.setheading(210)
    turtle.forward(length)
    if fill:
      turtle.end_fill()
    turtle.penup()
  def draw_background(self, max_orbit_radius, orbits):
    # turtle_screen = turtle.getscreen()
    # turtle_screen.bgcolor(randint(30, 70), randint(30, 70), randint(30, 70))
    self.set_color(False, 225, 225, 225)
    for i in range(orbits * 5):
      self.draw_star((randint(-max_orbit_radius - 20, max_orbit_radius + 20), randint(-max_orbit_radius - 20, max_orbit_radius + 20)), randint(1, 3), False)
    self.set_color()
  def sign(self, text, orbits):
    self.refresh_color()
    turtle.penup()
    max_canvas_dimension = 30 * (orbits + 1)
    turtle.setposition(max_canvas_dimension + 100, max_canvas_dimension)
    turtle.write(text, True, align="right", font=('Verdana', 10, 'bold'))
  def draw_system(self, signature, orbits, density):
    self.draw_background(30 * (orbits + 1), orbits)
    self.draw_star((0, 0), 10)
    original_offset = randint(0, 360)
    for orbit_index in range(orbits):
      offset_degree = (360 / orbits) / 5 * orbit_index + original_offset
      self.draw_orbit(30 * (orbit_index + 1))
      for i in range(density):
        self.pick_position(30 * (orbit_index + 1), (i + 1) * 360 / density + offset_degree)
        self.draw_simple_polygon(3 + orbit_index, 10)
    self.sign(signature, orbits)
  def save_drawing(self):
    turtle_screen = turtle.getscreen()
    turtle_screen.getcanvas().postscript(file="geometric_system.eps")

      

geometric_system = GeometricSystem()
geometric_system.draw_system('Name', 7, 10)
geometric_system.save_drawing()