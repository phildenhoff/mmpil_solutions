"""Implementation of Vignere and Caeser ciphers."""


# STR_HOW_TO = ""

def vignere(word):
    """Encrypt word with Vignere cihper."""
    print word


def caeser(word, difference):
    """Encrypt word with Caeser cihper."""
    word_ciphered = ''.join(list(map(lambda x: caeser_letter(x, difference),
                                 word)))
    return word_ciphered


def caeser_letter(letter, difference):
    """Encrypt a letter using Caeser cipher."""
    if ord(letter)+difference > 122:
        return chr(ord(letter)+difference-26)
    if ord(letter)+difference < 97:
            return chr(ord(letter)+difference+26)
    else:
        return chr(ord(letter)+difference)


print "    [E]ncrypt or [D]ecrypt?"
inputOK = 'false'
while inputOK != 'true':
    userInput = raw_input()
    if userInput[0].lower() == "e":
        print "    To encrypt using the Caeser Cipher, type a phrase and the\
 offset you'd like to use on seperate lines."
        userInput = raw_input().split()
        userDiff = int(raw_input())
        inputOK = 'true'
        words_ciphered = ' '.join(list(map((lambda x: caeser(x, userDiff)),
                                           userInput)))
        print "    Your encrypted phrase is"
        print words_ciphered
        break
    if userInput[0].lower() == "d":
        print "    To decrypt using the Caeser Cipher, type a phrase and the\
 offset you'd like to reverse on seperate lines."
        userInput = raw_input().split()
        userDiff = int(raw_input())
        inputOK = 'true'
        words_ciphered = ' '.join(list(map((lambda x: caeser(x, -userDiff)),
                                           userInput)))
        print "    Your decrypted phrase is"
        print words_ciphered
        break
    else:
        print "    You must input \"e\" or \"d\"."
