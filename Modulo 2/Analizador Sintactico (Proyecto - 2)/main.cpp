#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

// Enumeración para tipos de token
enum TokenType {
    NUMBER,
    ADD,
    SUBTRACT,
    MULTIPLY,
    DIVIDE,
    OPEN_PAREN,
    CLOSE_PAREN,
    END
};

// Estructura para representar un token
struct Token {
    TokenType type;
    string value;
};

// Función para analizar la expresión
bool parseExpression(const vector<Token>& tokens);

// Función para verificar si un token es un operador
bool isOperator(const Token& token);

// Función principal
int main() {
    // Supongamos que tenemos una lista de tokens previamente generados
    vector<Token> tokens = {
        {NUMBER, "5"},
        {ADD, "+"},
        {NUMBER, "3"},
        {MULTIPLY, "*"},
        {OPEN_PAREN, "("},
        {NUMBER, "2"},
        {ADD, "+"},
        {NUMBER, "1"},
        {CLOSE_PAREN, ")"},
        {END, ""}
    };

    // Llamar a la función de análisis sintáctico
    if (parseExpression(tokens)) {
        cout << "La expresión es sintácticamente válida." << endl;
    } else {
        cout << "La expresión es sintácticamente inválida." << endl;
    }

    return 0;
}

bool parseExpression(const vector<Token>& tokens) {
    stack<TokenType> operatorStack;
    stack<TokenType> operandStack;

    for (const Token& token : tokens) {
        if (token.type == NUMBER) {
            operandStack.push(token.type);
        } else if (token.type == OPEN_PAREN) {
            operatorStack.push(token.type);
        } else if (token.type == CLOSE_PAREN) {
            while (!operatorStack.empty() && operatorStack.top() != OPEN_PAREN) {
                operandStack.pop(); // Deshacer operadores anteriores
                operandStack.pop();
                if (operatorStack.empty()) {
                    return false; // Paréntesis no coincidentes
                }
                operatorStack.pop();
            }
        } else if (isOperator(token)) {
            while (!operatorStack.empty() && isOperator(token) &&
                   token.type <= operatorStack.top()) {
                operandStack.pop(); // Deshacer operador anterior
                operandStack.pop();
                operatorStack.pop();
            }
            operatorStack.push(token.type);
        } else if (token.type == END) {
            while (!operatorStack.empty()) {
                if (operatorStack.top() == OPEN_PAREN) {
                    return false; // Paréntesis no coincidentes
                }
                operandStack.pop(); // Deshacer operadores no resueltos
                operandStack.pop();
                operatorStack.pop();
            }
        } else {
            return false; // Token desconocido
        }
    }

    return operandStack.size() == 1 && operatorStack.empty();
}

bool isOperator(const Token& token) {
    return (token.type == ADD || token.type == SUBTRACT ||
            token.type == MULTIPLY || token.type == DIVIDE);
}
