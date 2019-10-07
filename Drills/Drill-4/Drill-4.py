from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 1
animation_line = 1


def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * animation_line, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x+= dir*2

    if x >= 800:
        dir = -1
        animation_line = 0
    elif x <= 0:
        dir = 1
        animation_line = 1

    #delay(0.01)

close_canvas()

