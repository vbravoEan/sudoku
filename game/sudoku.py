import random

class Sudoku:
    def __init__(self, dificultad, visualizacion):
        self.dificultad = dificultad
        self.visualizacion = visualizacion
        self.tablero = self.generar_tablero()
        self.vacio = 0

    def generar_tablero(self):
        base = 2  # Cambiado de 3 a 2 para generar un tablero de 4x4
        side = base * base
        nums = random.sample(range(1, base * base + 1), side)
        board = [[nums[(base * (r % base) + r // base + c) % side] for c in range(side)] for r in range(side)]
        rows = [g * base + r for g in range(base) for r in range(base)]
        cols = [g * base + c for g in range(base) for c in range(base)]
        nums = random.sample(range(1, base * base + 1), side)
        board = [[nums[(base * (r % base) + r // base + c) % side] for c in range(side)] for r in range(side)]
        squares = side * side
        empties = squares * 3 // 4
        for p in random.sample(range(squares), empties):
            board[p // side][p % side] = 0

        return board


    def mostrar_tablero(self):
        borde = '*' if self.dificultad == 'fácil' else '-'
        print(borde * (4 * 2 + 3))
        for fila in self.tablero:
            print(borde + " ".join(str(x) if x != 0 else '.' for x in fila) + borde)
        print(borde * (4 * 2 + 3))

    def es_valido(self, num, fila, col):
        for x in range(4):
            if self.tablero[fila][x] == num or self.tablero[x][col] == num:
                return False
        startRow = fila - fila % 2
        startCol = col - col % 2
        for i in range(2):
            for j in range(2):
                if self.tablero[i + startRow][j + startCol] == num:
                    return False
        return True

    def resolver_tablero(self):
        for fila in range(4):
            for col in range(4):
                if self.tablero[fila][col] == 0:
                    for num in range(1, 5):
                        if self.es_valido(num, fila, col):
                            self.tablero[fila][col] = num
                            if self.resolver_tablero():
                                return True
                            self.tablero[fila][col] = 0
                    return False
        return True

    def jugar(self):
        self.mostrar_tablero()
        while True:
            fila = self.pedir_entrada("Ingrese la fila (1-4): ", int, 1, 4) - 1
            columna = self.pedir_entrada("Ingrese la columna (1-4): ", int, 1, 4) - 1
            
            if self.visualizacion == 'numérico':
                valor = self.pedir_entrada("Ingrese el número (1-4): ", int, 1, 4)
            elif self.visualizacion == 'letras':
                valor = self.pedir_entrada("Ingrese la letra (A-D): ", str, 'A', 'D')
                valor = ord(valor) - ord('A') + 1  # Convertir la letra a un número
            else:
                raise ValueError("Visualización no válida")
            
            if 0 <= fila < 4 and 0 <= columna < 4 and 1 <= valor <= 4 and self.tablero[fila][columna] == 0:
                if self.es_valido(valor, fila, columna):
                    self.tablero[fila][columna] = valor
                    self.mostrar_tablero()
                    if all(self.tablero[fila][columna] != 0 for fila in range(4) for columna in range(4)):
                        print("¡Felicidades, has resuelto el tablero!")
                        return
                else:
                    print("Número no válido, inténtalo de nuevo.")
            else:
    
                print("Entrada no válida, inténtalo de nuevo.")


    def pedir_entrada(self, mensaje, tipo, minimo, maximo):
        while True:
            try:
                entrada = input(mensaje)
                if tipo == int:
                    entrada = int(entrada)
                elif tipo == str:
                    if entrada.isalpha() and len(entrada) == 1:
                        entrada = entrada.upper()
                    else:
                        raise ValueError("Entrada no válida")
                if minimo <= entrada <= maximo:
                    return entrada
                else:
                    print("Valor fuera de rango, inténtalo de nuevo.")
            except ValueError:
                print("Valor no válido, inténtalo de nuevo.")
