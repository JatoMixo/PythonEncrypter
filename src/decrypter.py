from src import encrypter
from math import pow

class Decrypter:

  def cesar_decryption(self, message, jumps=3):
    return encrypter.Encrypter().cesar_encryption(message, -jumps)

  def binary_decryption(self, message):
    binary_parsed = [""]
    decrypted_message = ""

    # Separate words
    for i in range(len(message)):

      if message[i] == " ":
        binary_parsed.append("")
        continue

      binary_parsed[len(binary_parsed) - 1] += message[i]
    
    # Generate words
    for binary in range(len(binary_parsed)):
      actual_char = 0
      for i in range(len(binary_parsed[binary])):
        actual_char += int(binary_parsed[binary][i]) * pow(2, len(binary_parsed[binary]) - (i + 1))
      
      decrypted_message += chr(int(actual_char))
      
      if len(decrypted_message) - 1 != binary:
        decrypted_message += " "
    
    return decrypted_message