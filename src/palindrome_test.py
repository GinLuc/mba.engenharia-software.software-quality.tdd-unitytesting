import unittest
from palindrome_code import getPalindrome


palindrome_words = ["Rotator", "bob", "madam", 
"mAlAyAlam", "1", "Able was I, ere I saw Elba", 
"Madam I'm Adam", "Step on no pets.", "Top spot!", "02/02/2020", "Socorram me subi no onibus em marrocos"]
normal_words = ["xyz", "elephant", "Country","Top . post!", "Wonderful-fool", "Wild imagination!"]

class TestPalindrome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.palindrome_words = palindrome_words
        self.normal_words = normal_words

    def test_palindrome_words(self):
        for word in self.palindrome_words:
            palindrome_words = getPalindrome(word)   
            self.assertEqual(palindrome_words[1], palindrome_words[0], "Não são palíndromos")

    @unittest.expectedFailure
    def test_normal_words(self):
        for word in self.normal_words:
            palindrome_words = getPalindrome(word)   
            self.assertEqual(palindrome_words[1], palindrome_words[0], "Não são palíndromos")

if __name__ == '__main__':
    unittest.main()