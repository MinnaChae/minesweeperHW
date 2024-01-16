"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

from abc import ABC, abstractmethod  # importing abstract base class


class Shape(ABC):  # ABC - abstract base class
    """ Creating a shape class which is an ABC class type. The methods in this class are: constructor,
    get_name, area(abstract method) and perimeter(abstract method), draw which prints the str method
    and a str method which has the string representation of get_name, area and perimeter"""

    def __init__(self, name):
        """  constructor for initialising name
          param : name """

        self.__name = name

    def get_name(self):
        """  method to get name
        return: name"""

        return self.__name

    @abstractmethod
    def area(self):
        """  abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """  abstract method for perimeter"""
        pass

    def draw(self):
        """ method to draw shapes which prints the str method"""
        print(self.__str__())

    def __str__(self):
        """  str method returns name, area and perimeter from the child classes"""
        return "{}, area: {}, perimeter: {}".format(self.get_name(), self.area(), self.perimeter())

    def __lt__(self, other):
        """ lesser than comparator method for sorting shapes. Compares with  other shapes
        param: other"""
        if isinstance(other, Shape):
            if self.__name < other.__name:
                return True
            elif self.__name == other.__name and self.area() < other.area():
                return True
            elif self.__name == other.__name and self.area() == other.area() and self.perimeter() < other.perimeter():
                return True
            else:
                return False
        else:
            raise TypeError("Other instance is not Shape type")

    def __eq__(self, other):
        """ equal to comparator method for sorting shapes. Compares with  other shapes
                param: other"""
        if isinstance(other, Shape):
            if self.__name == other.__name and self.area() == other.area() and self.perimeter() == other.perimeter():
                return True
            else:
                return False
        else:
            raise TypeError("Other instance is not Shape type")


class Circle(Shape):
    """ class Circle is a child class of Shape which gives the name of the class its area and perimeter """

    def __init__(self, radius):
        """ gets name from the Shape class
        param: radius"""
        super().__init__("Circle")
        self.__radius = radius

    def area(self):
        """ overriding area method from shape class and calculating area of circle"""
        value_of_area = 3.141592653589793 * self.__radius * self.__radius
        return value_of_area

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of circle"""
        value_of_perimeter = 6.283185307179586 * self.__radius
        return value_of_perimeter


class Rectangle(Shape):
    """ class Rectangle is a child class of Shape which gives the name of the class its area and perimeter"""

    def __init__(self, length, width):
        """  gets name from the Shape class
        param: length, width"""
        super().__init__("Rectangle")
        self.__length = length
        self.__width = width

    def area(self):
        """ overriding area method from shape class and calculating area of rectangle"""
        value_of_area = self.__length * self.__width
        return value_of_area

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of rectangle"""
        value_of_perimeter = 2 * (self.__length + self.__width)
        return value_of_perimeter


class Square(Shape):
    """ class Square is a child class of Shape which gives the name of the class its area and perimeter"""

    def __init__(self, side):
        """  gets name from the Shape class
                param: side"""
        super().__init__("Square")
        self.__side = side

    def area(self):
        """ overriding area method from shape class and calculating area of square"""
        value_of_area = self.__side * self.__side
        return value_of_area

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of square"""
        value_of_perimeter = 4 * self.__side
        return value_of_perimeter


class Triangle(Shape):
    """ class Triangle is a child class of Shape which gives the name of the class its area and perimeter"""

    def __init__(self, side1, side2, side3):
        """  gets name from the Shape class
                param: side1, side2, side3"""
        super().__init__("Triangle")
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def area(self):
        """ overriding area method from shape class and calculating area of triangle"""
        half_perimeter = self.perimeter() / 2
        return (half_perimeter * (half_perimeter - self.__side1) * (half_perimeter - self.__side2) * (
                half_perimeter - self.__side3)) ** 0.5

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of triangle"""
        return self.__side1 + self.__side2 + self.__side3