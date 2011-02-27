'''
authors: (append your name as needed)
  Zachariah Dumey
'''
from tile import Tile

class Map:
  def __init__(self, filename):
    # serialize a map as defined in the docs/maps file
    mapfile = open(filename)

    self.width = int(mapfile.readline())
    self.height = int(mapfile.readline())

    self.tiles = {}    

    if self.width < 1 or self.height < 1:
      raise Error("map has invalid params... here are width and height:", self.width, self.height)

    #representing the actual data as a dictionary keyed around a tuple 
    # (x, y) ... feel free to change this if it's confusing 
    for y in range(0, self.height - 1):
      row = mapfile.readline().split()

      if len(row) != self.width:
        raise Error("this map isn't square")

      for x in range(0, len(row) - 1):
        self.tiles[(x, y)] = Tile(row[x]) # create a new tile with the letter specified by the map text file

  def tile(self, i, j):
    #return the tile specified by i and j
    if i >= self.width or j >= self.height or i < 1 or j < 1:
      return None
    return tiles[(i, j)]

  def changeTile(self, i, j, newTileType):
    #change tile[i, j] to newTileType
    # returns true if successful, false otherwise
    if i >= self.width or j >= self.height or i < 1 or j < 1:
      return False
    tiles[(i, j)] = Tile(newTileType)
    return True  
