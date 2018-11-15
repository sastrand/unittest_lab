import unittest
import cap


class TestCap(unittest.TestCase):

    def setUp(self):
        """
        The setup is called before each test method.
        It allocates external resources used by tests,
        like database connections or test data.
        """
        pass

    def tearDown(self):
        """
        The tearDown is called after each test method.
        It's useful to deallocates resources and close connections.
        """
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

    # [ADD A TEST HERE]

    # [ADD ANOTHER TEST HERE]


if __name__ == '__main__':
    unittest.main()
