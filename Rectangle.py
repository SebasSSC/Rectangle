#Sebastian SantaCruz
#CIS 261
#Rectangle
class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width
  def calculate_perimeter(self):
    perimeter = 2 * (self.height + self.width)
    return perimeter
  def calculate_area(self):
    area = self.height * self.width
    return area
  def printinfo(self):
    print("Height: " + str(self.height))
    print("Width: " + str(self.width))
    print("Perimeter: " + str(self.calculate_perimeter()))
    print("Area: " + str(self.calculate_area()))
    pass

if __name__ == "__main__":
  while True:
    height = int(input("Introduce height: "))
    width = int(input("Introduce width: "))
    
    my_rectangle = Rectangle(height, width)
    my_rectangle.printinfo()
    
    print(" *" * width)
    for _ in range(height - 2):
      print(" *" + "  " * (width -2) + " *")
    print(" *" * width)
    user_input = input("Do you want to continue? (y/n): ")
    if user_input.lower() != "y":
      break
