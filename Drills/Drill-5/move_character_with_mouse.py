from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def move(move_x,move_y):
    global x,y
    global i
    if i<= 100:
        t = i / 100
        x = (1 - t) * x + t * move_x
        y = (1 - t) * y + t * move_y
        i+=1
        print(x,y,i,move_x,move_y)

def handle_events():
    global running
    global move_x, move_y
    global mouse_x, mouse_y
    global i
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                move_x, move_y = event.x, KPU_HEIGHT - 1 - event.y
                i = 0

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
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x,move_y = x,y
i = 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    mouse_pointer.clip_draw(0,0,52,52,mouse_x,mouse_y)
    move(move_x,move_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




