import math
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    
    def area_cal(self):
        area = math.pi * self.radius ** 2        
        return area

    def perimeter_cal(self):
        perimeter = math.pi * self.radius * 2
        return perimeter
        
    def informer(self, perimeter, area):
        print(f"AREA ::: {float(area)}")
        print(f"PERIMETER ::: {float(perimeter)}")


my_circle = Circle()
area = my_circle.area_cal()
perimeter = my_circle.perimeter_cal()

my_circle.informer(perimeter, area)
