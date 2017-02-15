"""Checks if an entered string is a palindrome, excluding spaces."""

import string

print("Type out a string, and this will determine if it is palindromic.")

userInput = raw_input()
isPalindrome = 'true'
userInput = userInput.translate(None, string.punctuation)
userInput = userInput.replace(" ", "").lower()
for i in range(len(userInput)):
    if userInput[i] != userInput[len(userInput)-1-i]:
        isPalindrome = 'false'
        print 'Failing letters: ', userInput[i], userInput[len(userInput)-1-i]

print isPalindrome
