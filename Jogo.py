import pygame
import random

# Defina a classe Bala aqui
class Bala(pygame.sprite.Sprite):
    # ...
    pass

# Define as cores que serão utilizadas no jogo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define as dimensões da tela do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classe para representar a nave do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

# Classe para representar os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)


# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu jogo Shoot 'em up!")

# Cria os grupos de sprites para os jogadores e inimigos
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Cria o jogador
player = Player()
all_sprites.add(player)

# Cria 10 inimigos e adiciona ao grupo de inimigos e de todos os sprites
for i in range(10):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

# Define o clock do jogo
clock = pygame.time.Clock()

# Define a fonte e a pontuação do jogador
font = pygame.font.SysFont(None, 30)
score = 0

# Loop principal do jogo
running = True
while running:
    # Trata os eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza os sprites
    all_sprites.update()

    # Verifica colisões entre jogadores e inimigos
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        # Diminui a pontuação do jogador se houver colisão
        score -= 1
        if score < 0:
            score = 0
        # Reinicia o jogo
        all_sprites.empty()
        enemies.empty()
        player = Player()
        all_sprites.add(player)
        for i in range(10):
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)

    # Dessenha os sprites na tela
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Cria um botão de saída do jogo
    button_font = pygame.font.SysFont(None, 30)
    button_text = button_font.render("Sair", True, WHITE)
    button_rect = button_text.get_rect()
    button_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)

    # Desenha o botão de saída do jogo
    screen.blit(button_text, button_rect)
   
   # Desenha a pontuação na tela
    score_font = pygame.font.SysFont(None, 30)
    score_text = score_font.render("Pontuação: " + str(score), True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topright = (SCREEN_WIDTH - 20, 20)
    screen.blit(score_text, score_rect)

    # verifica se a tecla de espaço está pressionada
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # cria uma nova bala e adiciona à lista de balas
                nova_bala = Bala(jogador.rect.centerx, jogador.rect.top)
                balas.add(nova_bala)

    # Verifica se o botão de saída foi clicado
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            running = False

    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de atualização do jogo
    clock.tick(60)
