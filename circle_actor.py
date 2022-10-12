import pygame
import const


class CircleActor(pygame.sprite.Sprite):

    def __init__(self, pos, r, v):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.radius = r
        self.velocity = v
        self.pos = pos
        self.image = pygame.Surface((2*r, 2*r),pygame.SRCALPHA)
        pygame.draw.circle(self.image, const.COLOR_P, (r,r), r)

        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

    def update(self, dt):
        #dt время в секундах от последнего обновления
        self.pos[0]+=self.velocity[0]*dt
        self.pos[1]+=self.velocity[1]*dt
        self.rect.center = tuple(self.pos)