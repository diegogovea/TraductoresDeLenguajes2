import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para realizar el análisis léxico
def analizar_cadena():
    entrada = entrada_text.get()
    elementos = []
    pila = [0]
    tokens = []
    reglas = []
    tabla_slr = []
    estado = 0
    indice = 0
    cadena = entrada + '$'
    identificador = []
    while (indice <= (len(cadena) - 1) and estado == 0):
        lexema = ''
        token = 'error'
        while (indice <= (len(cadena) - 1) and estado != 20):
            if estado == 0:
                if (cadena[indice].isspace()):
                    estado = 0
                elif cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 4
                    lexema += cadena[indice]
                    token = 'id'
                    identificador = 1
                elif cadena[indice].isnumeric():
                    estado = 20
                    lexema += cadena[indice]
                    token = 'constante'
                    identificador = 13
                elif cadena[indice] == '$':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'pesos'
                    identificador = 18
                elif cadena[indice] == '=':
                    lexema += cadena[indice]
                    token = 'asignación'
                    estado = 5
                    identificador = 8
                elif cadena[indice] == '>':

                    lexema += cadena[indice]
                    token = 'opRelacional'
                    estado = 5
                    identificador = 15
                elif cadena[indice] == '<':

                    lexema += cadena[indice]
                    token = 'opRelacional'
                    estado = 5
                    identificador = 15
                elif cadena[indice] == '!':

                    lexema += cadena[indice]
                    estado = 5
                elif cadena[indice] == ';':

                    lexema += cadena[indice]
                    token = ';'
                    estado = 20
                    identificador = 2
                elif cadena[indice] == '+':

                    lexema += cadena[indice]
                    token = 'opSuma'
                    estado = 20
                    identificador = 14
                elif cadena[indice] == '-':

                    lexema += cadena[indice]
                    token = 'opSuma'
                    estado = 20
                    identificador = 14
                elif cadena[indice] == '*':

                    lexema += cadena[indice]
                    token = 'opMultiplicacion'
                    estado = 20
                    identificador = 16
                elif cadena[indice] == ',':

                    lexema += cadena[indice]
                    token = 'coma'
                    estado = 20
                    identificador = 3
                elif cadena[indice] == '(':

                    lexema += cadena[indice]
                    token = '('
                    estado = 20
                    identificador = 4
                elif cadena[indice] == ')':

                    lexema += cadena[indice]
                    token = ')'
                    estado = 20
                    identificador = 5
                elif cadena[indice] == '{':

                    lexema += cadena[indice]
                    token = '{'
                    estado = 20
                    identificador = 6
                elif cadena[indice] == '}':

                    lexema += cadena[indice]
                    token = '}'
                    estado = 20
                    identificador = 7
                elif cadena[indice] == '|':

                    lexema += cadena[indice]
                    estado = 15
                elif cadena[indice] == '&':

                    lexema += cadena[indice]
                    estado = 16
                else:
                    estado = 20
                    token = 'error'
                    lexema = cadena[indice]
                    identificador = 18
                indice += 1

            elif estado == 4:
                if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 4
                    lexema += cadena[indice]
                    token = 'id'
                    indice += 1
                else:
                    estado = 20

            elif estado == 5:
                if cadena[indice] != '=':
                    estado = 20
                else:
                    estado = 20
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    identificador = 17
                indice += 1
            elif estado == 15:
                if cadena[indice] != '|':
                    estado = 20
                else:
                    estado = 20
                    lexema += cadena[indice]
                    token = 'opLogico'
                    identificador = 15
                    indice += 1
            elif estado == 16:
                if cadena[indice] != '&':
                    token = 'error'
                    estado = 20
                else:
                    estado = 20
                    lexema += cadena[indice]
                    token = 'opLogico'
                    identificador = 15
                    indice += 1

        estado = 0
        elementos.append({'token': token, 'lexema': lexema,
                         'identificador': identificador})
    for elemento in elementos:
        if elemento['lexema'] == "if":
            elemento['token'] = "condicional SI"
            elemento['identificador'] = 9
        if elemento['lexema'] == "else":
            elemento['token'] = "else"
            elemento['identificador'] = 12
        if elemento['lexema'] == "while":
            elemento['token'] = "while"
            elemento['identificador'] = 10
        if elemento['lexema'] == "return":
            elemento['token'] = "return"
            elemento['identificador'] = 11
        if elemento['lexema'] == "int":
            elemento['token'] = "tipo de dato"
            elemento['identificador'] = 0
        if elemento['lexema'] == "float":
            elemento['token'] = "tipo de dato"
            elemento['identificador'] = 0
        if elemento['lexema'] == "char":
            elemento['token'] = "tipo de dato"
            elemento['identificador'] = 0
        if elemento['lexema'] == "void":
            elemento['token'] = "tipo de dato"
            elemento['identificador'] = 0

    # Limpiar la tabla anterior
    for row in tabla.get_children():
        tabla.delete(row)

    # Mostrar los resultados en la tabla
    for elemento in elementos:
        tabla.insert('', 'end', values=(
            elemento['lexema'], elemento['token'], elemento['identificador']))
        tokens.append(elemento['identificador'])

    with open('GR2slrRulesId.txt', 'r') as archivo_reglas:
        for fila in archivo_reglas:
            arreglo_fila = fila.strip().split('\t')
            arreglo_fila = [int(numero) for numero in arreglo_fila]
            reglas.append(arreglo_fila)

    with open('GR2slrTable.txt', 'r') as archivo_tabla:
        for fila in archivo_tabla:
            arreglo_fila = fila.strip().split('\t')
            arreglo_fila = [int(numero) for numero in arreglo_fila]
            del (arreglo_fila[0])
            tabla_slr.append(arreglo_fila)

    continuar_analisis = True

    while tokens and continuar_analisis:
        accion = tabla_slr[pila[-1]][tokens[0]]
        if accion == -1:
            # Significa que la cadena es valida, muestralo en interfaz
            messagebox.showinfo("Mensaje Emergente", "Cadena Valida")

            continuar_analisis = False
        # Si es mayor a 0 en la tabla, significa que es un desplazamiento (lo que vendria siendo dX) haciendola a mano, X es el que te da la tabla
        elif accion > 0:
            pila.append(tokens[0])
            pila.append(accion)
            del (tokens[0])
        # Si es menor que 0, significa que es una reduccion (lo que vendria siendo rX) haciendola a mano, nomas que en la tabla el -1 es r0, el -2 es r1 y asi, por eso lo ajustamos
        elif accion < 0:
            accion = abs(accion+1)
            regla = reglas[accion]
            for i in range(regla[1]*2):
                pila.pop()
            pila.append(regla[0])
            pila.append(tabla_slr[pila[-2]][pila[-1]])
        else:
            # Significa que la cadena es invalida, muestralo en interfaz
            messagebox.showinfo("Mensaje Emergente", "Cadena Invalida")

            continuar_analisis = False


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Léxico")

# Crear y configurar el cuadro de entrada
entrada_label = tk.Label(ventana, text="Ingrese texto:")
entrada_label.pack()
entrada_text = tk.Entry(ventana, width=40)
entrada_text.pack()

# Crear y configurar el botón de análisis
analizar_button = tk.Button(ventana, text="Analizar", command=analizar_cadena)
analizar_button.pack()

# Crear y configurar la tabla
tabla = ttk.Treeview(ventana, columns=(
    "Lexema", "Token", "Identificador"), show="headings")
tabla.heading("Lexema", text="Lexema")
tabla.heading("Token", text="Token")
tabla.heading("Identificador", text="Identificador")
tabla.pack()

# Ejecutar la aplicación
ventana.mainloop()
