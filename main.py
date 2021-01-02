import pyglet
import math
from Spaceship import Spaceship
from Settings import WINDOW_HEIGHT, WINDOW_WIDTH
from pyglet import gl
from Laser import Laser
from Asteroid import Asteroid
import random

objects =[]
game_window = pyglet.window.Window(WINDOW_HEIGHT, WINDOW_WIDTH)
batch = pyglet.graphics.Batch()
player = Spaceship(batch, objects)
objects.append(player)

def load_asteroids(n):
    for i in range(0,n):
        if (int(player.x-player.image.width)) < 0:
            x1 = 0
        else:
            x1 = (int(player.x-player.image.width))
        if (int(player.x+player.image.width)) > WINDOW_WIDTH:
            x2 = WINDOW_WIDTH
        else:
            x2 = (int(player.x+player.image.width))
        if int(player.y-player.image.height) < 0:
            y1 = 0
        else:
            y1 = int(player.y-player.image.height)
        if int(player.y+player.image.height)> WINDOW_HEIGHT:
            y2 = WINDOW_HEIGHT
        else:
            y2 = int(player.y+player.image.height)
        x = random.randint(*random.choice([(0, x1), (x2,WINDOW_WIDTH)]))
        y = random.randint(*random.choice([(0, y1), (y2, WINDOW_HEIGHT)]))
        asteroid = Asteroid(batch, objects,x,y)
        objects.append(asteroid)

load_asteroids(5)
game_window.push_handlers(player.key_handler)

@game_window.event
def on_draw():
    game_window.clear()
    for x_offset in (-game_window.width, 0, game_window.width):
        for y_offset in (-game_window.height, 0, game_window.height):
            gl.glPushMatrix()
            gl.glTranslatef(x_offset, y_offset, 0)
            batch.draw()
            gl.glPopMatrix()

        
def update(dt):
    if len(objects) == 1 and str(type(objects[0]).__name__)=='Spaceship':
        load_asteroids(5)
    for obj in objects:
        obj.update(dt)
        if obj.isdead:
            objects.remove(obj)
            obj.sprite.delete()

            if (str(type(obj).__name__)) == 'Spaceship':
                pyglet.app.exit()
                

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
    











