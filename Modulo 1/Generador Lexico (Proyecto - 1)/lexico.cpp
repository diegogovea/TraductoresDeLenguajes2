#include "lexico.h"

  Lexico::Lexico(string fuente){
    ind= 0;
    this->fuente= fuente;
  }

  Lexico::Lexico(){
    ind= 0;
  }

  string Lexico::tipoAcad(int tipo){
         string cad= "";

         switch (tipo){
           case TipoSimbolo::IDENTIFICADOR:
                cad= "Identificador";
                break;
           case TipoSimbolo::ENTERO:
                cad= "Entero";
                break;
           case TipoSimbolo::REAL:
                cad= "Real";
                break;
            case TipoSimbolo::CADENA:
                cad= "Cadena";
                break;
            case TipoSimbolo::TIPO:
                cad= "TIPO";
                break;
            case TipoSimbolo::OPADIC:
                cad= "Op. Adicion";
                break;
            case TipoSimbolo::OPMULT:
                cad= "Op. Multiplicacion";
                break;
            case TipoSimbolo::OPRELAC:
                cad= "Op. Relacion";
                break;
            case TipoSimbolo::OPOR:
                cad= "Op. Or";
                break;
            case TipoSimbolo::OPAND:
                cad= "Op. AND";
                break;

           case TipoSimbolo::OPNOT:
                cad= "Op. NOT";
                break;

           case TipoSimbolo::OPIGUALDAD:
                cad= "Op. IGUALDAD";
                break;

           case TipoSimbolo::PUNTOYCOMA:
                cad= "Punto y coma";
                break;

           case TipoSimbolo::COMA:
                cad= "Coma";
                break;
            case TipoSimbolo::P1:
                cad= "Abre Parentesis";
                break;

            case TipoSimbolo::P2:
                cad= "Cierra Parentesis";
                break;

            case TipoSimbolo::LLAVE1:
                cad= "Abre Llave";
                break;

            case TipoSimbolo::LLAVE2:
                cad= "Cierra Llave";
                break;
            case TipoSimbolo::OPIF:
                cad= "Op. IF";
                break;
            case TipoSimbolo::OPWHILE:
                cad= "Op. WHILE";
                break;
            case TipoSimbolo::OPRETURN:
                cad= "Op. Return";
                break;
            case TipoSimbolo::OPELSE:
                cad= "Op. Else";
                break;
            case TipoSimbolo::PESOS:
                cad= "FIN";
                break;


         }

         return cad;
  }

  void Lexico::entrada(string fuente){
       ind= 0;
      this->fuente= fuente;
  }

int Lexico::sigSimbolo(){

    estado=0;
    continua= true;
    simbolo= "";

    //Inicio del Automata
    while (continua){
      c= sigCaracter();

      switch (estado){
        case 0:
            if(esDigito(c)){

            }

             if ( c == '+' || c=='-') aceptacion(2);
             if ( c == '*' || c=='/') aceptacion(3);
             if ( c == '<' || c=='>') aceptacion(4);
             if ( c == ',') aceptacion(5);
             if ( c == ';') aceptacion(6);
             if ( c == '(') aceptacion(7);
             if ( c == ')') aceptacion(8);
             if ( c == '{') aceptacion(9);
             if ( c == '}') aceptacion(10);
             if ( c == '=') aceptacion(11);






             else
              if ( c == '$' ) aceptacion(-1);

             break;

      }

   }
    //Fin del Automata

      switch (estado){

         case 2:
              tipo= TipoSimbolo::OPADIC;
              break;
         case 3:
              tipo= TipoSimbolo::OPMULT;
              break;
         case 4:
              tipo= TipoSimbolo::OPRELAC;
              break;
         case 5:
              tipo= TipoSimbolo::COMA;
              break;
         case 6:
              tipo= TipoSimbolo::PUNTOYCOMA;
              break;
         case 7:
              tipo= TipoSimbolo::P1;
              break;
         case 8:
              tipo= TipoSimbolo::P2;
              break;
         case 9:
              tipo= TipoSimbolo::LLAVE1;
              break;
         case 10:
              tipo= TipoSimbolo::LLAVE2;
              break;
         case 11:
              tipo= TipoSimbolo::IGUAL;
              break;
         case 12:
              tipo= TipoSimbolo::IDENTIFICADOR;


        default:
              tipo= TipoSimbolo::PESOS;
      }

	return tipo;
}

 char Lexico::sigCaracter(){
      if (terminado()) return '$';

      return fuente[ind++];
 }

  void Lexico::sigEstado(int estado){
       this->estado= estado;
       simbolo+= c;
  }

  void Lexico::aceptacion(int estado){
       sigEstado(estado);
       continua= false;
  }

  bool Lexico::terminado(){//fin de cadena
         return ind >= fuente.length();
  }

   bool Lexico::esLetra(char c){
        return isalpha(c) || c=='_';
   }


   bool Lexico::esDigito(char c){
        return isdigit(c);
   }

   bool Lexico::esEspacio(char c){
        return c== ' ' || c== '\t';
   }


   void Lexico::retroceso(){
      if ( c != '$') ind--;
        continua= false;
    }

