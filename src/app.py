from core.base import Base

class App(Base):

    def __init__(self, screen_size=[1280, 720]) -> None:
        super().__init__(screen_size)

    def initialize(self) -> None:
        return super().initialize()

    def update(self) -> None:
        return super().update()

if __name__ == "__main__":
    App().run()