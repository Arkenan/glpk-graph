import sys

inputfile = open("ej.mod")

for linea in inputfile:
    # print ("linea: "+ linea)
    # Separo a ambos lados de la restricción.
    # Busco si es <=, >=, =.
    punto = linea.find("=")
    # Chequeo que sea uno solo.
    punto2 = linea.find("=", punto+1)

    if punto2 != -1:
        print ("Error, más de una restricción en la línea " + linea)
        continue
        # sys.exit()

    if punto == -1:
        print ("Error, no hay restricción en la línea " + linea)
        continue
        # sys.exit()

    c = linea[punto -1]
    if c == "<":
        print ("La restricción es de menor o igual " + linea)
    elif c == ">":
        print ("La restricción es de mayor o igual " + linea)
    else:
        print ("La restricción es una igualdad. " + linea)
