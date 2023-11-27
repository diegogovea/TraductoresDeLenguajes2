# Analizador Sintáctico con Interfaz Gráfica

Este código extiende el analizador léxico con una funcionalidad adicional para realizar el análisis sintáctico utilizando una tabla SLR (Simple LR). Además, se presenta la información mediante una interfaz gráfica utilizando `tkinter`.

## Cómo funciona

1. **Función `analizar_cadena`**: Esta función se ejecuta cuando el usuario hace clic en el botón "Analizar". Además del análisis léxico, realiza el análisis sintáctico utilizando la técnica SLR.

2. **Variables y Estructuras de Datos Agregadas**: Se han agregado nuevas variables y estructuras de datos, como `pila`, `tokens`, `reglas`, y `tabla_slr`. Estas se utilizan en el proceso de análisis sintáctico.

3. **Análisis Sintáctico con Tabla SLR**: Se implementa un análisis sintáctico utilizando una tabla SLR. La pila se utiliza para realizar operaciones de desplazamiento y reducción según las reglas definidas en la tabla.

4. **Interfaz de Usuario Mejorada**: Se ha añadido el uso de la biblioteca `messagebox` para mostrar mensajes emergentes indicando si la cadena es válida o inválida después del análisis sintáctico.

5. **Lectura de Archivos de Reglas y Tabla**: Se leen dos archivos de texto (`GR2slrRulesId.txt` y `GR2slrTable.txt`) que contienen las reglas y la tabla SLR, respectivamente.

6. **Actualización de la Interfaz Gráfica**: La interfaz muestra resultados tanto del análisis léxico como del análisis sintáctico en la tabla.

## Uso

1. Ejecute el script.

2. Ingrese texto en el cuadro de entrada.

3. Haga clic en el botón "Analizar".

4. Se mostrará un mensaje emergente indicando si la cadena es válida o inválida después del análisis sintáctico.

