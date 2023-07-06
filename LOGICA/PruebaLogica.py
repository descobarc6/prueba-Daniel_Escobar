import math
class Calculadora:
    def __init__(self, expresion):
        self.expresion = expresion

    def resolver_operacion(self):
        if len(self.expresion) > 20:
            raise ValueError('La longitud máxima de la expresión debe ser de 20 caracteres')
        resultado = self.evaluar_expresion(self.expresion)
        return resultado

    def evaluar_expresion(self, expresion):
        operandos = []
        operadores = []
        numero = ''

        for caracter in expresion:
            if caracter.isdigit() or caracter == '.':
                numero += caracter
            else:
                if numero:
                    operandos.append(float(numero))
                    numero = ''

                if caracter == '(':
                    operadores.append(caracter)
                elif caracter == ')':
                    while operadores[-1] != '(':
                        self.operar(operandos, operadores)
                    operadores.pop()
                elif caracter in '+-*/^√':
                    while operadores and self.prioridad_operador(caracter, operadores[-1]):
                        self.operar(operandos, operadores)
                    operadores.append(caracter)

        if numero:
            operandos.append(float(numero))

        while operadores:
            self.operar(operandos, operadores)

        return operandos[0]

    def prioridad_operador(self, operador1, operador2):
        prioridad = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 3, '(': 0}
        return prioridad[operador1] <= prioridad[operador2]

    def operar(self, operandos, operadores):
        operador = operadores.pop()
        if operador == '√':
            operando = operandos.pop()
            resultado = math.sqrt(operando)
        else:
            segundo_operando = operandos.pop()
            primer_operando = operandos.pop()

        if operador == '+':
            resultado = primer_operando + segundo_operando
        elif operador == '-':
            resultado = primer_operando - segundo_operando
        elif operador == '*':
            resultado = primer_operando * segundo_operando
        elif operador == '/':
            if segundo_operando == 0:
                raise ValueError('No se puede dividir por cero.')
            resultado = primer_operando / segundo_operando
        elif operador == '^':
                resultado = primer_operando ** segundo_operando
        operandos.append(resultado)

if __name__ == "__main__":
    expresion = input("Ingrese la operacion matematica: ")
    calculadora = Calculadora(expresion)
    try:
        resultado = calculadora.resolver_operacion()
        print("El resultado es:", resultado)
    except ValueError as e:
        print("Error:", str(e))