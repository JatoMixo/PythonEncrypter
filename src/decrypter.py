import encrypter

class Decrypter:

  def CesarDecryption(self, message, jumps):
    return encrypter.Encrypter().CesarEncryption(message, -jumps)