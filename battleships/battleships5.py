#!/usr/bin/python

import random

SHIPS = (
  ("battleship", 5),
  ("destroyer", 2),
  ("cruiser", 3),
  ("swimmer", 1)
)

class CrashError(Exception):
  pass

class Board(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = []
    for y in range(height):
      self.board.append( [ "." ] * width )
    self.ships = []

  def add_ship(self, ship):
    for ship2 in self.ships:
      if ship.intersect(ship2):
        raise CrashError('other ship')
    if ship.is_outside(self.width, self.height):
      raise CrashError('land')
    self.ships.append(ship)

  def alive(self):
    for ship in self.ships:
      if ship.alive():
        return True
    return False

  def __str__(self):
    s = ''
    for y, row in enumerate(self.board):
      for x, cell in enumerate(row):
        result, ship = self.check(x, y)
        s += result if result in '*x' else cell
      s += '\n'
    return s

  def check(self, x, y):
    for ship in self.ships:
      result = ship.check(x, y)
      if result != ' ':
        return result, ship
    return ' ', None

  def place_ships(self, ships=SHIPS):
    for name, length in ships:
      while True:
        try:
          x = random.randint(0, self.width)
          y = random.randint(0, self.height)
          direction = random.choice('hv')
          ship = Ship(name, x, y, direction, length)
          self.add_ship(ship)
        except CrashError:
          pass
        else:
          break

  def attack(self, x, y):
    if x < 0 or x >= self.width:
      return
    if y < 0 or y >= self.height:
      return
    result, ship = self.check(x, y)
    if not ship:
      self.board[y][x] = '0' # miss
    else:
      ship.attack(x, y)

class Ship(object):
  def __init__(self, name, startx, starty, direction, length):
    self.name = name
    self.coords = set()
    if direction == "h":
      dx, dy = 1, 0
    else:
      dx, dy = 0, 1
    x, y = startx, starty
    for i in range(length):
      self.coords.add((x, y))
      x += dx
      y += dy
    self.destroyed = set()

  def intersect(self, other):
    return self.coords & other.coords

  def is_outside(self, width, height):
    for (x, y) in self.coords:
      if x >= width or y >= height:
        return True
    return False

  def check(self, x, y):
    if (x,y) in self.coords:
      return self.name[0]
    if (x,y) in self.destroyed:
      if self.coords:
        return 'x'
      return '*'
    return ' '

  def attack(self, x, y):
    if (x, y) not in self.coords:
      return
    self.destroyed.add((x, y))
    self.coords.remove((x, y))
    if not self.coords:
      print "You sunk my", self.name, "!"

  def alive(self):
    return bool(self.coords)


b = Board(8, 8)
b.place_ships()

while b.alive():
  print b
  s = raw_input("x, y:")
  xy = s.split(",")
  if len(xy) != 2:
    continue
  try:
    x = int(xy[0])
    y = int(xy[1])
  except ValueError:
    continue
  b.attack(x - 1, y - 1)
print b
print "You have won!"
