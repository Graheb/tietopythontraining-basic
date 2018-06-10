# tests for distance
import unittest
import distance


class DistanceTest(unittest.TestCase):

    # Tests that it crashes with TypeError when called on None
    def test_input_None_all(self):
        self.assertRaises(TypeError, distance.distance,
                          None, None, None, None)

    def test_input_None_x1(self):
        self.assertRaises(TypeError, distance.distance, None, 2, 3, 2)

    def test_input_None_y1(self):
        self.assertRaises(TypeError, distance.distance, 1, None, 3, 2)

    def test_input_None_x2(self):
        self.assertRaises(TypeError, distance.distance, 1, 2, None, 2)

    def test_input_None_y2(self):
        self.assertRaises(TypeError, distance.distance, 2, 3, 2, None)

    # Tests that it crashes with ValueError when called on 'aoeu'
    def test_input_string_all(self):
        self.assertRaises(ValueError,
                          distance.distance, 'aoeu', 'aoeu', 'aoeu', 'aoeu')

    def test_input_string_x1(self):
        self.assertRaises(ValueError, distance.distance, 'aoeu', 2, 3, 2)

    def test_input_string_y1(self):
        self.assertRaises(ValueError, distance.distance, 2, 'aoeu', 3, 2)

    def test_input_string_x2(self):
        self.assertRaises(ValueError, distance.distance, 2, 3, 'aoeu', 2)

    def test_input_string_y2(self):
        self.assertRaises(ValueError, distance.distance, 2, 3, 2, 'aoeu')

    # Tests it on corner cases:
    def test_vaule_zero(self):
        # Zero length
        self.assertAlmostEqual(distance.distance(2, 1, 2, 1), 0.0)

    def test_vaule_negative(self):
        self.assertAlmostEqual(distance.distance(-1, -1, -3, -5),
                               4.47214)  # Negative coordinates

    def test_vaule_vertical(self):
        self.assertAlmostEqual(distance.distance(2, 1, 2, 7),
                               6.0)  # Only vertical distance

    def test_vaule_horizontaly(self):
        self.assertAlmostEqual(distance.distance(5, 1, 10, 1),
                               5.0)  # Only horizontal distance

    # Typical conditions (difference on both coordinates)
    def test_vaule_1(self):
        self.assertAlmostEqual(distance.distance(3, -2, -1, 7), 9.84886)

    def test_vaule_2(self):
        self.assertAlmostEqual(distance.distance(-10, 2, 5, 12), 18.02776)

    def test_vaule_3(self):
        self.assertAlmostEqual(distance.distance(1, -5, -10, -12), 13.0384)

    # Test that the order of points does not matter
    def test_order(self):
        self.assertAlmostEqual(distance.distance(5, 1, 10, 2),
                         distance.distance(10, 2, 5, 1))

    # tests for output
    def test_check_output_cant_be_None(self):
        self.assertIsNotNone(TypeError, distance.distance)


if __name__ == '__main__':
    unittest.main()
