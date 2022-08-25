import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertice = (
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1)
)

aresta = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
)


def quadrado():
    """Diferença entre o Lines e o Line:
        Lines permite que um vertice permita apenas uma ligação, já o lines permite várias."""
    glBegin(GL_LINES)
    for temp_aresta in aresta:
        for vertex in temp_aresta:
            glVertex2iv(vertice[vertex]) #2iv = bidimensional
    glEnd()

def main():
    pygame.init() #Inicialize todos os módulos pygame importados
    display = (700, 700) #Define o tamanho da tela (Plano)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #insere o código do pygame dentro do display de demonstração
    gluPerspective(80, #quantos graus o objeto será posicinado
                   (display[0]/display[1]), #tamanho da dela, no caso 700x700,
                   1, #o qual distante o objeto será renderizado
                   40 #Distância a ser desenhado.
    )

    glTranslatef(
        0, #X
        0, #Y
        -3  #Z
    )

    glRotatef(45,  # angulo de retação
              0,  # x
              0,  # y
              0  # z
              )  # Transformação geometrica de rotação



    glColor3f(254,253,252)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glTranslatef(
            0,  # X
            0,  # Y
            -3  # Z
        )

        glRotatef(45,  # angulo de retação
                  3,  # x
                  -3,  # y
                  0  # z
                  )  # Transformação geometrica de rotação


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        quadrado()
        pygame.display.flip()

        pygame.time.wait(60)


main()