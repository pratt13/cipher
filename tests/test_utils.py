import unittest
import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from Utils import UtilMixin

# from ..Utils import UtilMixin


class UtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.utils = UtilMixin()

    def test_shuffle_letter(self):
        for (idx, expected_result) in [(4, "E"), (0, "A"), (-1, "Z")]:
            with self.subTest("Capital subtest", idx=idx, expected_result=expected_result):
                self.assertEqual(self.utils.shuffle_letter("A", idx), expected_result)

        for (idx, expected_result) in [(4, "g"), (0, "c"), (-1, "b")]:
            with self.subTest("Capital subtest", idx=idx, expected_result=expected_result):
                self.assertEqual(self.utils.shuffle_letter("c", idx), expected_result)

        with self.assertRaises(
            ValueError, msg="Unable to shuffle amount by '100' as it is greater than 26"
        ):
            self.utils.shuffle_letter("c", 100)

    def test_shuffle_str_by_n(self):
        # Simple shuffle
        self.assertEqual(self.utils.shuffle_str_by_n(["AB", "Cd"], 2), "CD Ef")

        # Shuffle with spaces and chars
        self.assertEqual(self.utils.shuffle_str_by_n(["AB +=g", "CD"], 2), "CD +=i EF")

        # Shuffle by more than 26
        self.assertEqual(self.utils.shuffle_str_by_n(["AB +=g", "CD"], 28), "CD +=i EF")


if __name__ == "__main__":
    unittest.main()
