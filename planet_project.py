
class Planet:
  def __init__(self, name, planet_type, star):
    if not isinstance(name, str) and not isinstance(planet_type, str) and not isinstance(star, str):
      raise TypeError("name, planet_type, and star must be strings")
    if not(name and planet_type and star):
      raise ValueError("name, planet_type, and star must be non-empty strings")
    
    self.name = name
    self.planet_type = planet_type
    self.star = star

  def orbit(self):
    return (f"{self.name} is orbiting around {self.star}...")
  
  def __str__(self):
    return(f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}")