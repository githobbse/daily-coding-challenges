'''
DCC: 3/19/2018
Goal: Using the Python language, have the function LongestWord(sen) take the
        sen parameter being passed and return the largest word in the string.
        If there are two or more words that are the same length, return the
        first word from the string with that length. Ignore punctuation and
        assume sen will not be empty. 
'''

def LongestWord(sen):
    words = sen.split()
    punctuation = '!@#$%^&*()_\'\"'
    longWord = ''
    for word in words:
        if len(word) > len(longWord):
            longWord = word
    return longWord

def main():
    sen = input("Please enter a string: ")
    print("Longest word: " + LongestWord(sen) + "\nLength: " + str(len(LongestWord(sen))))

main()
