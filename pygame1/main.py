import pygame
successes, failures = pygame.init()


def start_sound():

    # start background sound
    file = 'background.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(0.2)          # 1 is max volume
    pygame.mixer.music.play(-1)                 # -1 loop comtinuosuly

# end def

# game scfreen sizing
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

# game refresh in animation frames per second
FPS = 60

# main colours - use RGB system
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Circle(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, x_pos, y_pos, radius):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.colour = colour
        self.radius = radius
        self.position = [x_pos,y_pos]

    def draw(self, screen):

        pygame.draw.circle(screen, self.colour, self.position, CIRCLE_SIZE, width=0)
        self.rect = self.image.get_rect()

# endclass


# text title
fontObj = pygame.font.Font('freesansbold.ttf', 32)
title = fontObj.render('Hello World!', True, GREEN, BLUE)
title_rect = title.get_rect()
title_rect.center = (340, 50)

# initial objects positioning and sizing
initial_x = SCREEN_WIDTH/2
initial_y = SCREEN_HEIGHT/2
RECTANGLE_SIZE = (180, 80)
CIRCLE_SIZE = 50
rect_position_and_size = ( initial_x, initial_y) + RECTANGLE_SIZE
circle_position = [initial_x, initial_y]

# setup game
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption('Sausages')

rectangle_drag = False
circle_drag = False

# start_sound()

while True:

    clock.tick(FPS)

    # process key and mouse events - its a stack, each time an event is processed it's removed from the stack
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse button down", rectangle_drag, circle_drag)

            if event.button == 1:   # lmb

                mouse_x, mouse_y = event.pos

                if rectangle.collidepoint(event.pos):

                    print("rectangle",rectangle.x)
                    rectangle_drag = True
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

                elif circle.collidepoint(event.pos):

                    print("circle", circle.x)
                    circle_drag = True
                    offset_x = circle.x - mouse_x
                    offset_y = circle.y - mouse_y
                else:
                    print("Other collision woith mouse")
                # end if

        elif event.type == pygame.MOUSEBUTTONUP:

            print("mouse button up", rectangle_drag, circle_drag)

            if event.button == 1:   # lmb

                if rectangle_drag:
                    rectangle_drag = False
                if circle_drag:
                    circle_drag = False

        elif event.type == pygame.MOUSEMOTION:  # handel mouse movement

            print("mouse move/drag", rectangle_drag, circle_drag)

            if rectangle_drag:

                mouse_x, mouse_y = event.pos
                rx = mouse_x + offset_x
                ry = mouse_y + offset_y
                rect_position_and_size = (rx, ry) + RECTANGLE_SIZE

            elif circle_drag:

                mouse_x, mouse_y = event.pos
                cx = mouse_x + offset_x
                cy = mouse_y + offset_y
                circle_position = [cx + CIRCLE_SIZE, cy + CIRCLE_SIZE]

            else:

                print("Not sure")

            # end if

        elif event.type == pygame.KEYDOWN:      # handle key press

            print("Key's not being tracked")
            '''
            if event.key == pygame.K_UP:
                rectangle.move_ip(0, -4)
            elif event.key == pygame.K_DOWN:
                rectangle.move_ip(0, 4)
            elif event.key == pygame.K_LEFT:
                rectangle.move_ip(-4, 0)
            elif event.key == pygame.K_RIGHT:
                rectangle.move_ip(4, 0)
            '''
        # endif

    # end for

    screen.fill(BLUE)

    circle = pygame.draw.circle(screen, GREEN, circle_position, CIRCLE_SIZE, width=0)
    rectangle = pygame.draw.rect(screen, RED, rect_position_and_size, width=0)
    screen.blit(title, title_rect)

    pygame.display.update()

# end while - game loop
