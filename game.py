import pygame
import random
import sys

# инициализация Pygame
pygame.init()

# константы игры
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 10
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 10

# создание окна игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# создание таймера для управления частотой кадров
clock = pygame.time.Clock()


# класс для представления змейки
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        x, y = self.body[0]

        if self.direction == "up":
            y -= CELL_SIZE
        elif self.direction == "down":
            y += CELL_SIZE
        elif self.direction == "left":
            x -= CELL_SIZE
        elif self.direction == "right":
            x += CELL_SIZE

        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x, y = self.body[0]

        if self.direction == "up":
            y -= CELL_SIZE
        elif self.direction == "down":
            y += CELL_SIZE
        elif self.direction == "left":
            x -= CELL_SIZE
        elif self.direction == "right":
            x += CELL_SIZE

        self.body.insert(0, (x, y))


# класс для представления еды
class Food:
    def __init__(self):
        self.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE - 1)) * CELL_SIZE
        self.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE - 1)) * CELL_SIZE

    def draw(self):
        pygame.draw.rect(screen, FOOD_COLOR, (self.x, self.y, CELL_SIZE, CELL_SIZE))


def main():
    snake = Snake()
    food = Food()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "down":
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN and snake.direction != "up":
                    snake.direction = "down"
                elif event.key == pygame.K_LEFT and snake.direction != "right":
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT and snake.direction != "left":
                    snake.direction = "right"

        snake.move()

        # проверка столкновения со стенами
        if (
            snake.body[0][0] < 0
            or snake.body[0][0] >= SCREEN_WIDTH
            or snake.body[0][1] < 0
            or snake.body[0][1] >= SCREEN_HEIGHT
        ):
            running = False

        # проверка столкновения с едой
        if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
            snake.grow()
            food = Food()

        # проверка столкновения со своим телом
        for i in range(1, len(snake.body)):
            if snake.body[0][0] == snake.body[i][0] and snake.body[0][1] == snake.body[i][1]:
                running = False

        # очистка экрана
        screen.fill(BACKGROUND_COLOR)

        # рисуем змейку и еду
        for x, y in snake.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (x, y, CELL_SIZE, CELL_SIZE))
        food.draw()

        # обновление экрана
        pygame.display.flip()

        # задержка перед следующим кадром
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
