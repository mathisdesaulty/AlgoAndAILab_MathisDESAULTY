"""
Unit tests for the MathTool class.

This module contains test cases for the methods of the MathTool class,
specifically the calculate_one_way_distance and hausdorff_distance methods.
The tests cover various scenarios including normal operation, edge cases,
and invalid inputs.
"""

import unittest
import numpy as np
from Object.math_tool import MathTool

class TestMathTool(unittest.TestCase):
    """
    Test cases for the MathTool class.
    """
    def setUp(self):
        """
        Method executed before each test.
        """

    def test_calculate_one_way_distance_correct_output(self):
        """
        Test that calculate_one_way_distance produces the expected output for specific data.
        """
        coords1 = np.array([[0, 0], [1, 1]])
        coords2 = np.array([[1, 0], [0, 1]])
        image1 = np.array([[1, 0], [0, 1]])
        image2 = np.array([[0, 1], [1, 0]])
        expected_output = 1
        result = MathTool.calculate_one_way_distance(coords1, coords2, image1, image2)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_calculate_one_way_distance_edge_cases(self):
        """
        Test edge cases for calculate_one_way_distance.
        """
        # Identical points
        coords1 = np.array([[0, 0]])
        coords2 = np.array([[0, 0]])
        image1 = np.array([[1, 0], [0, 1]])
        image2 = np.array([[0, 1], [1, 0]])
        expected_output = 1
        result = MathTool.calculate_one_way_distance(coords1, coords2, image1, image2)
        self.assertEqual(result, expected_output)

    def test_hausdorff_distance_correct_output(self):
        """
        Test that hausdorff_distance produces the expected output for specific data.
        """
        image1 = np.array([[1, 0], [0, 1]])
        image2 = np.array([[0, 1], [1, 0]])
        expected_output = 1  # Maximum distance between non-matching points
        result = MathTool.hausdorff_distance(image1, image2)
        self.assertAlmostEqual(result, expected_output, places=6)

    def test_hausdorff_distance_edge_cases(self):
        """
        Test edge cases for hausdorff_distance.
        """
        # Both images are empty
        image1 = np.array([[]])
        image2 = np.array([[]])
        expected_output = 0
        result = MathTool.hausdorff_distance(image1, image2)
        self.assertEqual(result, expected_output)

        # One image is empty
        image1 = np.array([[1, 1], [1, 1]])
        image2 = np.array([[]])
        expected_output = np.inf
        result = MathTool.hausdorff_distance(image1, image2)
        self.assertEqual(result, expected_output)

        # Identical images
        image1 = np.array([[1, 1], [1, 1]])
        image2 = np.array([[1, 1], [1, 1]])
        expected_output = 0
        result = MathTool.hausdorff_distance(image1, image2)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
