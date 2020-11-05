def sustituye_patrones(frase, fichero):
    #Abrimos el fichero de texto y guardará las líneas de texto.
    f = open(fichero, "r")
    lineas = f.readlines()

    for x in range (len(lineas)):
        #Tomamos el fichero de texto y lo dividimos dentro de una lista
        editarFrase = frase
        nombres = lineas[x].split(":")

        #Por cada nombre que existe en la lista lo reemplazamos dentro de la frase, según su orden.
        for i in range (len(nombres)):
            editarFrase = editarFrase.replace(str(i), nombres[i])

        #Imprimimos la frase editada.
        print(editarFrase)