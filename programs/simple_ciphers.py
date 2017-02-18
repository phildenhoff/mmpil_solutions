"""Implementation of Vignere and Caeser ciphers."""
import sys  # for hard exits

STR_HOW_TO_ENC = "    To encrypt using the %s Cipher, type a phrase and the \
%s you'd like to use on seperate lines."

STR_HOW_TO_DEC = "    To decrypt using the %s Cipher, type a phrase and the \
%s you'd like to use on seperate lines."  # %s = method, %s = key type

STR_FORMS_OF_CRYPT = "    [V]ignere, V[e]rnam, or [C]aeser?"


# Pretty sure this method is fucked. It doesn't, or does, preserve spaces
# in some fuckled up way.
# Blatantly ripped from
# http://codereview.stackexchange.com/questions/67502/defining-functions-in-vigenere-cipher
def vignere(message, key):
    """Encrypt word with Vignere cihper."""
    mnum = [letter_to_number(x) for x in message]
    knum = [letter_to_number(x) for x in key]
    return ''.join([number_to_letter(mnum[i] + knum[i % len(key)])
                   for i in range(len(message))])


def letter_to_number(letter):
    """Convert a letter to it's ASCII num values."""
    return ord(letter) - ord('a')


def number_to_letter(number):
    """Convert a number to it's ASCII character value."""
    return chr(number % 26 + ord('a'))


def caeser(message, difference):
    """Encrypt word with Caeser cihper."""
    message_ciphered = ''.join(list(map(lambda x: caeser_letter(x, difference),
                                    message)))
    return message_ciphered


def caeser_letter(letter, difference):
    """Encrypt a letter using Caeser cipher."""
    if ord(letter)+difference > 122:
        return chr(ord(letter)+difference-26)
    if ord(letter)+difference < 97:
            return chr(ord(letter)+difference+26)
    else:
        return chr(ord(letter)+difference)


def crypt(encOrDec):
    """Method for encryption/decryption using three different forms."""
    # Get form of encryption
    print STR_FORMS_OF_CRYPT
    inputOK = 'false'
    cryption_method = ''
    while inputOK != 'true':
        inputForm = raw_input()
        if inputForm[0].lower() == 'v':
            cryption_method = 'vignere'
            key_type = 'alphabetical key'
            break
        if inputForm[0].lower() == 'e':
            print "This is not implemented yet."
            sys.exit()
            break
        if inputForm[0].lower() == 'c':
            cryption_method = 'caeser'
            key_type = 'numerical key'
            break
        else:
            print "You must enter \"v\", \"e\", or \"c\"."
    # Print instruction for encryption or decryption
    if encOrDec == 'enc':
        print STR_HOW_TO_ENC % (cryption_method.capitalize(), key_type)
    else:
        print STR_HOW_TO_DEC % (cryption_method.capitalize(), key_type)

    userInput = raw_input().split()
    # Caeser requires a num key, vignere requries a str key
    if cryption_method == 'caeser' or cryption_method == 'vignere':
        key = str(raw_input())
        if cryption_method == 'caeser':
            key = int(key)
            if encOrDec == 'dec':
                key *= -1  # decryption requires reversing key motion
    words_ciphered = ' '.join(list(map((lambda x: globals()[cryption_method]
                                       (x, key)), userInput)))
    print "    Your %s phrase is" % ('encrypted' if encOrDec == 'enc' else
                                     'decrypted')
    print words_ciphered


print "    [E]ncrypt or [D]ecrypt?"
inputOK = 'false'
# Enter ENC/DEC
while inputOK != 'true':
    inputEncDec = raw_input()
    if inputEncDec[0].lower() == 'e':
        crypt('enc')
        break
    if inputEncDec[0].lower() == 'd':
        crypt('dec')
        break
    else:
        print "    You must input \"e\" or \"d\"."
