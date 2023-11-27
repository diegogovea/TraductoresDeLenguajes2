# Analizador Léxico con Interfaz Gráfica

Este código implementa un analizador léxico simple con una interfaz gráfica utilizando la biblioteca `tkinter` en Python. El analizador léxico identifica tokens en una cadena de entrada y clasifica cada token en categorías como identificadores, constantes, operadores, etc. La interfaz gráfica permite al usuario ingresar texto y analizarlo con un botón.

## Cómo funciona

1. **Definición de Tokens y Estados**: El código define varios tokens y estados que representan las categorías de palabras clave, operadores y símbolos en el lenguaje que el analizador léxico está diseñado para reconocer.

2. **Función `analizar_cadena`**: Esta función se ejecuta cuando el usuario hace clic en el botón "Analizar". Realiza el análisis léxico de la cadena de texto ingresada.

3. **Bucle de Análisis Léxico**: Utiliza un bucle while para recorrer la cadena de entrada, identificando y clasificando cada token.

4. **Diccionario de Elementos**: Almacena los resultados del análisis léxico en una lista de diccionarios llamada `elementos`. Cada diccionario contiene información sobre el token, su lexema y un identificador asociado.

5. **Asignación de Identificadores**: Asigna identificadores numéricos a cada token. Por ejemplo, los identificadores de tipo de dato son 0, el identificador de la asignación es 8, etc.

6. **Asignación Específica de Tokens**: Después de analizar, el código realiza ajustes específicos para ciertas palabras clave, cambiando su token y asignando identificadores específicos.

7. **Interfaz Gráfica**: Se crea una interfaz gráfica con `tkinter` que incluye un cuadro de entrada, un botón de análisis y una tabla para mostrar los resultados.

## Uso

1. Ejecute el script.

2. Ingrese texto en el cuadro de entrada.

3. Haga clic en el botón "Analizar".

4. Los resultados del análisis léxico se mostrarán en la tabla.


