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

# Implementación del juego:
while True:
    window.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        snake.shape("square")
        snake.color("green")

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()
        puntuacion_jugador = 0
        tiempo_retraso = 0.1
        score_pen.clear()
        score_pen.write("Your score: 0 | Highest score: {}".format(highest_score), align="center", font=("Arial", 24, "normal"))

    if snake.distance(food) < 20:
        coord_x = random.randint(-270, 270)
        coord_y = random.randint(-270, 270)
        food.goto(coord_x, coord_y)
        # Agregar un segmento:
        added_segment = turtle.Turtle()
        added_segment.speed(0)
        added_segment.shape("square")
        added_segment.color("white")
        added_segment.penup()
        segments.append(added_segment)
        tiempo_retraso -= 0.001
        puntuacion_jugador += 5

        if puntuacion_jugador > highest_score:
            highest_score = puntuacion_jugador
            score_pen.clear()
            score_pen.write("Your score: {} | Highest score: {}".format(puntuacion_jugador, highest_score), align="center", font=("Arial", 24, "normal"))

    for i in range(len(segments) -1, 0, -1):
        coord_x = segments[i - 1].xcor()
        coord_y = segments[i - 1].ycor()
        segments[i].goto(coord_x, coord_y)

    if len(segments) > 0:
        coord_x = snake.xcor()
        coord_y = snake.ycor()
        segments[0].goto(coord_x, coord_y)
    
    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "Stop"
            snake.color("white")
            snake.shape("square")

        for segment in segments:
            segment.goto(1000, 1000)
            segment.clear()
        
        puntuacion_jugador = 0
        tiempo_retraso = 0.1
        score_pen.clear()
        score_pen.write("Your score: 0 | Highest score: {}".format(highest_score), align="center", font=("Arial", 24, "normal"))

    time.sleep(tiempo_retraso)