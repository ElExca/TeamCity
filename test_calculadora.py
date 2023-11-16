
import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)

    def test_restar(self):
        self.assertEqual(restar(7, 2), 5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 6), 24)

    def test_dividir(self):
        self.assertEqual(dividir(8, 4), 2)
        with self.assertRaises(ValueError):
            dividir(6, 0)

if __name__ == '__main__':
    unittest.main()
