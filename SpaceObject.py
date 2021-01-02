import pyglet
from Settings import WINDOW_HEIGHT, WINDOW_WIDTH

class SpaceObject:
    def __init__(self, game_batch = None, game_objects=None, x=0, y=0, x_speed=0, y_speed=0, rotation=0, image=''):
        self.isdead = False
        self.game_batch = game_batch
        self.objects = game_objects
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rotation
        self.image = pyglet.image.load(image)
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=self.game_batch)
        self.radius = self.image.height // 2

    def die(self, dt=0):
        self.isdead = True

    def distance(self,a, b, wrap_size):
        """Distance in one direction (x or y)"""
        result = abs(a - b)
        if result > wrap_size / 2:
            result = wrap_size - result
        return result

    def overlaps(self,a, b):
        """Returns true iff two space objects overlap"""
        distance_squared = (self.distance(a.x, b.x, WINDOW_WIDTH) ** 2 +
                            self.distance(a.y, b.y, WINDOW_HEIGHT) ** 2)
        max_distance_squared = (a.radius + b.radius) ** 2
        return distance_squared < max_distance_squared

    