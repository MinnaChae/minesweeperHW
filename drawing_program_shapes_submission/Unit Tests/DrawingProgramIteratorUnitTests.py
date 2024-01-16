"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""

import unittest
from ShapeFactory import ShapeFactory
from DrawingProgram import DrawingProgram

class MyDrawingProgramIteratorTest(unittest.TestCase):
# •	DrawingProgramIterator class functionality
# o	use of for loop as shown above demonstrates this class works
# o	be sure and use it with a DrawingProgram object that has no shapes, one shape, then maybe 5 shapes

    def test_iter_with_many_shapes(self):
        # Test Iterator iterating through many shapes
        # print("---------------Testing iter class for many shapes---------------")
        program = DrawingProgram()
        circle_small = ShapeFactory.create_shape("Circle", 1)
        circle_large = ShapeFactory.create_shape("Circle", 5)
        square_small = ShapeFactory.create_shape("Square", 1)
        square_large = ShapeFactory.create_shape("Square", 5)
        rectangle = ShapeFactory.create_shape("Rectangle", 2, 3)
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)

        program.add_shape(circle_small)
        program.add_shape(circle_large)
        program.add_shape(square_small)
        program.add_shape(square_large)
        program.add_shape(rectangle)
        program.add_shape(triangle)


        #tests for next function in the iteration protocol
        for i in program:
            self.assertRaises(StopIteration)

        iter_string=""

        for shape in program:
            iter_string += str(shape) +"\n"

        self.assertEqual(program.__str__(), iter_string)

    def test_iter_without_shapes(self):
        #Tests the iter function with no shapes where inter returns an IndexError

        program = DrawingProgram()
        with self.assertRaises(IndexError):
            for shape in program:
                print(shape)

    def test_iter_one_shape(self):
        # Test Iterator iterating through one shape

        program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1)
        program.add_shape(circle_one)

        for i in program:
            self.assertRaises(StopIteration)

        iter_string=""

        for shape in program:
            iter_string += str(shape) +"\n"

        self.assertEqual(program.__str__(), iter_string)

if __name__ == '__main__':
    unittest.main()