import unittest
from math import isclose
from PruebaLogica import Calculadora

class PruebaUnitaria1(unittest.TestCase):
    def test_suma(self):
        calculadora = Calculadora("2+3")
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, 5)

    def test_resta(self):
        calculadora = Calculadora("7-4")
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, 3)
    
    def test_multiplicacion(self):
        calculadora = Calculadora("5*4")
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, 20)  
    
    def test_division(self):
        calculadora = Calculadora("5/5")
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, 1)  
    
    def test_potencia(self):
        calculadora = Calculadora("2^3")
        resultado = calculadora.resolver_operacion()
        self.assertEqual(resultado, 8)

    def test_raiz_cuadrada(self):
        calculadora = Calculadora("√(16)")
        resultado = calculadora.resolver_operacion()
        self.assertTrue(isclose(resultado, 4))
        
if __name__ == "__main__":
    unittest.main()
