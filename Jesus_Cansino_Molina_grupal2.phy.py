# EJERCICIO 2)

# Supongamos que la ETSII ha comprado un nuevo ordenador que vamos a utilizar
# como servidor para las prácticas de la asignatura, y que necesitamos dar de
# alta a los alumnos como usuarios de ese servidor. Para ello, hemos de
# generar automáticamente un nombre de usuario para cada alumno, en base a su
# nombre y apellidos.

# En este ejercicio se pide una función imprime_usuarios(fichero), que
# recibiendo como entrada un fichero con los datos de cada usuario, imprime
# por pantalla un listado de los mismos en orden alfabético de apellidos,
# junto con el nombre de usuario automáticamente generado.

# Por ejemplo, aplicando la función imprime_usuarios al fichero nombres.txt
# que se proporciona, debe de mostrase el siguiente resultado:

# >>> imprime_usuarios("nombres.txt")
#
# DNI      Apellidos                      Nombre          Usuario
# -------- ------------------------------ --------------- --------
# 67834547 Abad Garcia                    Maria Jose      mjabagar
# 87452221 Fernandez Lopera               Maria           mferlop1
# 76865412 Fernandez Lopez                Mario           mferlop
# 36638712 Gomariz Gonzaga                Amador          agomgon1
# 12987534 Gomez Gonzalez                 Alicia          agomgon
# 21783647 Gonzalez Echevarri             Antonia Maria   amgonech
# 87654321 Luna Espejo                    Emilio          elunesp
# 78988851 Mencheta Ruiz                  Javier Liborio  jlmenrui2
# 88734412 Mencheta Ruiz                  Jose Luis       jlmenrui1
# 22426553 Menendez Ruiz                  Juan            jmenrui
# 23823472 Mensaque Ruibarros             Juan Luis       jlmenrui
# 63555789 Muela Garcia                   Lidia           lmuegar
# 73535787 Navas Suarez                   Rocio           rnavsua
# 73163633 Perez Posada                   Manuel Jose     mjperpos
# 73263638 Poza Ramirez                   Isabel          ipozram
# 73276362 Rodicio Martinez               Antonio Manuel  amrodmar1
# 12326523 Rodriguez Marquez              Antonio Manuel  amrodmar
# 34551211 Sanchez Sanchez                Fermin Jose     fjsansan
# 78363677 Sanchez Santaella              Enrique Manuel  emsansan
# 21334456 Torres Chacon                  Eduardo         etorcha


# El fichero de entrada es una secuencia de líneas de la forma:
# DNI:Nombre1:Nombre2:Apellido1:Apellido2
# o bien (si el alumno no tuviera nombre compuesto):
# DNI:Nombre::Apellido1:Apellido2

# Como se muestra en el ejemplo anterior, el nombre de usuario de cada alumno
# se ha de generar mediante la siguiente regla: inicial del primer nombre,
# inicial segundo nombre (si tuviera), las tres primeras letras del primer
# apellido y las tres primeras letras del segundo apellido, todo en
# minúsculas. Si con esta regla hay varios alumnos a los que les corresponde
# el mismo nombre de usuario, se distinguen mediante sucesivos índices
# numéricos que se añaden al final.

# Nótese que si una línea del fichero no tiene el formato indicado, se ha de
# ignorar.

# INDICACIONES:
# - Pueden ser útiles los métodos split y lower de la clase string
# - Al leer cada línea del fichero de entrada, el último carácter será el
#   salto de línea "\n". Si tenemos una cadena l que tiene ese carácter de fin
#   de línea, entonces l[:-1] es la misma línea pero sin ese carácter.
# - Para ordenar las líneas por orden alfabético, puede ser util el método de
#   sort de la clase listas, y usar el parametro "key=...".
# - Las líneas de salida del ejemplo han sido impresas con la siguiente cadena
#   de formateo:  "{0:>8} {1:<30} {2:<15} {3}"
# ----------------------------------------------------------------------------------
f = open("nombres.txt", "r")
arrayAlumnos=[]
while(True):
     linea = f.readline()
     temp=(linea.split(":"))
     temp[len(temp) -1] = temp[len(temp) -1].rstrip("\n")
     arrayAlumnos.append(temp)
     if not linea:
         break
f.close()


arrayAlumnos.pop(0)
arrayAlumnos.pop(len(arrayAlumnos)-1)

userNameArray = []
for row in arrayAlumnos:
    primerNombre = row[1][0].lower()
    segundoNombre = row[2]
    primerApellido = row[3]
    segundoApellido = row[4]
    if len(segundoNombre) != 0:
        nom1 = primerNombre[0].lower()
        nom2 = segundoNombre[0].lower()
        ape1 = primerApellido[0:3].lower()
        ape2 = segundoApellido[0:3].lower()

        userName = nom1+nom2+ape1+ape2
        if userName in userNameArray:
            index = 1
            bandera = -1
            while bandera == -1:
                aux = userName + str(index)
                if aux in userNameArray:
                    bandera = -1
                    index = index + 1
                    print(index)
                else:
                    userNameArray.append(aux)
                    bandera = 0
        else:
            userNameArray.append(userName)
    else:
        nom1 = primerNombre[0].lower()
        ape1 = primerApellido[0:3].lower()
        ape2 = segundoApellido[0:3].lower()
        userName = nom1+ape1+ape2
        if userName in userNameArray:
            index = 1
            bandera = -1
            while bandera == -1:
                aux = userName + str(index)
                if aux in userNameArray:
                    bandera = -1
                    index = index + 1
                    print(index)
                else:
                    userNameArray.append(aux)
                    bandera = 0
        else:
            userNameArray.append(userName)

index = 0
for user in userNameArray:
    arrayAlumnos[index].append(user)
    index = index + 1

arrayAlumnos.sort(key=lambda Alumnos: Alumnos[3])

# Combinamos los nombres y los apellidos para que quede mejor formateado el valor en la tabla
alumnos = []
for alumno in arrayAlumnos:
    nombres = alumno[1]+' '+alumno[2]
    apellidos = alumno[3]+' '+alumno[4]
    tupla = [alumno[0], apellidos, nombres, alumno[len(alumno)-1]]
    alumnos.append(tupla)

Tabla = """\
+---------------------------------------------------------------------+
| DNI          APELLIDOS            NOMBRE            USUARIO
|---------------------------------------------------------------------|
{}              

+---------------------------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join(" {0:>8} {1:<20} {2:<20} {3}".format(*fila) for fila in alumnos)))
print (Tabla)


# -----------------------------------------------------------------------------
