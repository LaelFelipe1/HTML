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
nome_jogo = pygame.display.set_caption("My Project")


# Movimentos
UP = (0, -20)
DOWN = (0, 20)
RIGHT = (20, 0)
LEFT = (-20, 0)
direcao_inicial = RIGHT
# Loop
deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                direcao_inicial = LEFT
            elif event.key == pygame.K_s:
                direcao_inicial = DOWN
            elif event.key == pygame.K_d:
                direcao_inicial = RIGHT
            elif event.key == pygame.K_w:
                direcao_inicial = UP
    # Desenhar bola
    pygame.draw.circle(tela, vermelho, (50, 50), 50, 50)
    # Desenhar linha
    pygame.draw.rect(tela, azul, (50, 300, 500, 50))

    #Atualizar tela
    pygame.display.update()