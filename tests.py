import unittest
import cap

class TestCap(unittest.TestCase):

    def setUp(self):
        # Called before each test method
        # Allocates exteneral resources used by tests
        # Like database connections or test data
        pass

    def tearDown(self):
        # Run after each test method
        # Deallocates resources
        pass

    def test_one_word(self):
        text = 'duck'
        result = cap.capitalizer(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = cap.capitalizer(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')

    def test_words_with_apostrophes (self):
        text = "\"did they get 'em?\", he asked."
        result = cap.capitalizer(text)
        self.assertEqual(result, "\"Did They Get 'Em?\", He Asked.")

    def test_words_with_quotes(self):
        text = "\"you're awesome,\" said daffy duck"
        result = cap.capitalizer(text)
        self.assertEqual(result, "\"You're Awesome,\" Said Daffy Duck")


if __name__ == '__main__':
    unittest.main()
