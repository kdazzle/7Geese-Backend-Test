import unittest

import code_challenge


class TestIsPalindrome(unittest.TestCase):
    """
    The `code_challenge.is_palindrome()` knows what is and isn't a palindrome
    """

    def test_single_digit_is_palindrome(self):
        """A single-digit number is a palindrome"""
        self.assertTrue(code_challenge.is_palindrome(9))

    def test_zero_is_palindrome(self):
        """Zero is a palindrome"""
        self.assertTrue(code_challenge.is_palindrome(0))

    def test_invalid_palindrome(self):
        """Some number is not a palindrome"""
        self.assertFalse(code_challenge.is_palindrome(10))

    def test_negative_number_is_not_a_palindrome(self):
        """A negative number is not a palindrome"""
        self.assertFalse(code_challenge.is_palindrome(-2))

    def test_valid_palindromes(self):
        """
        These numbers are all valid palindromes. If we used nose, we could use
        test generators so each number would be in a separate test.
        """
        valid_palindromes = [11, 121, 484, 1001, 10201, 1367631, 1004006004001]
        for number in valid_palindromes:
            self.assertTrue(code_challenge.is_palindrome(number))

    def test_invalid_palindromes(self):
        """None of these numbers should be considered palindromes"""
        invalid_palindromes = [12, 122, 485, 1002, 10202, 1367630, 1004006004000]
        for number in invalid_palindromes:
            self.assertFalse(code_challenge.is_palindrome(number))


class TestFindClosestPalindromes(unittest.TestCase):
    """We find the closest palindrome(s) of a number"""

    def test_one_below(self):
        """There is a palindrome directly below the given lesser number"""
        expected = (22, None)
        actual = code_challenge.find_closest_palindrome(23, 25)
        self.assertEquals(expected, actual)

    def test_one_above(self):
        """There is a palindrome directly above the given greater number"""
        expected = (None, 22)
        actual = code_challenge.find_closest_palindrome(19, 21)
        self.assertEquals(expected, actual)

    def test_equal_palindrome(self):
        """The given numbers are already a palindrome"""
        expected = (22, 22)
        actual = code_challenge.find_closest_palindrome(22, 22)
        self.assertEqual(expected, actual)

    def test_negative(self):
        """Test finding a palindrome from negative numbers"""
        expected = (None, 0)
        actual = code_challenge.find_closest_palindrome(-2, -1)
        self.assertEqual(expected, actual)

    def test_equidistant(self):
        """Greater and lesser palindromes are both returned"""
        expected = (9, 11)
        actual = code_challenge.find_closest_palindrome(10, 10)
        self.assertEqual(expected, actual)

    def test_high_number_lesser_palindrome(self):
        """Find the closest palindrome from an arbitrary large number"""
        expected = (12000021, None)
        actual = code_challenge.find_closest_palindrome(12000223, 12000225)
        self.assertEqual(expected, actual)

    def test_high_number_greater_palindrome(self):
        """Find the closest palindrome from an arbitrary large number"""
        expected = (None, 123321)
        actual = code_challenge.find_closest_palindrome(123300, 123302)
        self.assertEqual(expected, actual)

    def test_high_number_equidistant_palindrome(self):
        """
        Find the closest equidistant palindromes from an arbitrary large number.
        I found that these were equidistant totally by chance.
        """
        expected = (9927299, 9929299)
        actual = code_challenge.find_closest_palindrome(9928298, 9928300)

        lesser_difference = abs(9928298 - 9927299)
        greater_difference = abs(9928300 - 9929299)

        self.assertEqual(expected, actual)
        self.assertEqual(lesser_difference, greater_difference)


if __name__ == '__main__':
    unittest.main()
