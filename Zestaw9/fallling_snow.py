import pygame
import random
import sys

# inicjalizacja
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Topienie śniegu")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# ustawienia gry
SNOW_RADIUS = 25
SNOW_SPEED = 3
SPAWN_CHANCE = 0.05  # szansa pojawienia się płatka w klatce
MAX_MISSED = 5

snowflakes = []
caught = 0
missed = 0
game_over = False


# pojedynczy płatek śniegu
class Snowflake:
    def __init__(self):
        self.x = random.randint(SNOW_RADIUS, WIDTH - SNOW_RADIUS)
        self.y = -SNOW_RADIUS

    def move(self):
        self.y += SNOW_SPEED

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), SNOW_RADIUS)

    def is_clicked(self, pos):
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return dx * dx + dy * dy <= SNOW_RADIUS * SNOW_RADIUS


# główna pętla
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            for snowflake in snowflakes[:]:
                if snowflake.is_clicked(event.pos):
                    snowflakes.remove(snowflake)
                    caught += 1

    if not game_over:
        # losowe tworzenie płatków
        if random.random() < SPAWN_CHANCE:
            snowflakes.append(Snowflake())

        # ruch płatków
        for snowflake in snowflakes[:]:
            snowflake.move()
            if snowflake.y > HEIGHT:
                snowflakes.remove(snowflake)
                missed += 1
                if missed >= MAX_MISSED:
                    game_over = True

    # rysowanie
    screen.fill(BLACK)

    for snowflake in snowflakes:
        snowflake.draw()

    score_text = font.render(f"Caught: {caught}", True, GREEN)
    missed_text = font.render(f"Missed: {missed}/{MAX_MISSED}", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 50))

    if game_over:
        over_text = font.render("GAME OVER", True, RED)
        screen.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.flip()