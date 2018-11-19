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
        The tearDown is called after each test method, and can be 
        used to deallocate resources and close connections.
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
        text = "\"did they find 'em?\", he asked."
        result = cap.capitalizer(text)
        self.assertEqual(result, "\"Did They Find 'Em?\", He Asked.")

    def test_words_with_quotes(self):
        text = "\"we're on our way,\" she replied"
        result = cap.capitalizer(text)
        self.assertEqual(result, "\"We're On Our Way,\" She Replied")

    # [ADD A TEST HERE]

    # [ADD ANOTHER TEST HERE]


if __name__ == '__main__':
    unittest.main()
