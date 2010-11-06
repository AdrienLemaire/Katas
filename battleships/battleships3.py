#!/usr/bin/python

SHIPS = (
  ("battleship", 5),
  ("destroyer", 4),
  ("

class Board(object):
  def __init__(self, width, height):
    self.board = []
    for y in range(height):
      self.board.append( [ "." ] * width )
    self.ships = []

  def add_ship(self, ship):
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
        result, ship = self.check(x,y)
        s += result if result != ' ' else cell
      s += '\n'
    return s

  def check(self, x, y):
    for ship in self.ships:
      result = ship.check(x, y)
      if result != ' ':
        return result, ship
    return ' ', None    

  def attack(self, x, y):
    if x < 0 or x >= len(self.board[0]):
      return
    if y < 0 or y >= len(self.board):
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

  def check(self, x, y):
    if (x,y) in self.coords:
      return self.name[0]
    if (x,y) in self.destroyed:
      if self.coords:
        return 'x'
      return '*'
    return ' '

  def attack(self, x, y):
    self.destroyed.add((x, y))
    self.coords.remove((x, y))

  def alive(self):
    return bool(self.coords)


b = Board(8, 8)
b.add_ship(Ship('SSDojo', 2, 3, 'h', 3))

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
  b.attack(x, y)
print b
