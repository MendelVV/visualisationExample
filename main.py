import pygame
import const
import time
from circle_actor import CircleActor

pygame.init()#инициировали pygame

#создали экран заданного размера
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Test circles")

#получили объект твчающий за время
clock = pygame.time.Clock()

#инициировали спрайты (рисуемые объекты)
all_sprites = pygame.sprite.Group()

c1 = CircleActor([60, 50], 15, [30,0])
all_sprites.add(c1)
c2 = CircleActor([500, 48], 15,[-25,0])
all_sprites.add(c2)

running = True
t1 = time.time()
while running:
    clock.tick(const.FPS)  # держим частоту кадров не выше

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # обновление
    t2 = time.time()
    dt = (t2-t1)
    all_sprites.update(dt=dt)
    t1 = t2
    # отрисовка
    screen.fill(const.WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()