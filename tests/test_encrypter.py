import unittest
import sys
# sys.path.insert(0, "D:/Miguel/Programas/PythonEncrypter")
from src.encrypter import * 

class TestEncrypter(unittest.TestCase):

  def set_defaults(self):
    self.encrypter = Encrypter()

  def test_cesar_encryption(self):
    self.set_defaults()
    self.assertEquals("DEFGH", self.encrypter.cesar_encryption("ABCDE"))
    self.assertEquals("BCDEF", self.encrypter.cesar_encryption("ABCDE", 1))

  def test_binary_encryption(self):
    self.set_defaults()
    self.assertEqual("1000010 1101001 1101110 1100001 1110010 1111001 100000 1100011 1101111 1101111 1101100", self.encrypter.binary_encryption("Binary cool"))
    self.assertEqual("1000001", self.encrypter.binary_encryption("A"))

  def test_numeral_encryption(self):
    self.set_defaults()
    self.assertEqual(self.encrypter.numeral_encryption("Testing tests"), "54 65 73 74 69 6e 67 20 74 65 73 74 73")
    self.assertEqual(self.encrypter.numeral_encryption("A", 10, 2), "1000001")
    self.assertEqual(self.encrypter.numeral_encryption(""), "")
  
  def test_reverse_string(self):
    self.set_defaults()
    self.assertEqual(self.encrypter.reverse_encryption("ABCD EFGH"), "HGFE DCBA")
    self.assertEqual(self.encrypter.reverse_encryption("ABCD EFGH", True), "DCBA HGFE")
  
  def test_morse_encryption(self):
    self.set_defaults()
    self.assertEqual(self.encrypter.morse_encryption("ABC DE"), ".- -... -.-.  -.. .")
    self.assertEqual(self.encrypter.morse_encryption("test 2"), "- . ... -  ..---")

unittest.main()