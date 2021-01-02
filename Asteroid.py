from SpaceObject import SpaceObject
import math
from random import uniform

_ROTATION_SPEED = 0.3
ACCELERATION = 3000
class Asteroid(SpaceObject):
    def __init__(self,batch,g_objects = None,xA=0,yA=0):
        super(Asteroid, self).__init__(game_batch=batch, game_objects=g_objects,x=xA,y=yA, x_speed = 0, y_speed = 0, rotation = 0, image = 'meteorGrey_big1.png')
        self.dtc = 0

    def update(self, dt):
        self.dtc += dt
        rot = 0
        if self.dtc >= 1:
            rot = uniform(-100,100)
            self.dtc = 0
        self.rotation = self.rotation + dt * rot
        self.x_speed = dt * ACCELERATION * math.cos(self.rotation)
        self.y_speed = dt * ACCELERATION * math.sin(self.rotation)
        self.x = (self.x + dt * self.x_speed) % 800
        self.y = (self.y + dt * self.y_speed) % 600
        self.sprite.rotation = 90 - math.degrees(self.rotation)
        self.sprite.x = self.x
        self.sprite.y = self.y