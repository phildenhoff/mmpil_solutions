"""Turn a given string into Pig Latin"""

def piggify(word):
	# starts with vowek
	if word[0].lower() in vowels:
		return word+"way"
	# starts with consonant cluster
	if word[0:2].lower() in clusters:
		return word[2:len(word)]+word[0:2]+"ay"
	# starts with consonant
	else:
		return word[1:len(word)]+word[0]+"ay"


print "Type a string to convert to pig latin"
userInput = raw_input()
wordList = userInput.split()
vowels = ['a', 'e', 'i', 'o', 'u']
clusters = ['ch', 'sh','sm']
piggedWordList = []

for word in wordList:
	piggedWordList.append(piggify(word))

piggedSentence = " ".join(piggedWordList)

print piggedSentence
