from src.encrypter import Encrypter
from src.morse_translated import morse_translation
from src.words_parser import parse_words
from src.element_finder import find_by_second_element
from math import pow

class Decrypter:

  def cesar_decryption(self, message, jumps=3):
    return Encrypter().cesar_encryption(message, -jumps)

  def binary_decryption(self, message):
    binary_parsed = parse_words(message)
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
    return Encrypter().reverse_encryption(message, only_words)
  
  def morse_decryption(self, message):

    decrypted_message = ""

    morse_parsed = parse_words(message)

    for morse_char in morse_parsed:
      if morse_char == "":
        decrypted_message += " "
        continue

      decrypted_message += find_by_second_element(morse_translation, morse_char)

    return decrypted_message