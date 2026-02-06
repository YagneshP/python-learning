class Rectangle:
  """Rectangle clas to create rectangle for provided width and height"""
  def __init__(self, width, height):
    self._width = width
    self._height = height
  
  def set_width(self, new_width):
    self._width = new_width
  
  def set_height(self, new_height):
    self._height = new_height

  def get_area(self):
    return self._width * self._height
  
  def perimeter(self):
    return 2 * (self._width + self._height)