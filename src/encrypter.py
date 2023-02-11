from math import floor
from src import words_parser

def decimal_to_binary(decimal):

  binary = ""

  while decimal > 0:
    if decimal % 2 == 0:
      binary = "0" + binary
    else:
      binary = "1" + binary
    
    decimal = floor(decimal / 2)
  
  return binary

class Encrypter:

  def cesar_encryption(self, message, jumps=3):

    new_message = ""

    for i in message:
      new_message += chr(ord(i) + jumps)

    return new_message

  def binary_encryption(self, message):

    binary = ""

    for i in message:
      binary += decimal_to_binary(ord(i))
      if message.index(i) != len(message) - 1:
        binary += " "
    
    return binary
  
  '''def numeral_encryption(self, message, original_base=10, new_base=16):

    encrypted_message = ""

    for i in message:
      encrypted_message += str(ord(i))
      if message.index(i) != len(message) - 1:
        encrypted_message += " "

    return encrypted_message'''

  def reverse_encryption(self, message, only_words=False):
    
    encrypted_message = ""

    if not(only_words):
      for i in range(len(message)):
        encrypted_message += message[len(message) - (i + 1)]
      
      return encrypted_message
    
    words = words_parser.parse_words(message)
    for i in range(len(words)):
      encrypted_message += self.reverse_encryption(words[i])
      if i != len(words) - 1:
        encrypted_message += " "


    return encrypted_message