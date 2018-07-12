""" 
    Name:           Adam Hudson
    Date:           2018-07-12
    Program Name:   decrypt-message.py
    Description:    This program will receive a text file and decrypt the message using the 
                    caesar-cypher method. The decrypted message will output to the terminal.
"""

# Declair imports
import fileinput
from string import punctuation

# Shift length. Default: 3
shift = 3

# list for letter translation
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# List of inputs from the file
data = []

# Get user's file from command line
with fileinput.input() as fileObject:
    for line in fileObject:
        l = list(line)
        data.append(l)

for line in data:
    for char in line:

        # Check for special characters because are not encrypted
        if char == ' ' or char == '\n' or char in set(punctuation):
            print(char, end='')
        
        else:
            # This is the decryption logic
            newIndex = alphabet.index(char) + shift
            
            # If the decryption leaves the scope of the array, continue at the start of the array
            if newIndex > (len(alphabet) - 1):
                newIndex = newIndex - len(alphabet)
            
            # Print the decryped character
            print(alphabet[newIndex], end='')
