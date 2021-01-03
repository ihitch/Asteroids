import pyglet
import math
from Settings import WINDOW_HEIGHT, WINDOW_WIDTH
from pyglet.window import key
from Laser import Laser
from SpaceObject import SpaceObject

_ROTATION_SPEED = 4
ACCELERATION = 30
MAX_SPEED = 250
class Spaceship(SpaceObject):
    def __init__(self, batch,g_objects = None):
        super(Spaceship, self).__init__(game_batch=batch, game_objects=g_objects,x = WINDOW_HEIGHT / 2,y = WINDOW_WIDTH / 2, x_speed = 0, y_speed = 0, rotation = 0, image = 'Resources/playerShip1_orange.png')
        self.reload = 0.5
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        self.reload += dt
        if self.key_handler[key.D]:
            self.rotation = self.rotation - dt * _ROTATION_SPEED
        if self.key_handler[key.A]:
            self.rotation = self.rotation + dt * _ROTATION_SPEED
        if self.key_handler[key.W]:
            self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed += dt * ACCELERATION * math.sin(self.rotation)
            if self.x_speed > MAX_SPEED:
                self.x_speed = MAX_SPEED
            if self.y_speed > MAX_SPEED:
                self.y_speed = MAX_SPEED
        else:
            if abs(self.x_speed) > 1.5:
                self.x_speed -= dt * self.x_speed/5
            else:
                self.x_speed = 0
            if abs(self.y_speed) > 1.5:
                self.y_speed -= dt * self.y_speed/5
            else:
                self.y_speed = 0
        if self.key_handler[key.SPACE]:
            if self.reload > 0.5:
                self.fire()
                self.reload = 0.0
        
        self.x = (self.x + dt * self.x_speed) % 800
        self.y = (self.y + dt * self.y_speed) % 600
        self.sprite.rotation = 90 - math.degrees(self.rotation)
        self.sprite.x = self.x
        self.sprite.y = self.y
        
        for obj in self.objects:
            if str(type(obj).__name__) == 'Asteroid' and self.collides_with(obj):
                self.die()

    def fire(self):
        missile = Laser(self.game_batch, self.objects,self.x, self.y, self.rotation, self.x_speed, self.y_speed)
        self.objects.append(missile)
