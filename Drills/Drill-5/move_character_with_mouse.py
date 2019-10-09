from pico2d import *
import math

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def move(move_x,move_y):
    global x,y
    global i
    global animation_line

    global dist
    if dist != 0:
        if i<= dist:
            t = i / dist
            x = (1 - t) * x + t * move_x
            y = (1 - t) * y + t * move_y
            i+=1

        else:
            if animation_line == 1:
                animation_line = 3
            elif animation_line == 0:
                animation_line =2

def handle_events():
    global running
    global x, y
    global move_x, move_y
    global mouse_x, mouse_y
    global i
    global animation_line
    global dist

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                move_x, move_y = event.x, KPU_HEIGHT - 1 - event.y

                dist = math.sqrt((move_x-x)*(move_x-x) + (move_y-y)*(move_y-y))
                dist = int(dist)

                i = 0
                if x<move_x:
                    animation_line = 1
                else:
                    animation_line = 0

        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT -1 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
mouse_pointer = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
mouse_x , mouse_y = 0, 0
animation_line = 1
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x,move_y = x,y
dist = 0
i = 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * animation_line, 100, 100, x, y)
    mouse_pointer.clip_draw(0,0,52,52,mouse_x+26,mouse_y-26)
    move(move_x,move_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    delay(0.01)

close_canvas()




