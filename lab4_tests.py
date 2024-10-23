import data
import lab4
import unittest


# Write your test cases for each part below.
from data import Point
class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[],[1,2]]
        result = lab4.first_element(input)
        expected = [1]
        self.assertEqual(expected, result)

    # Part 2

    def test_x_coordinates(self):
        input = [Point(1,2), Point(2,3), Point(3,4)]
        result = lab4.x_coordinates(input)
        expected = [1,2,3]
        self.assertEqual(expected,result)
    def test_x_coordinates_2(self):
        input = [Point(-1,2), Point(-10,-15), Point(100,-5)]
        result = lab4.x_coordinates(input)
        expected = [-1,-10,100]
        self.assertEqual(expected,result)

    # Part 3

    def test_are_in_positive_quadrant(self):
        input = [Point(-1,2), Point(1,-2), Point(-2,-2)]
        result = lab4.are_in_positive_quadrant(input)
        expected = []
        self.assertEqual(expected,result)
    def test_are_in_positive_quadrant_2(self):
        input = [Point(1,2), Point(-1,2), Point(5,10)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[1,2],[5,10]]
        self.assertEqual(expected,result)

    # Part 4

    def test_distance(self):
        input = Point(1,2)
        input2 = Point(3,4)
        result = lab4.distance(input,input2)
        expected = 2.0
        self.assertEqual(expected,result)
    def test_distance_2(self):
        input = Point(10,15)
        input2= Point(2,11)
        result = lab4.distance(input,input2)
        expected = 8.0
        self.assertEqual(expected,result)

    # Part 5

    def test_manhattan_distance(self):
        input = Point(10,10)
        input2 = Point(5,5)
        result = lab4.manhattan_distance(input,input2)
        expected = 10.0
        self.assertEqual(expected,result)
    def test_manhattan_distance_2(self):
        input = Point(-10,-10)
        input2 = Point(5,5)
        result = lab4.manhattan_distance(input,input2)
        expected = 30.0
        self.assertEqual(expected,result)

    # Part 6

    def test_distance_all(self):
        input = [Point(3,4),Point(8,6),]
        result = lab4.distance_all(input)
        expected = [5,10]
        self.assertEqual(expected,result)
    def test_distance_all_2(self):
        input = [Point(-3,-4), Point(-8,6)]
        result = lab4.distance_all(input)
        expected = [5,10]
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
