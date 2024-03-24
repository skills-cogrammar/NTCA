import unittest
from caesar_cipher import *

'''
Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Shift: 23
Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

Text : ATTACKATONCE
Shift: 4
Cipher: EXXEGOEXSRGI
'''

class TestCaesarCipher(unittest.TestCase):
    
    def test_encrypt_returns_correct_result(self):
        # Arrage 
        input_text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shift = 23

        # Act
        actual = encrypt(input_text, shift)

        # Assert
        expected = 'XYZABCDEFGHIJKLMNOPQRSTUVW'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()