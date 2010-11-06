#!/usr/bin/python

class Board(object):
  def __init__(self, width, height):
    self.board = []
    for y in range(height):
      self.board.append( [ " " ] * width )

  def __str__(self):
    return str(self.board)


class Ship(object):
  def __init__(self, name, startx, starty, direction, length):
    self.coords = []
    if direction == "h":
      dx, dy = 1, 0
    else:
      dx, dy = 0, 1
    x, y = startx, starty
    for i in range(length):
      self.coords.append((x, y))
      x += dx
      y += dy
    self.destroyed = []


b = Board(8, 8)
print b
