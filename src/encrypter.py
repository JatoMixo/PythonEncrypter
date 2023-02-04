class Encrypter:

  def CesarEncryption(self, message, jumps=3):

    new_message = ""

    for i in message:
      new_message += chr(ord(i) + jumps)

    return new_message