# Módulos importados.
import turtle
import random
import time

# Puntos para el jugador.
puntuacion_jugador = 0
puntuacion_mas_alta = 0
tiempo_retraso = 0.1

# Primera parte, el lienzo.
# Crear pantalla:
window = turtle.Screen()
window.title("Laberinto de la serpiente: 🐍")
window.bgcolor("red")

# Tamaño de la pantalla:
window.setup(width=600, height=600)

# Crear la serpiente:
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"
