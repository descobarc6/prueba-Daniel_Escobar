import unittest
from math import isclose
from PruebaLogica import Calculadora

class PruebaUnitaria2(unittest.TestCase):
    def test_division_por_cero(self):
        calculadora = Calculadora("10/0")
        self.assertRaises(ValueError, calculadora.resolver_operacion)

    def test_expresion_con_parentesis(self):
        calculadora = Calculadora("((2+3)*4) / (5-1)")
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, 5)

    def test_longitud_maxima(self):
        expresion = "110+20-30*40/50*√100"
        calculadora = Calculadora(expresion)
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, -110.0)

    def test_error_longitud_excedida(self):
        expresion = "123456789012345678901"
        with self.assertRaises(ValueError):
            Calculadora(expresion).resolver_operacion()

if __name__ == "__main__":
    unittest.main()
    