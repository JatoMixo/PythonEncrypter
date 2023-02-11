from src import encrypter
from src import words_parser
from math import pow

class Decrypter:

  def cesar_decryption(self, message, jumps=3):
    return encrypter.Encrypter().cesar_encryption(message, -jumps)

  def binary_decryption(self, message):
    binary_parsed = words_parser.parse_words(message)
    decrypted_message = ""

    # Generate words
    for binary in range(len(binary_parsed)):
      actual_char = 0
      for i in range(len(binary_parsed[binary])):
        actual_char += int(binary_parsed[binary][i]) * pow(2, len(binary_parsed[binary]) - (i + 1))
      
      decrypted_message += chr(int(actual_char))
      
      if len(decrypted_message) - 1 != binary:
        decrypted_message += " "
    
    return decrypted_message
  
  def reverse_decryption(self, message,  only_words=False):
    return encrypter.Encrypter().reverse_encryption(message, only_words)