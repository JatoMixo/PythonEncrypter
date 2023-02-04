class Encrypter:

  def CesarEncryption(message, jumps=3):

    new_message = ""

    for i in message:
      new_message += str(i + chr(jumps))

    return new_message