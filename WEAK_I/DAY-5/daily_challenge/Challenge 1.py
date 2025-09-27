import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return math.isclose(self.radius, other.radius)
        return NotImplemented

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=14)
    c3 = Circle(radius=3)

    print(c1)  
    print(c2) 

    c4 = c1 + c3
    print("Sum of c1 and c3:", c4)

   
    print("c1 > c2?", c1 > c2)  
    print("c1 < c2?", c1 < c2)  
    print("c1 == c3?", c1 == c3) 
    
    circles = [c1, c2, c3, c4]
    print("\nBefore sorting:")
    for c in circles:
        print(c)

    circles.sort()  
    print("\nAfter sorting:")
    for c in circles:
        print(c)

    try:
        import turtle
        t = turtle.Turtle()
        t.speed(0)
        screen = turtle.Screen()
        screen.title("Sorted Circles")

        t.penup()
        t.goto(-200, 0)
        for c in circles:
            t.pendown()
            t.circle(c.radius * 10) 
            t.penup()
            t.forward(c.radius * 20)
        screen.mainloop()
    except ImportError:
        print("\nTurtle module not installed; skipping drawing.")
