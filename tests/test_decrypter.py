import unittest
import sys
sys.path.insert(0, "/home/jatomixo/Code/PythonEncrypter")
from src.decrypter import *

class TestDecrypter(unittest.TestCase):

  def set_defaults(self):
    self.decrypter = Decrypter()

  def test_cesar(self):
    self.assertEqual()