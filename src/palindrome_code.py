
palindrome_words = ["Rotator", "bob", "madam", 
"mAlAyAlam", "1", "Able was I, ere I saw Elba", 
"Madam I'm Adam", "Step on no pets.", "Top spot!", "02/02/2020", "Socorram-me subi no onibus em marrocos"]

special_char = (" ", ".", "'", "/", ",","-", "!")

def getPalindrome(word):
    # Removing all Special Characters
    for char in special_char:
        word = word.replace(char, "")
    
    # Returning the original lower word and his palindrome
    return (word.lower(), word[::-1].lower())
    

if __name__ == '__main__':
    # Test Drive
    for word in palindrome_words:
        new_word = getPalindrome(word)
        print(new_word)