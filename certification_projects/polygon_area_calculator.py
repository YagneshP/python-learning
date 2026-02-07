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
    if self._width > shape._width and self._height > shape._width:
      return self._width // shape._width * self._height // shape._height
    return 0
    
  def __repr__(self):
    return f"Rectangle(width={self._width}, height={self._height})"

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def set_width(self, new_side_width):
    super().set_width(new_side_width)
    super().set_height(new_side_width)
    
  def set_height(self, new_side_height):
    super().set_width(new_side_height)
    super().set_height(new_side_height)
  
  def set_side(self, side_length):
    self._width = side_length
    self._height = side_length

  def __repr__(self):
    return f"Square(side={self._width})"
  

# print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
  
# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())