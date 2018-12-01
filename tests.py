import unittest
import cap


class TestCap(unittest.TestCase):

    def setUp(self):
        """
        The setup is called before each test method.
        It allocates external resources used by tests,
        like database connections or test data. 
        You can do this lab without a `setUp`.
        """
        pass

    def tearDown(self):
        """
        The tearDown is called after each test method, and can be 
        used to deallocate resources and close connections.
        You can do this lab without a `tearDown`.
        """
        pass

    def test_one_word(self):
        text = 'spam'
        result = cap.capitalizer(text)
        self.assertEqual(result, 'Spam')

    def test_multiple_words(self):
        text = 'so much spam'
        result = cap.capitalizer(text)
        self.assertEqual(result, 'So Much Spam')

    def test_words_with_apostrophes (self):
        text = "\"did they find 'em?\", he asked."
        result = cap.capitalizer(text)
        self.assertEqual(result, "\"Did They Find 'Em?\", He Asked.")
        
    def test_leading_number(self):
        text = "the 49ers organize"
        result = cap.capitalizer(text)
        self.assertEqual(result, "The 49ers Organize")

    def test_words_with_quotes(self):
        text = "\"we're on our way,\" she replied"
        result = cap.capitalizer(text)
        self.assertEqual(result, "\"We're On Our Way,\" She Replied")
        
    def test_leading_at_sign(self):
        text = "Username: @maya"
        result = cap.capitalizer(text)
        self.assertEqual(result, "Username: @Maya")
       
    def test_all_sym(self):
        text = "!@#$%"
        result = cap.capitalizer(text)
        self.assertEqual(result, "!@#$%")

    def test_empty_str(self):
        result = cap.capitalizer("")
        self.assertEqual(result, "")

    def test_all_nums(self):
        result = cap.capitalizer("1234 n college ave.")
        self.assertEqual(result, "1234 N College Ave.")

if __name__ == '__main__':
    unittest.main()
