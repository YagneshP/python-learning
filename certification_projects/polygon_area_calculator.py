import math
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
  
  def get_perimeter(self):
    return 2 * (self._width + self._height)
  
  def get_diagonal(self):
    return math.sqrt(self._width ** 2 + self._height ** 2)
  
  def get_picture(self):
    result = ''
    if self._width > 50 or self._height > 50:
      result += 'Too big for picture.'
      return result
    for h in range(0, self._height):
      result += f"{'*' * self._width}\n"
    return result
  
  def get_amount_inside(self, shape):
    # 1. we check height and width of shape compare to self 
    # 2. shape.height // self.height and shape.width // self.width and get max value 
    if self._width > shape._width and self._height > shape._width:
      return max(self._width // shape._width, self._height // shape._height)
    return 0
    
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))