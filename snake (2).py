import pygame, sys, time, random

speed = 6


frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()

if check_errors[1] > 0:
    print("Error" + check_errors[1])
else:
    print("sorun yok knks")

# initialize game window
pygame.display.set_caption("perinay")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fps_controller = pygame.time.Clock()
# one snake square size
square_size = 20


def init_vars():
    global head_pos, snake_body, food_pos, score, direction
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                random.randrange(1, (frame_size_y // square_size)) * square_size]
    score = 0


init_vars()


def show_score(choice, color, font, size):
    score_surface = font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    elif keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    elif keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    elif keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    elif direction == "RIGHT":
        head_pos[0] += square_size

    # check if the snake hits the boundaries
    if head_pos[0] < 0 or head_pos[0] >= frame_size_x or head_pos[1] < 0 or head_pos[1] >= frame_size_y:
        pygame.quit()
        sys.exit()

    # check if the snake hits itself
    for segment in snake_body[1:]:
        if segment == head_pos:
            pygame.quit()
            sys.exit()

    new_head = list(head_pos)
    snake_body.insert(0, new_head)

    # check if the snake eats the food
    if head_pos == food_pos:
        score += 1
        food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                    random.randrange(1, (frame_size_y // square_size)) * square_size]
    else:
        snake_body.pop()

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], square_size, square_size))
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], square_size, square_size))

    show_score(1, white, pygame.font.SysFont('comicsansms', 20), 20)
    pygame.display.update()
    fps_controller.tick(speed)