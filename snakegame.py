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

# Crear la comida:
food = turtle.Turtle()
shapes = random.choice(['triangle', 'circle'])
food.shape(shapes)
food.color("blue")
food.speed(0)
food.penup()
food.goto(0, 100)

# Agregar puntuación para el jugador:
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.shape('square')
score_pen.color('white')
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 250)
score_pen.write("Tu puntación: 0 | Tu puntación más alta: 0", align="center", font=("Arial", 24, "normal"))

# Segunda parte, direcciones.
# Asignación de direcciones con las teclas de dirección:
def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up":
        snake.direction = "down"

# Movimiento:
def move():
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y + 20)

    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y - 20)
    
    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x + 20)
    
    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x - 20)
    
# Eventos en la pantalla:
window.listen()
window.onkeypress(move_left, 'Left')
window.onkeypress(move_right, 'Right')
window.onkeypress(move_up, 'Up')
window.onkeypress(move_down, 'Down')

# Tercera parte, la implementación general del juego...
# Segmentos.
segments = []
highest_score = 0