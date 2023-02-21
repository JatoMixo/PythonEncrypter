from math import floor
from words_parser import parse_words
from morse_translated import morse_translation

def process_last_element(index, array, addition):

  IS_LAST_ELEMENT = index == len(array) - 1

  if not(IS_LAST_ELEMENT):
    return addition
  
  return ""

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

    if jumps == '':
      jumps = 0

    jumps = int(jumps)
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
  
  def reverse_encryption(self, message, only_words=False):
    
    encrypted_message = ""

    if not(only_words):
      for i in range(len(message)):
        encrypted_message += message[len(message) - (i + 1)]
      
      return encrypted_message
    
    words = parse_words(message)
    for i in range(len(words)):
      encrypted_message += self.reverse_encryption(words[i])
      if i != len(words) - 1:
        encrypted_message += " "


    return encrypted_message
  
  def morse_encryption(self, message):

    encrypted_message = ""
    words_parsed = parse_words(message)

    for index_of_word in range(len((words_parsed))):

      word = words_parsed[index_of_word]

      for index, char in enumerate(word):
        encrypted_message += morse_translation[char.upper()] + process_last_element(index, word, " ")

      encrypted_message += process_last_element(index_of_word, words_parsed, "  ") 

    return encrypted_message
  
  def wave_encryption(self, message, key):

    if key == "":
      raise Exception("Invalid key.")

    encrypted_message = ""

    for index, character in enumerate(message):

      if character == " ":
        encrypted_message += process_last_element(index, message, " ")
        continue

      encrypted_message += str(int(ord(character) + pow(ord(key[index % len(key)]), 2))) + process_last_element(index, message, " ")
    
    return encrypted_message