import unittest 
from reverse_int import ReverseInt


class TestReverseInt(unittest.TestCase):
    def setUp(self) -> None:
        self.reverse_logic = ReverseInt()

    def test_get_reversed_int_value_is_backwards(self):
        # Arrage 
        intial_value = 123

        # Act
        actual = self.reverse_logic.get_reversed_int(intial_value)

        # Assert
        expected = 321
        self.assertEqual(actual, expected, f'Expected to get {expected} but got {actual}')

    def test_get_reversed_int_should_be_integer(self):
        # Arrage 
        intial_value = 123

        # Act
        actual = self.reverse_logic.get_reversed_int(intial_value)

        # Assert
        self.assertIsInstance(actual, int, f'Expected type int but got {type(actual)}')

    def test_get_reversed_int_returns_negative(self):
        # arrage 
        intial_value = -123

        # act 
        actual = self.reverse_logic.get_reversed_int(intial_value)

        # Assert
        expected = -321
        self.assertEqual(actual, expected, f'Expected Negative value, got positive')




if __name__ == '__main__':
    unittest.main()