from tabulate import tabulate

tlr2 = [[2,0,0,1],
        [0,0,-1,0],
        [0,3,-3,0],
        [2,0,0,4],
        [0,0,-2,0]]

data = []
pila = list()
pilaS = ""
lexList = list()
sinList = list()
fila = 0
columna = 0
accion = 0
elim = 6
archivo = open('Mini Sintactico\compilador.lr','r')
lines = archivo.readlines()
reglas = list()
reg = 0
num = 0
tlr1 = list()

class Regla:
    def __init__(self, num, num2, elem, fuente):
        self.num = num
        self.num2 = num2
        self.elem = elem
        self.fuente = fuente

class ElementoPila:
    def __init__(self, fuente):
        self.fuente = fuente

class Terminal(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente)
        self.tipo = tipo

class NoTerminal(ElementoPila):
    def __init__(self, fuente):
        super().__init__(fuente)

class Estado(ElementoPila):
    def __init__(self, fuente):
        super().__init__(fuente)

pila.append(Terminal("$", 100))
pila.append(Estado(0))

for line in lines:
    line = line.rstrip()
    line = line.split("\t")
    if (reg == 1):
        tlr1.append(line)
        for i in range(len(tlr1)):
            for j in range(len(tlr1[i])):
                tlr1[i][j] = int(tlr1[i][j])
    if (line[0]=='52'):
        continue
    if (line[0]=='95'):
        reg = 1
    if (reg == 0):
        num += 1
        obj = Regla(num, int(line[0]), int(line[1]), line[2])
        reglas.append(obj)

class miniAnalizador:
    def __init__(self, cadena):
        self.cadena = cadena + '$'
        self.edo = -1

    def check(self, cad):
        reservadas = ["if","while", "return", "else"]
        tipoR = ["19","20", "21", "22"]
        if (cad in reservadas):
            it = 0
            for it in range(0, len(reservadas)):
                if cad == reservadas[it]:
                    tipoS = tipoR[it]
                    obj = Terminal(cad, int(tipoS))
                    lexList.append(obj)
                    it= it+1 
                    cad = ""
        else:
            obj = Terminal(cad, 0)
            lexList.append(obj)
            cad = ""
            

    def analizar(self):
        cad = ""
        identificador = ""
        numero = ""
        real = ""
        entero = ""
        cadenaS = ""
        i=0
        n=0
        skip = False
        tipo = ["int", "void", "float"]
        simbolos = [";", ",", "(", ")", "{", "}", "$"]
        tipoA = ["12", "13", "14", "15", "16", "17", "23"]
        relac = ""
        orV = ""
        reservadas = ["if","while", "return", "else"]
        tipoR = ["19", "20", "21", "22"]
        for caracter in self.cadena:
            asCarac = ord(caracter)
            if (caracter == '$'):
                obj = Terminal(caracter, 23)
                lexList.append(obj)
                break

            elif(skip==True):
                if(n != cont-1):
                    n=n+1
                    continue
                else:
                    skip=False
            elif (asCarac > 64 and asCarac < 91) or (asCarac>96 and asCarac<123): #Comprobamos si el caracter es una letra
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(cadenaS)!=0):
                    obj = Terminal(cadenaS, 3)
                    lexList.append(obj)
                    print("Cadena Tipo 3: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    identificador += caracter
                else:
                    identificador += caracter

            elif (asCarac > 47 and asCarac < 58):
                if(len(identificador)!=0):
                    identificador += caracter
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                elif(len(cadenaS)!=0):
                    obj = Terminal(cadenaS, 2)
                    lexList.append(obj)
                    print("Cadena Tipo 3: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    identificador += caracter
                else:
                    #entero +=caracter
                    numero += caracter
                    if(len(real)!=0):
                        real+=caracter
                       
            elif (caracter == "."):
                if(len(real)==0):
                    real += numero + caracter
                else:
                    print("ERROR")
            
            elif (caracter == " "):
                if(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(entero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(cadenaS)!=0):
                    obj = Terminal(cadenaS, 3)
                    lexList.append(obj)
                    print("Cadena Tipo 3: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    
            
            elif (caracter =="'") or (caracter == '"'):
                c=i+1
                cont = 0
                if(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                
                for cadenaCar in range(c, len(self.cadena)):
                    cont=cont+1
                    if (self.cadena[cadenaCar] == '$'):
                        print("ERROR CADENA NO CIERRA")
                        obj = Terminal('$', 23)
                        lexList.append(obj)
                        skip = True
                        break
                    elif (self.cadena[cadenaCar]=="'") or (self.cadena[cadenaCar]=='"'):
                        skip = True
                        obj = Terminal(cadenaS, 3)
                        lexList.append(obj)
                        print("Cadena Tipo 3: ", cadenaS)
                        real=""
                        identificador=""
                        numero=""
                        cadenaS=""
                        break
                    cadenaS=cadenaS + self.cadena[cadenaCar]

            elif (caracter == '+') or (caracter == '-'):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 5)
                    #obj = Terminal(caracter, 1)
                    lexList.append(obj)
                    print("opSuma Tipo 5: ", caracter)
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 5)
                    #obj = Terminal(caracter, 1)
                    lexList.append(obj)
                    print("opSuma Tipo 5: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        obj = Terminal(caracter, 5)
                        #obj = Terminal(caracter, 1)
                        lexList.append(obj)
                        print("opSuma Tipo 5: ", caracter)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        obj = Terminal(caracter, 5)
                        #obj = Terminal(caracter, 1)
                        lexList.append(obj)
                        print("opSuma Tipo 5: ", caracter)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        obj = Terminal(caracter, 5)
                        #obj = Terminal(caracter, 1)
                        lexList.append(obj)
                        print("opSuma Tipo 5: ", caracter)
                else:
                    obj = Terminal(caracter, 5)
                    #obj = Terminal(caracter, 1)
                    lexList.append(obj)
                    print("opSuma Tipo 5: ", caracter)
            
            elif (caracter == '*') or (caracter == '/'):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 6)
                    lexList.append(obj)
                    print("opMul Tipo 6: ", caracter)
                elif(len(real)!=0):
                    obj = Terminal(real, 6)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 6)
                    lexList.append(obj)
                    print("opMul Tipo 6: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        obj = Terminal(caracter, 6)
                        lexList.append(obj)
                        print("opMul Tipo 6: ", caracter)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        obj = Terminal(caracter, 6)
                        lexList.append(obj)
                        print("opMul Tipo 6: ", caracter)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        obj = Terminal(caracter, 6)
                        lexList.append(obj)
                        print("opMul Tipo 6: ", caracter)
                else:
                    obj = Terminal(caracter, 6)
                    lexList.append(obj)
                    print("opMul Tipo 6: ", caracter)

            elif (caracter == '<') or (caracter == '>') or (caracter == '!'):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="="):
                    cont= 1
                    skip = True
                    relac = caracter + self.cadena[i+1]
                    obj = Terminal(relac, 7)
                    lexList.append(obj)
                    print("opRelac Tipo 7: ", relac)
                    cont = 1
                    skip = True
                else:
                    obj = Terminal(caracter, 7)
                    lexList.append(obj)
                    print("opRelac Tipo 7: ", caracter)

            elif (caracter == '='):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador = ""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="="):
                    relac = caracter + self.cadena[i+1]
                    obj = Terminal(relac, 7)
                    lexList.append(obj)
                    print("opRelac Tipo 7: ", relac)
                    cont = 1
                    skip = True
                else:
                    obj = Terminal(caracter, 18)
                    lexList.append(obj)
                    print("opAsignacion Tipo 18: ", caracter)
                
            elif (caracter == '|'):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="|"):
                    orV = caracter + self.cadena[i+1]
                    obj = Terminal(orV, 8)
                    lexList.append(obj)
                    print("opOr Tipo 8: ", orV)
                    cont = 1
                    skip = True
                else:
                    print("OpOr incompleto ")

            elif (caracter == '&'):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="&"):
                    andV = caracter + self.cadena[i+1]
                    obj = Terminal(andV, 9)
                    lexList.append(obj)
                    print("opAnd Tipo 9: ", andV)
                    cont = 1
                    skip = True
                else:
                    print("OpAnd incompleto ")

            elif (caracter == '!'):
                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 10)
                    lexList.append(obj)
                    print("opNot Tipo 10: ", caracter)
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 10)
                    lexList.append(obj)
                    print("opNot Tipo 10: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        obj = Terminal(caracter, 10)
                        lexList.append(obj)
                        print("opNot Tipo 10: ", caracter)
                        identificador=""
                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador = ""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        obj = Terminal(caracter, 10)
                        lexList.append(obj)
                        print("opNot Tipo 10: ", caracter)
                else:
                    obj = Terminal(caracter, 10)
                    lexList.append(obj)
                    print("opNot Tipo 10: ", caracter)

            elif (caracter in simbolos):
                it = 0
                for it in range(0, len(simbolos)):
                    if caracter == simbolos[it]:
                        tipoS = tipoA[it]
                    it= it+1

                if(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 10)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                        
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                obj = Terminal(caracter, int(tipoS))
                lexList.append(obj)
                print("Simbolo Tipo "+ tipoS + ":", caracter)
             
            
            i=i+1            

        if(len(real)!=0):
            obj = Terminal(real, 2)
            lexList.append(obj)
            print("Real Tipo 2", real)
            real=""
            identificador=""
            numero=""
        elif(len(numero)!=0):
            obj = Terminal(numero, 1)
            lexList.append(obj)
            print("Entero Tipo 1", numero)
            real=""
            identificador=""
            numero=""
        elif(len(identificador)!=0):
            if(identificador in tipo):
                obj = Terminal(identificador, 4)
                lexList.append(obj)
                print("TipoDato Tipo 4: ", identificador)
                identificador=""

            elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
            else:
                obj = Terminal(identificador, 0)
                lexList.append(obj)
                print("Identificador Tipo 0", identificador)
                real=""
                identificador=""
                numero=""
                obj = Terminal("$", 23)
                lexList.append(obj)



#print("Ingresa una cadena")
#cadena = input()
cadena = "void menu(){hola = 5;}"
i=0
miniAnalizador(cadena).analizar()
print("HOLAAA", lexList[-1].fuente)
while True:
    obj = lexList[i]
    fila = pila[-1]
    print("OVJETO", obj.fuente)
    columna = obj.tipo
    accion = tlr1[fila.fuente][columna]
    print("ACCION", accion)
    #print("FILA", fila.fuente)
    #print("COLUMNA", columna)

   
    if (accion == 0):
        acc = "NADA"
        print("NADA")
        break
    elif (accion > 0):
        i+=1
        acc = "d"+str(accion)
        pila.append(Terminal(obj.fuente, obj.tipo))
        print("ACC", accion)
        pila.append(Estado(accion))
    elif (accion == -1):
        acc = "r0(acept)"
        print("R0")
        break
    else:
        acc = "r"+str(abs(accion+1))
        for obj2 in reglas:
            if (accion == (obj2.num + 1)*-1):
                acc = "r"+str(obj2.num)
                accion = tlr1[fila.fuente][obj2.num2]
                if obj2.elem !=0:
                    elim = obj2.elem*2
                    while elim !=0:
                        pila.pop()
                        elim -=1
                    fila = pila[-1]
                    accion = tlr1[fila.fuente][obj2.num2]
                    pila.append(obj2)
                    pila.append(Estado(accion))
                else:
                    print("obb", obj.fuente)
                    pila.append(obj2)
                    pila.append(Estado(accion))
                break
    if(i == len(lexList)):
        print("FIN")
        
                

    for p in pila:
        #print("PPPPP", p)
        pilaS += str(p.fuente)
    data.append([pilaS, obj.fuente, acc])
    pilaS = ""

    '''if acc == "r1":
        elim = len(pila)-2
        while elim !=0:
            pila.pop()
            elim -=1
        pila.append(NoTerminal("E"))    
        pila.append(Estado(str(abs(accion+1))))
        for p in pila:
            pilaS += str(p.fuente)
        data.append([pilaS, "$", acc])
    if acc == "r2":
        elim = len(pila)-2
        while elim !=0:
            pila.pop()
            elim -=1
        pila.append(NoTerminal("E"))    
        pila.append(Estado(str(abs(accion+1))))
        for p in pila:
            pilaS += str(p.fuente)
        data.append([pilaS, "$", acc])'''

print(tabulate(data, headers=["Pila", "Entrada", "Salida"]))
