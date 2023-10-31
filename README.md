# Sudoku

Este proyecto es una implementación del juego de Sudoku en Python. El jugador puede elegir entre dos niveles de dificultad, fácil y difícil, así como diferentes visualizaciones para el tablero, incluyendo numérico y letras.

## Requisitos

- Python 3.11.5 o superior

## Estructura del proyecto

- `game/`
  - `__init__.py`
  - `player.py`: Define la clase `Player` que representa al jugador.
  - `sudoku.py`: Define la clase `Sudoku` que representa al juego de Sudoku, con sus métodos para jugar y verificar la validez de los movimientos.
- `scores/`
  - `__init__.py`
  - `score_manager.py`: Define la clase `ScoreManager` que maneja los puntajes de los jugadores.
- `main.py`: Archivo principal que ejecuta el juego.
- `README.md`: Archivo con instrucciones y descripción del proyecto.

## Pasos para ejecutar el proyecto

1. Asegúrate de tener Python 3.11.5 o superior instalado en tu máquina.
2. Clona o descarga este repositorio a tu máquina local.
3. Abre una terminal y navega al directorio donde descargaste el proyecto.
4. Crea un ambiente virtual con el comando `python -m venv venv`.
5. Activa el ambiente virtual con el comando `source venv/bin/activate` (en macOS/Linux) o `venv\Scripts\activate` (en Windows).
6. Ejecuta el comando `python main.py` para iniciar el juego.
7. Sigue las instrucciones en pantalla para jugar el juego.
