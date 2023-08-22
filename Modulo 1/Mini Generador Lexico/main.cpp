//Govea Ortiz Diego Leon
//Mini Analizador Lexico

#include <iostream>
#include <string>
using namespace std;


bool esLetra(char c) {
    return isalpha(c);
}

bool esDigito(char c) {
    return isdigit(c);
}

void imprimirToken(string token,bool real){
    string tokenActual=token;
    bool esReal=real;
    if (!tokenActual.empty()) {
        if (esReal) {
            cout << "Real: " << tokenActual << endl;
        } else {
            cout << "Identificador: " << tokenActual << endl;
        }

    }
}
// Función para analizar el texto y encontrar tokens
void analizarTexto(const string& texto) {
    string tokenActual;
    bool esReal = false;
    bool esId = false;

    for (char c : texto) {
        if (esLetra(c)) {
            tokenActual += c;
            esId=true;
        } else if (esDigito(c)) {
            tokenActual += c;
            if(!esId)esReal = true;
        } else if (c == '.' && esReal) {
            tokenActual += c;
        } else {
            imprimirToken(tokenActual,esReal);
            tokenActual.clear();
            esReal = false;
            esId=false;

        }
    }
    imprimirToken(tokenActual,esReal);
}



int main() {
    string texto = "a1 1345 123.456 12.1 xyrrz 789.0 aaa1 a2 a3 a4";

    cout << "Analizando el texto:" << endl;
    analizarTexto(texto);

    return 0;
}
