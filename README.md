# Calculadora - Documentación
Este es un programa de calculadora que evalúa y resuelve expresiones matemáticas básicas. Puedes ingresar una expresión matemática y la calculadora devolverá el resultado de la operación.

# Algoritmo
El programa sigue los siguientes pasos para resolver la expresión matemática:

1. Se recibe una expresión matemática del usuario como entrada.
2. Se crea una instancia de la clase Calculadora con la expresión ingresada.
3. Se verifica que la longitud de la expresión no exceda los 20 caracteres. En caso de excederlo, se lanza un error ValueError.
4. Se llama al método resolver_operacion() de la instancia de Calculadora.
5. Dentro del método resolver_operacion(), se inicia la evaluación de la expresión llamando al método evaluar_expresion().
6. Se inicializan las listas operandos y operadores.
7. Se itera sobre cada caracter de la expresión:
* Si el caracter es un dígito o un punto decimal, se agrega al número en construcción.
* Si el caracter es un operador (suma, resta, multiplicación, división, potencia o raíz cuadrada), se realizan las siguientes acciones:
* Si hay un número en construcción, se agrega a la lista de operandos.
* Si el operador es un paréntesis de apertura, se agrega a la lista de operadores.
* Si el operador es un paréntesis de cierre, se realizan las siguientes acciones:
* Se realizan operaciones hasta encontrar el paréntesis de apertura correspondiente.
* Se elimina el paréntesis de apertura de la lista de operadores.
* Si el operador tiene una prioridad mayor que los operadores existentes en la lista, se agrega a la lista de operadores.
* En caso contrario, se realizan las operaciones necesarias para mantener la prioridad correcta de los operadores.
8. Si aún hay un número en construcción, se agrega a la lista de operandos.
9. Se realizan las operaciones pendientes hasta vaciar la lista de operadores.
10. Se devuelve el resultado que se encuentra en la lista de operandos.

# Ejecución del programa
Para ejecutar el programa, sigue estos pasos:

Abre una terminal o línea de comandos.
Navega hasta la ubicación del archivo que contiene el código de la calculadora.
Asegúrate de tener instalado Python en tu sistema.
Ejecuta el siguiente comando para ejecutar el programa:

python nombre_del_archivo.py

Se mostrará un mensaje para ingresar la operación matemática.
Ingresa la operación matemática y presiona Enter.
El programa mostrará el resultado de la operación o mostrará un mensaje de error si ocurre alguna excepción.

# Pruebas unitarias

El programa también incluye pruebas unitarias para verificar el funcionamiento correcto de la calculadora. Estas pruebas cubren escenarios de suma, resta, multiplicación, división, potencia, raíz cuadrada, división por cero, expresiones con paréntesis y longitud máxima de expresión.

Para ejecutar las pruebas unitarias, sigue los mismos pasos anteriores para ejecutar elprograma, pero en lugar de ejecutar el programa principal, ejecuta el siguiente comando:

python nombre_del_archivo_pruebas.py

Esto ejecutará las pruebas unitarias y mostrará los resultados de las pruebas en la terminal o línea de comandos. Verificarás si todas las pruebas pasan correctamente sin errores.
