from code.entity import Entity


class Shot(Entity):

    def __init__(self, name, position=(0,0)):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += 3
