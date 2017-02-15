"""Reverses a stdin string."""

print("What string would you like to reverse?")
userInput = raw_input()
reverseInput = ""
for i in range(len(userInput)):
    reverseInput += userInput[len(userInput)-1-i]
print reverseInput
