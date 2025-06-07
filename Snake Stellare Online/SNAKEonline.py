import pygame
import time
import random

snake_img = pygame.image.load("C:\\Users\\verdi\OneDrive\\Documenti\\Snake Stellare Online\\snake.png")
food_img = pygame.image.load("C:\\Users\\verdi\OneDrive\\Documenti\\Snake Stellare Online\\apple.png")

# Ridimensiona (opzionale, per adattare a 20x20)
snake_img = pygame.transform.scale(snake_img, (20, 20))
food_img = pygame.transform.scale(food_img, (20, 20))



# Inizializza pygame
pygame.init()

# Colori
bianco = (255, 255, 255)
nero = (0, 0, 0)
rosso = (213, 50, 80)
verde = (0, 255, 0)
blu = (50, 153, 213)

# Dimensioni finestra
larghezza = 800
altezza = 600
finestra = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

# Imposta clock
clock = pygame.time.Clock()

# Dimensioni serpente e velocità
dimensione_blocco = 20
velocita_snake = 10

# Font
font_stile = pygame.font.SysFont("bahnschrift", 25)
font_punteggio = pygame.font.SysFont("comicsansms", 20)

# Carica l'immagine di sfondo
sfondo = pygame.image.load('C:\\Users\\verdi\OneDrive\\Documenti\\Snake Stellare Online\\background.png')  # Sostituisci con il nome del tuo file immagine
sfondo = pygame.transform.scale(sfondo, (800, 600))  # Ridimensiona l'immagine alla dimensione della finestra
sfondo_gameover = pygame.image.load("C:\\Users\\verdi\OneDrive\\Documenti\\Snake Stellare Online\\game_over.png")
sfondo_gameover = pygame.transform.scale(sfondo_gameover, (800, 600))

def punteggio(score):
    valore = font_punteggio.render("Score: " + str(score), True, nero)
    finestra.blit(valore, [0, 0])

def nostro_serpente(dimensione_blocco, lista_serpente):
    for pos in lista_serpente:
        finestra.blit(snake_img, (pos[0], pos[1]))

def messaggio(msg, colore):
    testo = font_stile.render(msg, True, colore)
    finestra.blit(testo, [larghezza / 6, altezza / 2.05])

def gioco():
    game_over = False
    game_close = False

    x1 = larghezza / 2
    y1 = altezza / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpente = []
    lunghezza_serpente = 1

    cibo_x = round(random.randrange(0, larghezza - dimensione_blocco) / 20.0) * 20.0
    cibo_y = round(random.randrange(0, altezza - dimensione_blocco) / 20.0) * 20.0

    finestra.blit(sfondo, (0, 0))  # Deve essere prima di tutto

    while not game_over:

        while game_close:
            finestra.blit(sfondo_gameover, (0, 0))
            testo_punteggio = font_punteggio.render("Punteggio: " + str(lunghezza_serpente - 1), True, nero)
            finestra.blit(testo_punteggio, ((larghezza - testo_punteggio.get_width()) // 2, 20))
            messaggio("Hai perso! Premi Q per uscire o C per continuare", nero)
            punteggio(lunghezza_serpente - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gioco()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -dimensione_blocco
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = dimensione_blocco
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -dimensione_blocco
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = dimensione_blocco
                    x1_cambio = 0

        if x1 >= larghezza or x1 < 0 or y1 >= altezza or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        finestra.blit(sfondo, (0, 0))
        finestra.blit(food_img, (cibo_x, cibo_y))

        testa = []
        testa.append(x1)
        testa.append(y1)
        lista_serpente.append(testa)
        if len(lista_serpente) > lunghezza_serpente:
            del lista_serpente[0]

        for x in lista_serpente[:-1]:
            if x == testa:
                game_close = True

        nostro_serpente(dimensione_blocco, lista_serpente)
        punteggio(lunghezza_serpente - 1)

        pygame.display.update()

        if x1 == cibo_x and y1 == cibo_y:
            cibo_x = round(random.randrange(0, larghezza - dimensione_blocco) / 20.0) * 20.0
            cibo_y = round(random.randrange(0, altezza - dimensione_blocco) / 20.0) * 20.0
            lunghezza_serpente += 1

        clock.tick(velocita_snake)

    pygame.quit()
    quit()

gioco()
