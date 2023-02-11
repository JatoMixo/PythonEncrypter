import unittest
import sys
sys.path.insert(0, "D:/Miguel/Programas/PythonEncrypter")
from src.decrypter import *

class TestDecrypter(unittest.TestCase):

  def set_defaults(self):
    self.decrypter = Decrypter()

  def test_cesar(self):
    self.set_defaults()
    self.assertEqual("ABCDE", self.decrypter.cesar_decryption("BCDEF", 1))
    self.assertEqual("ABCDE", self.decrypter.cesar_decryption("DEFGH"))

  def test_binary_decryption(self):
    self.set_defaults()
    self.assertEqual(self.decrypter.binary_decryption("1000010 1101001 1101110 1100001 1110010 1111001 100000 1100011 1101111 1101111 1101100"), "Binary cool")
    self.assertEqual(self.decrypter.binary_decryption("1000001"), "A")
  
  def test_numeral_decryption(self):
    self.set_defaults()
    pass

  def test_reverse_encryption(self):
    self.set_defaults()
    self.assertEqual(self.decrypter.reverse_decryption("TSET"), "TEST")
    self.assertEqual(self.decrypter.reverse_decryption("TSET TON", True), "TEST NOT")

unittest.main()