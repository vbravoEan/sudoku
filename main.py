# main.py
from game.sudoku import Sudoku
from game.player import Player
from scores.score_manager import ScoreManager

def main():
    score_manager = ScoreManager()
    name = input("Ingrese su nombre: ")
    player = Player(name)

    while True:
        print("1. Jugar Sudoku")
        print("2. Ver mejores puntajes")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            visualizacion = input("Ingrese tipo de visualización (numérico, letras, símbolos): ")
            dificultad = input("Ingrese nivel de dificultad (fácil, difícil): ")
            sudoku = Sudoku(dificultad, visualizacion)
            puntos = sudoku.jugar()
            player.add_points(puntos)
            if player.score > score_manager.best_score():
                nombre = input("¡Nuevo mejor puntaje! Ingresa tu nombre: ")
                score_manager.add_score(nombre, player.score)
        
        elif opcion == '2':
            score_manager.show_scores()

        elif opcion == '3':
            break

        else:
            print("Opción no válida, inténtalo de nuevo.")

    if player.score > 0:
        print(f"Tu puntaje final es: {player.score}")
        
if __name__ == "__main__":
    main()