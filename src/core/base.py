# external imports
import pygame as pg
import sys

# core imports
from core.input import Input

class Base(object):

    def __init__(self, screen_size=[1280, 720]) -> None:
        print(f"Starting up..")
        # initialize pygame
        pg.init()
        # set display flags
        display_flags = pg.DOUBLEBUF | pg.OPENGL
        # init buffers for antialiasing
        pg.display.gl_set_attribute( pg.GL_MULTISAMPLEBUFFERS, 1 )
        pg.display.gl_set_attribute( pg.GL_MULTISAMPLESAMPLES, 4 )
        # use a core opengl profile for cross platform
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK,
            pg.GL_CONTEXT_PROFILE_CORE )
        self._Screen = pg.display.set_mode(
            screen_size,
            display_flags )
        pg.display.set_caption("Math is neat!")

        # running variable
        self._Running = True

        # elapsed time variable
        self._Clock = pg.time.Clock()

        # set up input component
        self._Input = Input()

    def initialize(self) -> None:
        print(f"Initializing...")
        # specified in inherited class
        pass

    def update(self) -> None:
        # specified in inherited class
        pass

    def shutdown(self) -> None:
        print(f"Shutting down..")
        pg.quit()
        sys.exit()

    def run(self) -> None:

        # startup
        self.initialize()

        # main loop
        while self._Running:

            # process input
            self._Input.update()
            if self._Input._Quit:
                self._Running = False

            # update
            self.update()

            # render
            pg.display.flip()

            # enforce fps (default 60)
            self._Clock.tick(60)

        # shutdown
        self.shutdown()