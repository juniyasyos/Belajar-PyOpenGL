import pygame as pg
from OpenGL.GL import *
import numpy
import ctypes

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640,480), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1,0.2,0.2,1)

        self.mainLoop()

    def mainLoop(self):
        run = True 
        while(run):
            for i in pg.event.get():
                if (i.type == pg.QUIT):
                    run = False
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            self.clock.tick(60)
        self.quit()
    
    def quit():
        pg.quit()


class kotak:
    def __init__(self):
        self.verticels = {
            -0.5,-0.5,-0.0,1.0,-0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5,0.0,0.0,0.0,1.0
        }

        self.verticels = np.array(self.verticels, dtype=np.float32)

        self.vertex_count = 3

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGetBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER. self.verticels.nbytes, self.verticels, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24,ctypes.c_void_p(0))
        glEnableVertexArrayAttrib(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24,ctypes.c_void_p(12))


if __name__ == "__main__":
    myApp = App()
