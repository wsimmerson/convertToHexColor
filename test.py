import unittest
from convertToHexColor import convertToHexColor

class TestStringMethods(unittest.TestCase):

    def test_should_be_seven_characters(self):
        self.assertEqual(len(convertToHexColor("")), 7)
        self.assertEqual(len(convertToHexColor("John Doe")), 7)
        self.assertEqual(len(convertToHexColor("Trouble with Tribbles")), 7)
        self.assertEqual(len(convertToHexColor("Mars Attacks")), 7)

    def test_should_have_consistend_results(self):
        self.assertEqual(convertToHexColor("John Doe"), convertToHexColor("John Doe"))
    
    def test_should_start_with_hashtag(self):
        color = convertToHexColor("And now for something completely different")
        self.assertTrue(color.startswith("#"))

if __name__ == '__main__':
    unittest.main()