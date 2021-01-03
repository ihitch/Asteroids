from SpaceObject import SpaceObject
import pyglet
import math
from pyglet import clock

SHOOTING_SPEED = 300
class Laser(SpaceObject):
    def __init__(self, game_batch, objects,ship_x, ship_y, ship_rotation, ship_x_speed, ship_y_speed):
        super(Laser, self).__init__(game_batch=game_batch,game_objects = objects,x=ship_x,y=ship_y, x_speed = ship_x_speed, y_speed = ship_y_speed, rotation = ship_rotation, image = 'Resources/laserRed12.png')
        clock.schedule_once(self.die, 1.8)
    
    def update(self,dt):
        self.x = (self.x + dt * (SHOOTING_SPEED + abs(self.x_speed)) * math.cos(self.rotation)) % 800
        self.y = (self.y + dt * (SHOOTING_SPEED + abs(self.y_speed)) * math.sin(self.rotation)) % 600
        self.sprite.rotation = 90 - math.degrees(self.rotation)
        self.sprite.x = self.x
        self.sprite.y = self.y

        for obj in self.objects:
            if str(type(obj).__name__) == 'Asteroid' and self.collides_with(obj):
                obj.die()
                self.die()