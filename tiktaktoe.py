# Dibuja el tablero
def mostrartablero(tablero):
    for fila in tablero:
        print('-' * 13)
        for j in fila:
            print('| ', j, ' ', end='', sep='')
        print('|')
    print('-' * 13)

# Evita el error para que no pueda imprimir sobre otra jugada
def jugada(tablero, posicion, jugador):
    posicion -= 1
    estaocupado = tablero[posicion // 3][posicion % 3] == 'X' or tablero[posicion // 3][posicion % 3] == 'O'
    if estaocupado:
        return False
    else:
        tablero[posicion // 3][posicion % 3] = jugador
        return True

# Crea las formas de ganar que en total son 8
def evaluacion(tablero):
    f0 = f1 = f2 = c0 = c1 = c2 = d1 = d2 = True
    for i in range(2):
        f0 = f0 and tablero[0][i] == tablero[0][i + 1]
        f1 = f1 and tablero[1][i] == tablero[1][i + 1]
        f2 = f2 and tablero[2][i] == tablero[2][i + 1]
        c0 = c0 and tablero[i][0] == tablero[i + 1][0]
        c1 = c1 and tablero[i][1] == tablero[i + 1][1]
        c2 = c2 and tablero[i][2] == tablero[i + 1][2]
        d1 = d1 and tablero[i][i] == tablero[i + 1][i + 1]
        d2 = d2 and tablero[2 - i][i] == tablero[2 - i - 1][i + 1]
    return f0 or f1 or f2 or c0 or c1 or c2 or d1 or d2

base = []
fila = []
for i in range(1, 10):
    fila.append(i)
    if i % 3 == 0:
        base.append(fila)
        fila = []

tablero = base[:]
jugador = ('X', 'O')
contador = 0
mensaje = True
while True:
    if mensaje: # Muestra los mensajes de cuando es el turno de cada jugador
        mostrartablero(tablero)
        print('Juega', jugador[contador % 2], end='')
        posicion = int(input(', ingrese posicion del 1 al 9: '))
    else:
        print(' Posicion invalida', end= '')
        posicion = int(input(', vuelva a ingresar una posicion del 1 al 9: '))
    mensaje = jugada(tablero, posicion, jugador[contador % 2])
    if evaluacion(tablero):
        mostrartablero(tablero)
        print('Ganador', jugador[contador % 2])
        break
    if contador == 8: # Si todas las casillas estan tomadas y no hubo ganador el juego queda en empate
        print('EMPATE, NADIE GANÓ')
        break
    if mensaje:
        contador += 1

