from idlelib import window

import pygame
from random import randint, choice
from pygame import display
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.time import Clock

pygame.init()
disparo = 0
tamanho = 800, 600  # variável que absorve o tamanho do plano em X e Y
superficie = display.set_mode((tamanho))  # variável que absorve a contrução do plano.
display.set_caption('O  Homem Aranha')  # funcão que escreve o nome da janela.
fundo = scale(load('images/cidade.jpg'),
              tamanho)  # como a imagem é maior que o plano, usamos a função SCALE para transformar a imagem no tamanho do plano.


class HomemAranha(Sprite):  # criamos o primeiro sprint que irá compor o jogo, o objeto principal.
    def __init__(self, teia):
        super().__init__()  # defino essa função será usada em outras classes como herança.

        self.image = load('images/homemaranha_small.png')  # carrego a imagem e em seguida tranfiro para uma variável.
        self.rect = self.image.get_rect()  # uso a função get_rect na imagem, onde irá me permitir o movimento no plano.
        self.velocidade = 2
        self.teia = teia

    def update(self):

        keys = pygame.key.get_pressed()  # recebe o movimento

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade

    def soltarTeia(self):
        if len(self.teia) < 15:
            self.teia.add(
                Teia(*self.rect.center)
            )


class Teia(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self, x, y):
        super().__init__()

        self.image = load('images/teia_small.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.x += 1
        if self.rect.x > tamanho[0]:
            self.kill()


class Inimigo(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()

        self.image = load('images/inimigo_1.png')
        self.rect = self.image.get_rect(
            center=(800, randint(10, 500))  # retorna posição aleatoria.
        )

    def update(self):
        self.rect.x -= 0.1


class Inimigo(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()

        self.image = load('images/inimigo_1.png')
        self.rect = self.image.get_rect(
            center=(800, randint(10, 500))  # retorna posição aleatoria.
        )

    def update(self):
        self.rect.x -= 1


class Chefao(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()
        self.win = False
        self.image = load('images/inimigo_2.png')
        self.rect = self.image.get_rect(
            center=(800, 300)  # retorna posição aleatoria.
        )

    def update(self):
        self.rect.x -= 0.1
        if self.rect.x > tamanho[0]:
            self.win = True



# Espaço do display
grupo_inimigo = Group()
grupo_chefao = Group()
grupo_aranha = Group()
homem_aranha = HomemAranha(grupo_aranha)
grupo_geral = GroupSingle(homem_aranha)
boss = Chefao()
grupo_inimigo.add(Inimigo())
grupo_chefao.add(boss)

round = 0
morte = 0
morte_player = 0
clock = Clock()
morte_p_recente = False

def placard(fase):
    if fase == 1:
        font = pygame.font.SysFont("arial", 15, True, False)
        placard_fase1_1 = font.render('Minhas mortes: ' + str(morte_player) + '/3',
                                    True, (0, 0, 0))
        placard_fase1_2 = font.render(
            'Mortes Inimigo: ' + str(morte) + '/20',
            True, (0, 0, 0))
        placard_fase1_rect_1 = placard_fase1_1.get_rect()
        # placard_fase1_rect_2 = pygame.draw.rect(superficie,(255,255,255),rect,200,7,0,0,0)
        placard_fase1_rect_2 = placard_fase1_2.get_rect()
        placard_fase1_rect_2.x = 645
        superficie.blit(placard_fase1_1, placard_fase1_rect_1)
        superficie.blit(placard_fase1_2, placard_fase1_rect_2)
    if fase == 2:
        font = pygame.font.SysFont("arial", 15, True, False)
        placard_fase1_1 = font.render('Minhas mortes: ' + str(morte_player) + '/3',
                                    True, (0, 0, 0))
        placard_fase1_2 = font.render(
            'Boss: ' + str(disparo) + '/20',
            True, (0, 0, 0))
        placard_fase1_rect_1 = placard_fase1_1.get_rect()
        # placard_fase1_rect_2 = pygame.draw.rect(superficie,(255,255,255),rect,200,7,0,0,0)
        placard_fase1_rect_2 = placard_fase1_2.get_rect()
        placard_fase1_rect_2.x = 718
        superficie.blit(placard_fase1_1, placard_fase1_rect_1)
        superficie.blit(placard_fase1_2, placard_fase1_rect_2)

def interactions(type):
    if type == 1:
        font = pygame.font.SysFont("arial", 30, True, False)
        placard_fase1 = font.render("GAME OVER",
                                True, (252, 7, 3))
        rect = pygame.Rect(300,300, 0, 0)
        superficie.blit(placard_fase1, rect)
    elif type == 2:
        font = pygame.font.SysFont("arial", 30, True, False)
        placard_fase1 = font.render("VENCEDOR!",
                                True, (60, 219, 11))
        rect = pygame.Rect(300,300, 0, 0)
        superficie.blit(placard_fase1, rect)

def limpaJogo():
    grupo_geral.empty()
    grupo_inimigo.empty()
    grupo_chefao.empty()
    grupo_aranha.empty()
    grupo_aranha.empty()

placard_mode = 1

while True:

    clock.tick(120)
    if round % 500 == 0:
        grupo_inimigo.add(Inimigo())

    if morte_p_recente and round % 200 == 0:
        grupo_geral.add(homem_aranha)

    superficie.blit(fundo, (
        0, 0))  # Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.

    placard(placard_mode)

    grupo_geral.draw(superficie)  # Desenhar o objeto no plano

    if (morte < 20):
        grupo_inimigo.draw(superficie)
        grupo_inimigo.update()
        disparo = 0
    else:
        placard_mode = 2
        grupo_chefao.draw(superficie)
        grupo_chefao.update()

    grupo_aranha.draw(superficie)

    grupo_geral.update()
    grupo_aranha.update()

    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                homem_aranha.soltarTeia()

    if groupcollide(grupo_aranha, grupo_inimigo, True, True):
        morte += 1


    if groupcollide(grupo_inimigo, grupo_geral, False, True):
        morte_player += 1
        morte_p_recente = True

    if groupcollide(grupo_chefao, grupo_geral, False, True):
        morte_player += 1
        morte_p_recente = True

    if disparo == 20:
        morte_p_recente = False
        limpaJogo()
        interactions(2)
        resposta = True
    else:
        resposta = False

    if groupcollide(grupo_aranha, grupo_chefao, True, resposta):
        disparo += 1
    if morte_player == 3 or boss.win:
        morte_p_recente = False
        limpaJogo()
        interactions(1)

    round += 1
    display.update()  # a função update atualiza os frames.
