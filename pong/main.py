# code library that allows us to make and run games
import pygame

# code library that allows us to read well-organised data
import json
from readjsonfile import get_constants_data


class Paddle:

    def __init__(self, x, y, width, height, colour, paddle_veloctiy):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.velocity = paddle_veloctiy

    def draw(self, win):
        pygame.draw.rect(
            win, self.colour, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:

    def __init__(self, x, y, radius, ball_velocity, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = ball_velocity
        self.y_vel = 0
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def draw(win, paddles, ball, left_score, right_score):

    win.fill(WINDOW_COLOUR)

    left_score_text = SCORE_FONT.render(f"{left_score}", True, RED)
    right_score_text = SCORE_FONT.render(f"{right_score}", True, BLACK)

    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) -right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(win)
    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):

    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:

        if (ball.y >= left_paddle.y) and (ball.y <= (left_paddle.y + left_paddle.height)):
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / BALL_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:

        if (ball.y >= right_paddle.y) and (ball.y <= (right_paddle.y + right_paddle.height)):
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / BALL_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_paddle_movement(keys, left_paddle, right_paddle):

    if keys[pygame.K_w] and left_paddle.y - PADDLE_VELOCITY >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + PADDLE_VELOCITY + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - PADDLE_VELOCITY >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + PADDLE_VELOCITY + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


data = get_constants_data()

WIDTH = data["constants"]["width"]
HEIGHT = data["constants"]["height"]

FPS = data["constants"]["fps"]
WHITE = data["constants"]["white"]
BLACK = data["constants"]["black"]
BLUE = data["constants"]["blue"]
GREEN = data["constants"]["green"]
RED = data["constants"]["red"]

PADDLE_WIDTH = data["constants"]["paddle_width"]
PADDLE_HEIGHT = data["constants"]["paddle_height"]
PADDLE_VELOCITY = data["constants"]["paddle_velocity"]

BALL_RADIUS = data["constants"]["ball_radius"]
BALL_VELOCITY = data["constants"]["ball_velocity"]

WINNING_SCORE = data["constants"]["winning_score"]
SCORE_FONT_NAME = data["constants"]["score_font_name"]
SCORE_FONT_SIZE = data["constants"]["score_font_size"]

WINDOW_COLOUR = BLUE


# main program starts here
def main():

    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT, GREEN, PADDLE_VELOCITY)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, RED, PADDLE_VELOCITY)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_VELOCITY, GREEN)

    left_score = 0
    right_score = 0

    run = True
    while run:

        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        print(left_score,right_score)
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            text = SCORE_FONT.render(win_text, True, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    SCORE_FONT = pygame.font.SysFont(SCORE_FONT_NAME, SCORE_FONT_SIZE)
    pygame.display.set_caption("Pong")
    main()
