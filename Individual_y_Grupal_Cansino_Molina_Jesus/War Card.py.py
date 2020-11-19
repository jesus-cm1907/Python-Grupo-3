from random import shuffle

palos = 'Diamante Corazon Pica Trebol'.split()
numeros = '1 2 3 4 5 6 7 8 9 10 J Q K'.split()


class Cartas:

    def __init__(self):
        print("Creando nuevo mazo.")
        self.Tcartas = [(s, r) for s in palos for r in numeros]

    def shuffle(self):
        print("Barajando...")
        shuffle(self.Tcartas)

    def cortar(self):
        return (self.Tcartas[:26],self.Tcartas[26:])

class Mano:

    def __init__(self, cartas):
        self.cartas = cartas

    def __str__(self):
        return "Contiene {} cartas".format(len(self.cartas))

    def add(self, Acartas):
        self.cartas.extend(Acartas)

    def Rcartas(self):
        return self.cartas.pop()


class Jugador:

    def __init__(self, nombre, mano):
        self.nombre = nombre
        self.mano = mano

    def Jugar_cartas(self):
        robar_carta = self.mano.Rcartas()
        print("{} ha introducido: {}".format(self.nombre, robar_carta))
        print('\n')
        return robar_carta

    def borrar_guerra_cartas(self):
        guerra_cartas = []
        if len(self.mano.cartas) < 3:
            return guerra_cartas
        else:
            for x in range(3):
                guerra_cartas.append(self.mano.cartas.pop())
            return guerra_cartas

    def todaviatienecartas(self):
        return len(self.mano.cartas) != 0


print("Empecemos!")


# Create New Cartas and split in half
d = Cartas()
d.shuffle()
mitad1, mitad2 = d.cortar()

# Create Both Jugadors
comp = Jugador("ordenador", Mano(mitad1))
nombre = input("Introduzca su nombre de usuario: ")
usuario = Jugador(nombre, Mano(mitad2))

# Set Round Count
Rondas_Totales = 0
puntuacionguerra = 0
# Let's play
while usuario.todaviatienecartas() and comp.todaviatienecartas():
    Rondas_Totales += 1
    print("Comienza una nueva ronda")
    print("Estas son las posiciones actuales: ")
    print(usuario.nombre+" puntos: "+str(len(usuario.mano.cartas)))
    print(comp.nombre+" puntos: "+str(len(comp.mano.cartas)))
    print("Ambos jugadores juegan una carta")
    print('\n')

    CartasMesa = []

    ccarta = comp.Jugar_cartas()
    jcarta = usuario.Jugar_cartas()

    # Añade cartas a la mesa
    CartasMesa.append(ccarta)
    CartasMesa.append(jcarta)

    # Calcula el rango de las cartas
    if ccarta[1] == jcarta[1]:
        puntuacionguerra += 1
        print("Cada jugador elimina 3 cartas boca abajo y 1 carta boca arriba.")
        CartasMesa.extend(usuario.borrar_guerra_cartas())
        CartasMesa.extend(comp.borrar_guerra_cartas())

        ccarta = comp.Jugar_cartas()
        jcarta = usuario.Jugar_cartas()

        CartasMesa.append(ccarta)
        CartasMesa.append(jcarta)

        if numeros.index(ccarta[1]) < numeros.index(jcarta[1]):
            print(usuario.nombre+" tiene la carta más alta.")
            usuario.mano.add(CartasMesa)
        else:
            print(comp.nombre+" tiene la carta más alta.")
            comp.mano.add(CartasMesa)

    else:
        # Calcula quien tiene el rango más alto
        if numeros.index(ccarta[1]) < numeros.index(jcarta[1]):
            print(usuario.nombre+" tiene la carta más alta.")
            usuario.mano.add(CartasMesa)
        else:
            print(comp.nombre+" tiene la carta más alta.")
            comp.mano.add(CartasMesa)

print("Bien jugado!")
