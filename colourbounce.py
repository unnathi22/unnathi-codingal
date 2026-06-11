import pygame
import random
pygame.init()
pygame.
# 2) Initialize pygame using `pygame.init()`.

# 3) Create two custom event IDs using `pygame.USEREVENT`:
#    a) `SPRITE_COLOR_CHANGE_EVENT` for changing the sprite color.
#    b) `BACKGROUND_COLOR_CHANGE_EVENT` for changing the background color.

# 4) Define color constants using `pygame.Color()`:
#    a) Background colors: BLUE, LIGHTBLUE, DARKBLUE
#    b) Sprite colors: YELLOW, MAGENTA, ORANGE, WHITE

# 5) Create a `Sprite` class that inherits from `pygame.sprite.Sprite`.

# 6) Define the constructor `__init__(self, color, height, width)` for the Sprite:
#    a) Call the parent constructor using `super().__init__()`.
#    b) Create a surface for the sprite using `pygame.Surface([width, height])`.
#    c) Fill the sprite surface with the given `color`.
#    d) Create a rectangle (`self.rect`) for positioning using `self.image.get_rect()`.
#    e) Set an initial velocity with random direction in x and y:
#       `self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]`.

# 7) Define an `update(self)` method to move the sprite and detect boundary hits:
#    a) Move the sprite by its velocity using `self.rect.move_ip(self.velocity)`.
#    b) Set `boundary_hit = False` to track collisions.
#    c) If the sprite touches left/right edges (0 or 500):
#       - reverse x direction (`self.velocity[0] = -self.velocity[0]`)
#       - set `boundary_hit = True`
#    d) If the sprite touches top/bottom edges (0 or 400):
#       - reverse y direction (`self.velocity[1] = -self.velocity[1]`)
#       - set `boundary_hit = True`
#    e) If `boundary_hit` is True, post two events:
#       - `SPRITE_COLOR_CHANGE_EVENT`
#       - `BACKGROUND_COLOR_CHANGE_EVENT`

# 8) Define a method `change_color(self)` in Sprite:
#    a) Fill the sprite surface with a random choice of sprite colors
#       (YELLOW, MAGENTA, ORANGE, WHITE).

# 9) Define a function `change_background_color()`:
#    a) Use `global bg_color` so the background color can be updated.
#    b) Set `bg_color` to a random choice of (BLUE, LIGHTBLUE, DARKBLUE).

# 10) Create a sprite group `all_sprites_list = pygame.sprite.Group()`
#     to store and manage sprites.

# 11) Create one sprite object `sp1 = Sprite(WHITE, 20, 30)`.

# 12) Set the sprite’s starting position randomly:
#     a) `sp1.rect.x` between 0 and 480
#     b) `sp1.rect.y` between 0 and 370

# 13) Add the sprite to the group using `all_sprites_list.add(sp1)`.

# 14) Create the game window (screen) of size 500x400 and set the title.

# 15) Set the initial background color `bg_color = BLUE`
#     and fill the screen once with this color.

# 16) Create a loop control variable `exit = False`
#     and create a `clock` object to control the FPS.

# 17) Start the main game loop `while not exit`:

# 18) Inside the loop, handle events:
#     a) If `pygame.QUIT` occurs, set `exit = True`.
#     b) If `SPRITE_COLOR_CHANGE_EVENT` occurs, call `sp1.change_color()`.
#     c) If `BACKGROUND_COLOR_CHANGE_EVENT` occurs, call `change_background_color()`.

# 19) Update all sprites using `all_sprites_list.update()`.

# 20) Redraw the screen each frame:
#     a) Fill the screen with the current `bg_color`.
#     b) Draw all sprites using `all_sprites_list.draw(screen)`.

# 21) Update the display using `pygame.display.flip()`.

# 22) Limit the frame rate using `clock.tick(240)`.

# 23) When the loop ends, close pygame using `pygame.quit()`.