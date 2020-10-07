#example 1 of raising errors 
def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    #first try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

### try exercute a code, if failed raises the error we mentioned and return None

    #Now process the file
    character = {}
    for line in f:
        for char in line:
            character[char] = characters.get(char, 0) + 1

    f.close()
    return characters


#example 2 

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

#example 3

import unittest

from file import file function

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(file function("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(file function("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(file function("invalid user", 1). False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, file function, "user", -1)

unittest.main()
