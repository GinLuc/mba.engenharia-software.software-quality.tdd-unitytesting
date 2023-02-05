
palindrome_words = ["Rotator", "bob", "madam", 
"mAlAyAlam", "1", "Able was I, ere I saw Elba", 
"Madam I'm Adam", "Step on no pets.", "op spot!", "02/02/2020", "Socorram me subi no onibus em marrocos"]

special_char = (" ", ".", "'", "/")

def isPalindrome(s):
 
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
 
    # if length is less than 2
    if l < 2:
        return True
 
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
 
        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
 
    else:
        return False
 

if __name__ == '__main__':
    # Driver Code
    for word in palindrome_words:
        print(isPalindrome(word))
        #print("Original word: {0} \t Palindrome Word: {1}".format(word.lower(), palindrome_word.lower()))