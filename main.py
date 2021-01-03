import pyglet
import math
from Spaceship import Spaceship
from Settings import WINDOW_HEIGHT, WINDOW_WIDTH
from pyglet import gl
from Laser import Laser
from Asteroid import Asteroid
import random
import time

#game_over = False
objects =[]
game_window = pyglet.window.Window(WINDOW_HEIGHT, WINDOW_WIDTH)
batch = pyglet.graphics.Batch()
#GO_batch = pyglet.graphics.Batch()
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

def draw_text(text, x, y, pos_x):
    label = pyglet.text.Label(
        text,
        font_name='League Gothic',
        font_size=36,
        x=x, y=y, anchor_x=pos_x)
    label.draw()

@game_window.event
def on_draw():
    game_window.clear()
    #if game_over == False:
    for x_offset in (-game_window.width, 0, game_window.width):
        for y_offset in (-game_window.height, 0, game_window.height):
            gl.glPushMatrix()
            gl.glTranslatef(x_offset, y_offset, 0)
            batch.draw()
            gl.glPopMatrix()
    """        
    for obj in objects:
        obj.draw_circle(obj.x,obj.y,obj.radius)
    else:
        print('lol')
        draw_text('GAME OVER',WINDOW_WIDTH/2,WINDOW_HEIGHT/2,'left')
        GO_batch.draw()"""

        
def update(dt):

    if len(objects) == 1 and str(type(objects[0]).__name__)=='Spaceship':
        load_asteroids(5)
    for obj in objects:
        obj.update(dt)
        if obj.isdead:
            objects.remove(obj)
            obj.sprite.delete()

            if (str(type(obj).__name__)) == 'Spaceship':
                #game_over = True
                objects.clear()
                time.sleep(3)
                pyglet.app.exit()
                
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
    











