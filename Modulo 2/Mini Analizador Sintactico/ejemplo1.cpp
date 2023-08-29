//Diego Leon Govea Ortiz
//Ejemplo 1: Modulo 2

#include <iostream>
#include <stack>
#include <string>
#include <cctype> // Para isalpha y isdigit

// Tabla de transiciones simplificada (0 para aceptar, negativos para reducir)
int tabla[5][3] = {
    {2, -1, 1},
    {-1, -1, -1},
    {-1, 3, -1},
    {4, -2, -2},
    {-1, -3, -3}
};

// Función para obtener el siguiente token
int getToken(const std::string& input, int& i) {
    if (i < input.size()) {
        char c = input[i];
        if (isalpha(c)) {
            return 0; // identificador
        } else if (c == '+') {
            return 1; // '+'
        } else if (c == '$') {
            return 2; // fin de entrada
        }
    }
    return -1; // token inválido
}

bool analizar(std::string input) {
    input += "$";
    std::stack<int> pila;
    pila.push(0);
    int i = 0;

    while (!pila.empty()) {
        int estado = pila.top();
        int token = getToken(input, i);
        int accion = tabla[estado][token];

        if (accion == 0) {
            return true; // Aceptación
        } else if (accion < 0) {
            int reduccion = -accion;
            for (int j = 0; j < reduccion; j++) {
                pila.pop();
            }
            int estado_actual = pila.top();
            // Consultar la tabla con el símbolo de reducción
            int simbolo_reduccion = 3; // Por ejemplo, 3 representa la reducción de regla 3
            int nuevo_estado = tabla[estado_actual][simbolo_reduccion];
            pila.push(simbolo_reduccion);
            pila.push(nuevo_estado);
        } else {
            pila.push(token);
            pila.push(accion);
            i++;
        }
    }
    return false; // No se alcanzó la aceptación
}

int main() {
    std::string input;
    std::cout << "Ingrese una expresión (ejemplo: hola+mundo): ";
    std::cin >> input;

    if (analizar(input)) {
        std::cout << "Expresión valida.\n";
    } else {
        std::cout << "Expresión invalida.\n";
    }
    return 0;
}
