# coding: utf-8
from tkinter import messagebox
import sys
import os
import pygame

import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the crowd sound as a Sound object
crowd_sound = pygame.mixer.Sound("/Users/nahomflagot/Downloads/crowd.mp3")
victory_sound = pygame.mixer.Sound("/Users/nahomflagot/Downloads/victory.mp3")
goal_sound = pygame.mixer.Sound("/Users/nahomflagot/Downloads/goal.mp3")
# Set volume only for the crowd sound (range 0.0 to 1.0)
crowd_sound.set_volume(.5)  # Adjust as needed

# Play the crowd sound on a loop (-1 for infinite loop)
crowd_sound.play(-1)

from graphics import *
from variaveis import *
import time, math
from graphics import *
import time

# Create the window
tela = GraphWin("Old Head Soccer", 500, 500)

# Initialize the game time (120 seconds)
game_time = 120

# Create a Text object to display the timer
timer_text = Text(Point(250, 20), f"Time Left: {game_time}")
timer_text.setSize(18)  # Set the font size
timer_text.setTextColor("red")  # Set the text color
timer_text.draw(tela)

# Function to update the timer display
def update_timer(time_left):
    timer_text.setText(f"Time Left: {time_left}")
# Set target frame rate (e.g., 30 FPS)
TARGET_FPS = 30
frame_time = 1 / TARGET_FPS

# Function to control frame rate
def frame_delay(last_time):
    current_time = time.time()
    delta_time = current_time - last_time
    if delta_time < frame_time:
        time.sleep(frame_time - delta_time)
    return current_time

#### VARIÁVEIS ####
tela = GraphWin("Head Soccer", x, y, False)

intro = Image(Point(x / 2, y / 2), "Imagens/intro2.gif")
intro.draw(tela)

jogar = Image(Point(175, 500), "Imagens/jogar.gif")
jogar.draw(tela)

sair = Image(Point(425, 500), "Imagens/sair.gif")
sair.draw(tela)

####################
## LOOP DA INTRO ###
####################
last_time = time.time()

while True:
    current_time = time.time()
    dt = current_time - last_time  # Calculate delta time
    last_time = current_time  # Update last_time

    enter = tela.checkKey()
    check = tela.checkMouse()

    if check is not None:
        check_x = check.getX()
        check_y = check.getY()
        if (470 <= check_y <= 530) and (75 <= check_x <= 275):
            break
        elif (470 <= check_y <= 530) and (325 <= check_x <= 525):
            tela.close()
            break

    if enter == "Return":
        break

    time.sleep(max(0, 0.07 - dt))  # Adjust sleep dynamically based on delta time


c_bola = Circle(Point(x / 2, 100), raio)
c_bola.draw(tela)

cabeca = Circle(Point(300, 491), raio_cabeca)
cabeca.draw(tela)
pe = Circle(Point(300, 529), raio)

pe.draw(tela)

cabeca2 = Circle(Point(900, 491), raio_cabeca)
cabeca2.draw(tela)
pe2 = Circle(Point(900, 529), raio)
pe2.draw(tela)

col_trave1 = Circle(Point(105, 360), 5)
col_trave1.draw(tela)

col_trave2 = Circle(Point(x - 105, 360), 5)
col_trave2.draw(tela)

bg = Image(Point(x / 2, y / 2), "Imagens/bg.gif")
bg.draw(tela)

#### BONECO ESQUERDO ####
boneco = Image(Point(300, 503), "Imagens/LeftChar.gif")
boneco.draw(tela)

#### BONECO DIREITO ####
boneco2 = Image(Point(900, 503), "Imagens/RightChar.gif")
boneco2.draw(tela)

#### BOLA ####
bola = Image(Point(x / 2, 100), "Imagens/ball.gif")
bola.draw(tela)

### TRAVE ESQUERDA ###
trave1 = Image(Point(55, 450), "Imagens/trave1.gif")
trave1.draw(tela)

### TRAVE DIREITA ###
trave2 = Image(Point(x - 55, 450), "Imagens/trave2.gif")
trave2.draw(tela)

x1_trave2 = trave2.getAnchor().getX() - larg_t
x2_trave2 = trave2.getAnchor().getX() + larg_t

x1_trave1 = trave1.getAnchor().getX() - larg_t
y1_trave = trave1.getAnchor().getY() - alt_t
x2_trave1 = trave1.getAnchor().getX() + larg_t
y2_trave = trave1.getAnchor().getY() + alt_t

x_cabeca = cabeca.getCenter().getX()
y_cabeca = cabeca.getCenter().getY()
x_cabeca2 = cabeca2.getCenter().getX()
y_cabeca2 = cabeca2.getCenter().getY()

x_pe = pe.getCenter().getX()
y_pe = pe.getCenter().getY()
x_pe2 = pe2.getCenter().getX()
y_pe2 = pe2.getCenter().getY()

x_bola = c_bola.getCenter().getX()
y_bola = c_bola.getCenter().getY()

placar1 = Text(Point(x / 2 + 20, 40), "")
placar1.setStyle("bold")
placar1.setTextColor("white")
placar1.setSize(25)
placar1.draw(tela)

placar2 = Text(Point(x / 2 - 20, 40), "")
placar2.setStyle("bold")
placar2.setTextColor("white")
placar2.setSize(25)
placar2.draw(tela)

# pygame.mixer.init()
# pygame.mixer.music.load('Sons/gol.wav')

#### LOOP DO JOGO ###
tela.ligar_Buffer()

while True:
    placar1.setText(contador_gol1)
    placar2.setText(contador_gol2)
    while not (gol):
        lista = tela.checkKey_Buffer()
        update()

        colisao_cabeca = math.hypot((x_cabeca - x_bola), (y_cabeca - y_bola))
        colisao_pe = math.hypot((x_pe - x_bola), (y_pe - y_bola))

        colisao_cabeca2 = math.hypot((x_cabeca2 - x_bola), (y_cabeca2 - y_bola))
        hitbox_size = 19  # Quadruples hitbox area
        colisao_pe2 = math.hypot((x_pe2 - x_bola) * hitbox_size, (y_pe2 - y_bola) * hitbox_size)
        if (not (y_bola + raio <= y1_trave and x_bola >= x1_trave2)) and (
            not (y_bola + raio <= y1_trave and x_bola <= x2_trave1)
        ):
            if y_bola + raio < chao:
                if vely_bola < 20:
                    vely_bola += 0.4
                if y_bola + raio + vely_bola > chao:
                    vely_bola = chao - (y_bola + raio)
            else:
                if not (vely_bola <= 3):
                    vely_bola = (vely_bola * -0.7) // 1
                else:
                    vely_bola = 0
            cont_trave = 0
        else:
            if y_bola + raio < y1_trave:
                if vely_bola < 12:
                    vely_bola += 0.4
                if y_bola + raio + vely_bola > y1_trave:
                    vely_bola = y1_trave - (y_bola + raio)
            cont_trave += 1
            if cont_trave >= 60:
                if x_bola > x / 2:
                    bola.move(-1, 0)
                    c_bola.move(-1, 0)
                else:
                    bola.move(1, 0)
                    c_bola.move(1, 0)

        if y_bola + raio > chao:
            c_bola.move(0, chao - (y_bola + raio))
            bola.move(0, chao - (y_bola + raio))

        if y_bola + raio == chao:
            if velx_bola > 0:
                velx_bola -= atrito
            if velx_bola < 0:
                velx_bola += atrito

        if colisao_cabeca <= 80:
            if x_bola - raio >= x_cabeca + raio_cabeca:
                if (
                    (x_cabeca - raio_cabeca)
                    <= (x_bola - raio + velx_bola)
                    <= (x_cabeca + raio_cabeca)
                ):
                    velx_bola = (x_cabeca + raio_cabeca) - (x_bola - raio)

            if not (x_bola == x_cabeca):
                a_cabeca = (y_cabeca - y_bola) / (x_cabeca - x_bola)
                teta_cabeca = math.atan(a_cabeca)
            else:
                teta_cabeca = 0

            if not (x_bola == x_pe):
                a_pe = (y_pe - y_bola) / (x_pe - x_bola)
                teta_pe = math.atan(a_pe)
            else:
                teta_pe = 0

        if colisao_cabeca2 <= 80:

            if x_bola + raio <= x_cabeca2 - raio_cabeca:
                if (
                    (x_cabeca2 - raio_cabeca)
                    <= (x_bola + raio + velx_bola)
                    <= (x_cabeca2 + raio_cabeca)
                ):
                    velx_bola = (x_cabeca2 - raio_cabeca) - (x_bola + raio)

            if not (x_bola == x_pe2):
                a_pe2 = (y_pe2 - y_bola) / (x_pe2 - x_bola)
                teta_pe2 = math.atan(a_pe2)
            else:
                teta_pe2 = 0

            if not (x_bola == x_cabeca2):
                a_cabeca2 = (y_cabeca2 - y_bola) / (x_cabeca2 - x_bola)
                teta_cabeca2 = math.atan(a_cabeca2)
            else:
                teta_cabeca2 = 0

        if not (2 * raio >= colisao_cabeca and 2 * raio >= colisao_pe):
            if 2 * raio >= colisao_pe:  ### COLISÃO COM O PÉ ###
                if chute:
                    vely_bola = (2.8 * vel * math.sin(teta_pe)) // 1
                    velx_bola = (1.2 * vel * math.cos(teta_pe)) // 1
                else:
                    if y_pe <= y_bola and x_pe >= x_bola:
                        velx_bola = (vel * math.cos(teta_pe)) // -1
                        vely_bola = (vel * math.sin(teta_pe)) // -1
                    else:
                        velx_bola = (vel * math.cos(teta_pe)) // 1
                        vely_bola = (vel * math.sin(teta_pe)) // 1

                if y_bola + raio + vely_bola > chao:
                    vely_bola = chao - (y_bola + raio)
            if not (chute):
                if (
                    2 * (raio_cabeca - 8) >= colisao_cabeca
                ):  ### COLISAO COM A CABEÇA ###
                    if (y_cabeca <= y_bola and x_cabeca >= x_bola) or (
                        y_cabeca >= y_bola and x_cabeca >= x_bola
                    ):
                        velx_bola = (1.2 * vel * math.cos(teta_cabeca)) // -1
                        vely_bola = (2 * vel * math.sin(teta_cabeca)) // -1
                    else:
                        velx_bola = (vel * math.cos(teta_cabeca)) // 1
                        vely_bola = (vel * math.sin(teta_cabeca)) // 1
            else:
                if raio >= colisao_cabeca:  ### COLISAO COM A CABEÇA ###
                    if (y_cabeca <= y_bola and x_cabeca >= x_bola) or (
                        y_cabeca >= y_bola and x_cabeca >= x_bola
                    ):
                        velx_bola = (vel * math.cos(teta_cabeca)) // -1
                        vely_bola = (vel * math.sin(teta_cabeca)) // -1
                    else:
                        velx_bola = (vel * math.cos(teta_cabeca)) // 1
                        vely_bola = (vel * math.sin(teta_cabeca)) // 1

        else:
            velx_bola = (vel * math.cos(teta_pe)) // 1
            vely_bola = (vel * math.sin(teta_pe)) // 1

        if not (2 * raio >= colisao_cabeca2 and 2 * raio >= colisao_pe2):
            if 2 * raio >= colisao_pe2:  ### COLISÃO COM O PÉ ###
                if chute2:
                    vely_bola = (1.2 * vel * math.cos(teta_pe2)) // -1
                    velx_bola = (vel * math.cos(teta_pe2)) // -1
                else:
                    if y_pe2 <= y_bola and x_pe2 >= x_bola:
                        velx_bola = (vel * math.cos(teta_pe2)) // -1
                        vely_bola = (vel * math.sin(teta_pe2)) // -1
                    else:
                        velx_bola = (vel * math.cos(teta_pe2)) // 1
                        vely_bola = (vel * math.sin(teta_pe2)) // 1

                if y_bola + raio + vely_bola > chao:
                    vely_bola = chao - (y_bola + raio)
            if not (chute2):
                if (
                    2 * (raio_cabeca - 8) >= colisao_cabeca2
                ):  ### COLISAO COM A CABEÇA ###
                    if (y_cabeca2 <= y_bola and x_cabeca2 >= x_bola) or (
                        y_cabeca2 >= y_bola and x_cabeca2 >= x_bola
                    ):
                        velx_bola = (vel * math.cos(teta_cabeca2)) // -1
                        vely_bola = (vel * math.sin(teta_cabeca2)) // -1
                    else:
                        velx_bola = (vel * math.cos(teta_cabeca2)) // 1
                        vely_bola = (vel * math.sin(teta_cabeca2)) // 1
                else:
                    if raio >= colisao_cabeca2:  ### COLISAO COM A CABEÇA ###
                        if (y_cabeca2 <= y_bola and x_cabeca2 >= x_bola) or (
                            y_cabeca2 >= y_bola and x_cabeca2 >= x_bola
                        ):
                            velx_bola = (vel * math.cos(teta_cabeca2)) // -1
                            vely_bola = (vel * math.sin(teta_cabeca2)) // -1
                        else:
                            velx_bola = (vel * math.cos(teta_cabeca2)) // 1
                            vely_bola = (vel * math.sin(teta_cabeca2)) // 1

        else:
            velx_bola = (vel * math.cos(teta_pe2)) // -1
            vely_bola = (vel * math.sin(teta_pe2)) // -1

        bola.move(2 * velx_bola // 1, 2 * vely_bola // 1)
        c_bola.move(2 * velx_bola // 1, 2 * vely_bola // 1)

        if len(lista) > 0:
            if ("Left" in lista) and (x_cabeca2 - raio_cabeca > 0):
                boneco2.move(-vel, 0)
                cabeca2.move(-vel, 0)
                pe2.move(-vel, 0)

            if ("Right" in lista) and (x_cabeca2 + raio_cabeca < x):
                boneco2.move(vel, 0)
                cabeca2.move(vel, 0)
                pe2.move(vel, 0)

            if ("a" in lista) and (x_cabeca - raio_cabeca > 0):
                boneco.move(-vel, 0)
                cabeca.move(-vel, 0)
                pe.move(-vel, 0)

            if ("d" in lista) and (x_cabeca + raio_cabeca < x):
                boneco.move(vel, 0)
                cabeca.move(vel, 0)
                pe.move(vel, 0)

        if not (chute):
            if len(lista) > 0 and ("space" in lista):
                chute = True
        else:
            if cont_chute // 1 == 0:
                pe.move(0, 8)
                boneco.undraw()
                boneco = Image(
                    Point(boneco.getAnchor().getX(), boneco.getAnchor().getY()),
                    "Imagens/LeftChar_kick1.gif",
                )
                boneco.draw(tela)
            if cont_chute // 8 == 1:
                pe.move(2, -2)
                boneco.undraw()
                boneco = Image(
                    Point(boneco.getAnchor().getX(), boneco.getAnchor().getY()),
                    "Imagens/LeftChar_kick2.gif",
                )
                boneco.draw(tela)
            cont_chute += 1
            if cont_chute == 15:
                boneco.undraw()
                boneco = Image(
                    Point(boneco.getAnchor().getX(), boneco.getAnchor().getY()),
                    "Imagens/LeftChar.gif",
                )
                boneco.draw(tela)
                cont_chute = 0
                pe.move(-14, 6)
                chute = False

        if not (chute2):
            if len(lista) > 0 and ("Return" in lista):
                chute2 = True
        else:
            if cont_chute2 // 1 == 0:
                pe2.move(0, 8)
                boneco2.undraw()
                boneco2 = Image(
                    Point(boneco2.getAnchor().getX(), boneco2.getAnchor().getY()),
                    "Imagens/RightChar_kick1.gif",
                )
                boneco2.draw(tela)
            if cont_chute2 // 8 == 1:
                pe2.move(-2, -2)
                boneco2.undraw()
                boneco2 = Image(
                    Point(boneco2.getAnchor().getX(), boneco2.getAnchor().getY()),
                    "Imagens/RightChar_kick2.gif",
                )
                boneco2.draw(tela)
            cont_chute2 += 1
            if cont_chute2 == 15:
                boneco2.undraw()
                boneco2 = Image(
                    Point(boneco2.getAnchor().getX(), boneco2.getAnchor().getY()),
                    "Imagens/RightChar.gif",
                )
                boneco2.draw(tela)
                cont_chute2 = 0
                pe2.move(14, 6)
                chute2 = False

        ##### PULO BONECO2 ####
        if not (pulando):
            if len(lista) > 0 and ("w" in lista):
                pulando = True
                dy = 3  # Increased initial jump strength
        else:
            if cont <= 30:  # Increased jump duration
                if cont // 15 == 0:  # Longer ascent
                    boneco.move(0, -dy)
                    cabeca.move(0, -dy)
                    pe.move(0, -dy)
                    dy += 1
                if cont // 15 == 1:  # Longer descent
                    dy -= 1
                    boneco.move(0, dy)
                    cabeca.move(0, dy)
                    pe.move(0, dy)
                cont += 1
            else:
                pulando = False
                cont = 0

        if not (pulando2):
            if len(lista) > 0 and ("Up" in lista):
                pulando2 = True
                dy2 = 3  # Increased initial jump strength
        else:
            if cont2 <= 30:  # Increased jump duration
                if cont2 // 15 == 0:  # Longer ascent
                    boneco2.move(0, -dy2)
                    cabeca2.move(0, -dy2)
                    pe2.move(0, -dy2)
                    dy2 += 1
                if cont2 // 15 == 1:  # Longer descent
                    dy2 -= 1
                    boneco2.move(0, dy2)
                    cabeca2.move(0, dy2)
                    pe2.move(0, dy2)
                cont2 += 1
            else:
                pulando2 = False
                cont2 = 0

        if x_bola + raio > x:
            if velx_bola > 0:
                velx_bola = (velx_bola * -1) * 0.7
        if x_bola - raio < 0:
            if velx_bola < 0:
                velx_bola = (velx_bola * -1) * 0.7
        if y_bola - raio < 0:
            if vely_bola < 0:
                vely_bola = (vely_bola * -1) * 0.7

        x_boneco = boneco.getAnchor().getX()
        y_boneco = boneco.getAnchor().getY()
        x_boneco2 = boneco2.getAnchor().getX()
        y_boneco2 = boneco2.getAnchor().getY()

        x_cabeca = cabeca.getCenter().getX()
        y_cabeca = cabeca.getCenter().getY()
        x_cabeca2 = cabeca2.getCenter().getX()
        y_cabeca2 = cabeca2.getCenter().getY()

        x_pe = pe.getCenter().getX()
        y_pe = pe.getCenter().getY()
        x_pe2 = pe2.getCenter().getX()
        y_pe2 = pe2.getCenter().getY()

        x_bola = c_bola.getCenter().getX()
        y_bola = c_bola.getCenter().getY()

        x_t2 = col_trave2.getCenter().getX()
        y_t2 = col_trave2.getCenter().getY()

        x_t1 = col_trave1.getCenter().getX()
        y_t1 = col_trave1.getCenter().getY()

        if x_bola > 900:
            if not (x_bola == x_t2):
                a_t2 = (y_t2 - y_bola) / (x_t2 - x_bola)
                teta_t2 = math.atan(a_t2)
            else:
                teta_t2 = 0
            if y_bola + raio <= y1_trave and x_bola >= x1_trave2:
                if y_bola + raio + vely_bola > y1_trave - 5:
                    if vely_bola < 3:
                        vely_bola = 0
                    vely_bola = (vely_bola * -0.8) // 1

            if raio >= math.hypot((x_t2 - x_bola), (y_t2 - y_bola)):
                velx_bola = (vel * math.cos(teta_t2)) // -1
                vely_bola = (vel * math.sin(teta_t2)) // -1

            if (x_bola >= x1_trave2) and (y_bola - raio >= y1_trave):
                # pygame.mixer.music.play()
                gol = True
                lado = "right"

        elif x_bola < 300:
            if not (x_bola == x_t1):
                a_t1 = (y_t1 - y_bola) / (x_t1 - x_bola)
                teta_t1 = math.atan(a_t1)
            else:
                teta_t1 = 0
            if y_bola + raio <= y1_trave and x_bola <= x2_trave1:
                if y_bola + raio + vely_bola > y1_trave - 5:
                    if vely_bola < 3:
                        vely_bola = 0
                    vely_bola = (vely_bola * -0.8) // 1

            if raio >= math.hypot((x_t1 - x_bola), (y_t1 - y_bola)):
                velx_bola = (vel * math.cos(teta_t1)) // 1
                vely_bola = (vel * math.sin(teta_t1)) // 1

            if (x_bola <= x2_trave1) and (y_bola - raio >= y1_trave):
                # pygame.mixer.music.play()
                gol = True
                lado = "left"

        time.sleep(0.018)
        tela.update()

    if lado == "left":
        contador_gol1 += 1
    elif lado == "right":
        contador_gol2 += 1


    def reset_game():
        python = sys.executable
        os.execl(python, python, *sys.argv)  # Restarts the script from the beginning


    def check_game_over():
        global contador_gol1, contador_gol2  # Ensure we modify the global variables

        if contador_gol1 == 3:
            choice = messagebox.askyesno("Game Over", "Player 2 wins! Do you want to play again?")
            if choice:
                contador_gol1 = 0
                contador_gol2 = 0  # Reset the score to 0-0 and continue
                reset_game()
            else:
                reset_game()

        elif contador_gol2 == 3:
            choice = messagebox.askyesno("Game Over", "Player 1 wins! Do you want to play again?")
            if choice:
                contador_gol1 = 0
                contador_gol2 = 0  # Reset the score to 0-0 and continue
            else:
                reset_game()





    check_game_over()

    gol = False
    pulando = False
    pulando2 = False
    dy = 1
    dy2 = 1
    cont = 0
    cont2 = 0
    cont_chute = 0
    cont_chute2 = 0
    bola.move(x / 2 - x_bola, 100 - y_bola)
    c_bola.move(x / 2 - x_bola, 100 - y_bola)
    boneco.move(300 - x_boneco, 503 - y_boneco)
    cabeca.move(300 - x_cabeca, 491 - y_cabeca)
    pe.move(300 - x_pe, 529 - y_pe)
    boneco2.move(900 - x_boneco2, 503 - y_boneco2)
    cabeca2.move(900 - x_cabeca2, 491 - y_cabeca2)
    pe2.move(900 - x_pe2, 529 - y_pe2)
    velx_bola = 0
    vely_bola = 0

    time.sleep(1)
