import unittest
from encrypter import *

class TestEncrypter(unittest.TestCase):

  def set_defaults(self):
    self.encrypter = Encrypter()

  def test_cesar_encryption(self):
    self.set_defaults()
    self.assertEquals("DEFGH", self.encrypter.CesarEncryption("ABCDE"))
    self.assertEquals("BCDEF", self.encrypter.CesarEncryption("ABCDE", 1))


unittest.main()