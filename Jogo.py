"""
Shoot 'em Up Game - Jogo de Nave Espacial

Um jogo simples de shoot 'em up onde o jogador controla uma nave espacial
e deve desviar dos inimigos que caem do topo da tela.

@author: Anderson C. (@AndersonC75)
@license: MIT License
@version: 1.0.0
@created: 2023-05-07
@updated: 2025-09-21

Como executar:
    python Jogo.py

Controles:
    ← Seta Esquerda: Mover nave para a esquerda
    → Seta Direita: Mover nave para a direita
    Botão "Sair": Fechar o jogo
    
Saída:
    Jogo em janela gráfica com pontuação em tempo real.
    O jogo reinicia automaticamente após colisões.

Dependências:
    - pygame 2.0+
    - Python 3.7+
"""

import pygame
import random

# Define as cores que serão utilizadas no jogo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define as dimensões da tela do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Bala(pygame.sprite.Sprite):
    """Classe para representar as balas do jogador (não implementada completamente)."""
    def __init__(self):
        super().__init__()
        # TODO: Implementar funcionalidade de balas
        pass


class Player(pygame.sprite.Sprite):
    """Classe para representar a nave do jogador."""
    
    def __init__(self):
        """Inicializa o jogador com posição inicial na parte inferior da tela."""
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - 100
        
    def update(self):
        """Atualiza a posição do jogador baseado nas teclas pressionadas."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    """Classe para representar os inimigos que caem do topo da tela."""
    
    def __init__(self):
        """Inicializa um inimigo em posição aleatória no topo da tela."""
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        
    def update(self):
        """Atualiza a posição do inimigo, movendo-o para baixo e reposicionando quando sai da tela."""
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)


def main():
    """Função principal que executa o loop do jogo."""
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
        
        # Desenha os sprites na tela
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        # Cria e desenha o botão de saída do jogo
        button_font = pygame.font.SysFont(None, 30)
        button_text = button_font.render("Sair", True, WHITE)
        button_rect = button_text.get_rect()
        button_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        screen.blit(button_text, button_rect)
        
        # Desenha a pontuação na tela
        score_font = pygame.font.SysFont(None, 30)
        score_text = score_font.render("Pontuação: " + str(score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topright = (SCREEN_WIDTH - 20, 20)
        screen.blit(score_text, score_rect)
        
        # Verifica se o botão de saída foi clicado
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                running = False
        
        # Atualiza a tela
        pygame.display.flip()
        
        # Define a taxa de atualização do jogo (60 FPS)
        clock.tick(60)
    
    # Encerra o Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
