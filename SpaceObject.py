import pyglet
from Settings import WINDOW_HEIGHT, WINDOW_WIDTH
import math
from pyglet import gl

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

    def distance(self,point_1=(0, 0), point_2=(0, 0)):
        return math.sqrt(
            (point_1[0] - point_2[0]) ** 2 +
            (point_1[1] - point_2[1]) ** 2)

    def collides_with(self, other):
        collision_distance = (self.radius) + (other.radius)
        actual_distance = self.distance((self.x,self.y), (other.x,other.y))

        return actual_distance <= collision_distance

    def draw_circle(self,x, y, radius):
        iterations = 20
        s = math.sin(2*math.pi / iterations)
        c = math.cos(2*math.pi / iterations)

        dx, dy = radius, 0

        gl.glBegin(gl.GL_LINE_STRIP)
        for i in range(iterations+1):
            gl.glVertex2f(x+dx, y+dy)
            dx, dy = (dx*c - dy*s), (dy*c + dx*s)
        gl.glEnd()


    