class Shape:
    def area(self):
        pass
    class Triangle(Shape):
        def __init__(self, base, height):
            self.base=base
            self.height=height
            def area(self):
                return 0.5*self.base*self.height
            
            class Circle(Shape):
                def __init__(self,radius):
                    self.radius=radius
                    def area(self):
                        return 3.14*self.radius*self.radius
                    
                    class Rectangle(Shape):
                        def __intit__(self, length, width):
                            self.length=length
                            self.width=width
                            def area(self):
                                return self.length*self.width
                            b=int(input("Enter the value of base"))
                            h=int(input("Enter thr value of height"))
                            triangle=triangle(b, h)
                            print("Area of the triangle: ", triangle.area())
                            r=int(input("Enter the value of radius"))
                            circle=circle(r)
                            print("Area of the circle", circle.area())
                            l=int(input("enter the value of length"))
                            w=int(input("Enter the value of width"))
                            rectangle=Rectangle(l, w)
                            print("Area of the rectangle: ", rectangle.area())