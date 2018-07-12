# caesar-cipher
Getting to know basic encryption with Caesar's encryption method.

### README Sections
  1. Motivation
  2. Encryption Method
  3. Program Description

## Motivation
As I dive further computer security, I need to strengthen my understanding of cryptography. I've started out by understanding Caesar cipher.

## Encryption Method
The Caesar cipher method works by replacing each plain text letter with another letter shifted by three places on the alphabet. This makes 'a' become 'x' and 'd' become 'a'

## Program Description
The program was written with Python 3.6.6. There are actually two parts to this program. The encrypt-message and decrypt-message. The program only allows ASCII text and letters a-z as well as A-Z. Numbers and special characters will not be encrypted or decrypted. To make things easier, the encrypted version of 'a' will become 'X' and so on.<br> <br>
To run this program: `$ python encrypt-message.py [message.txt]` <br>
The program will output a file called [message.txt].caesar. <br> <br>
To decrypt the message: `$ python encrypt-message.py [message.txt].caesar` <br>
The decrypted message will be outputted to the terminal window.
