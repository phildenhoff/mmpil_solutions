"""Counts the number of vowels in stdin."""

import sys
print "Input a string, and the vowels will be counted."
userInput = raw_input()
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for i in range(len(userInput)):
    if userInput[i] in vowels:
        vowelCount[userInput[i]] += 1
print "The final vowel count is"
print " ".join([str(x) for x in vowels])
for vowel in vowels:
    sys.stdout.write(str(vowelCount[vowel]))
    sys.stdout.write(' ')
sys.stdout.write('\n')
