import unittest
import sys
sys.path.insert(0, "D:/Miguel/Programas/PythonEncrypter")
from src.encrypter import * 

class TestEncrypter(unittest.TestCase):

  def set_defaults(self):
    self.encrypter = Encrypter()

  def test_cesar_encryption(self):
    self.set_defaults()
    self.assertEquals("DEFGH", self.encrypter.CesarEncryption("ABCDE"))
    self.assertEquals("BCDEF", self.encrypter.CesarEncryption("ABCDE", 1))

  def test_binary_encryption(self):
    self.set_defaults()
    self.assertEqual("1000010 1101001 1101110 1100001 1110010 1111001 100000 1100011 1101111 1101111 1101100", self.encrypter.BinaryEncryption("Binary cool"))
    self.assertEqual("1000001", self.encrypter.BinaryEncryption("A"))


unittest.main()