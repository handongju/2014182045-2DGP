from pico2d import *
import random

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#Objects
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,700), 90
        self.frame = random.randint(0,3)
        self.image = load_image('animation_sheet.png')
        self.frame_line=1
        self.speed = random.randint(4,8)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed

        if self.x > 800:
            self.x = 800
            self.speed *= -1
            self.frame_line = 0
        elif self.x < 0:
            self.x = 0
            self.speed *= -1
            self.frame_line = 1


    def draw(self):
        self.image.clip_draw(self.frame *100, self.frame_line * 100, 100, 100, self.x , self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50,750), 599

        self.size = random.randint(0,1)

        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.speed = random.randint(-12,-2)
    def update(self):
        self.y += self.speed

        if self.size==0:
            if self.y <= 61:
                self.y = 61
                self.speed = 0
        elif self.size == 1:
            if self.y <= 71:
                self.y = 71
                self.speed = 0


    def draw(self):
        if self.size==0:
            self.image.clip_draw(0, 0, 21, 21, self.x, self.y)
        elif self.size == 1:
            self.image.clip_draw(0, 0, 41, 41, self.x, self.y)



# initialization code
open_canvas()
boys = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
grass = Grass()

running = True

# game main loop code
while running:
    handle_events()
    clear_canvas()

    for boy in boys:
        boy.update()
        boy.draw()

    for ball in balls:
        ball.update()
        ball.draw()

    grass.draw()
    update_canvas()
    delay(0.05)

close_canvas()

# finalization code