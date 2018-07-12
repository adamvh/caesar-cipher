""" 
    Name:           Adam Hudson
    Date:           2018-07-12
    Program Name:   encrypt-message.py
    Description:    This program will receive a text file and encrypt the message using the 
                    caesar-cypher method. The encrypted message will go into a new file called 
                    [filename].caesar
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
    
    # Write the new file with the new file extension ".caesar"
    newFile = open( fileinput.filename() + ".caesar", "w" )

for line in data:
    for char in line:

        # Check for special characters because they cannot be encrypted
        if char == ' ' or char == '\n' or char in set(punctuation):
            newFile.write(char)
        
        else:
            # This is the encryption logic
            newIndex = alphabet.index(char) - shift
            
            # If the encryption leaves the scope of the array, continue at the end of the array
            if newIndex < 0:
                newIndex = len(alphabet) + newIndex
            
            # Write the encrypted value to the new file
            newFile.write( alphabet[newIndex] )
