'''
authors: (append name as needed)
  Zachariah Dumey
'''

TILE_TYPE_UNIVERSE = { 'E': 'empty', 'X': 'border', 'T': 'track' }  

class Tile:
  # represents a single tile on the playing field

  def __init__(self, tileType):
    self.ttype = TILE_TYPE_UNIVERSE[tileType]

    if self.ttype is None:
      raise Error('invalid tile type: ', tileType)
