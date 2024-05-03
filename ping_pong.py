import pygame

# Iniciar o Pygame
pygame.init()


# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


# Definições de tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
nome_jogo = pygame.display.set_caption("Ping Pong - Lael")
tela.fill(branco)

#Criar traves
rect1 = pygame.Rect(4, 170, 15, 60)
rect2 = pygame.Rect(580, 170, 15, 60)


# Movimentos
UP = (0, -20)
DOWN = (0, 20)
RIGHT = (20, 0)
LEFT = (-20, 0)


# Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect1.move_ip(UP)
            elif event.key == pygame.K_s:
                rect1.move_ip(DOWN)
            elif event.key == pygame.K_DOWN:
                rect2.move_ip(DOWN)
            elif event.key == pygame.K_UP:
                rect2.move_ip(UP)

    # Desenhar bola
    pygame.draw.circle(tela, vermelho, (300, 200), 10, 10)
    # Desenhar retângulo
    pygame.draw.rect(tela, azul, rect1)
    pygame.draw.rect(tela, azul, rect2)



    #Atualizar tela
    pygame.display.update()
