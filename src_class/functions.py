#functions.py

# pyright: reportGeneralTypeIssues=false
import random
import math
import pygame
import os
from .constants import *

class Frisk:

    def __init__(self, hp):

        self.fight_image = pygame.image.load(f"{IMAGE_ROOT}/fight.png")
        self.act_image = pygame.image.load(f"{IMAGE_ROOT}/act.png")
        self.item_image = pygame.image.load(f"{IMAGE_ROOT}/item.png")
        self.mercy_image = pygame.image.load(f"{IMAGE_ROOT}/mercy.png")

        font1 = pygame.font.Font("./fonts/DeterminationMonoWebRegular-Z5oq.ttf", 35)
        font2 = pygame.font.Font("./fonts/DeterminationMonoWebRegular-Z5oq.ttf", 43)
        font3 = pygame.font.Font("./fonts/DeterminationMonoWebRegular-Z5oq.ttf", 30)

        self.ui1 = font1.render("Frisk", True, WHITE, BLACK)
        self.ui2 = font2.render("LV 19", True, WHITE, BLACK)
        self.ui3 = font3.render("HP", True, WHITE, BLACK)
        self.ui4 = font3.render("KR", True, WHITE, BLACK)
        self.ui5 = font2.render(f"{hp} / 92", True, WHITE, BLACK)

        self.HP = hp * 2


    def update_red_heart(self, heart_x: float, heart_y: float) -> tuple[float, float]:
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP]:
            speed = 6
            if pressed_key[pygame.K_RSHIFT] or pressed_key[pygame.K_LSHIFT]:
                speed = 4

            if heart_y <= 365:
                speed = 0
            heart_y -= speed

        if pressed_key[pygame.K_DOWN]:
            speed = 6
            if pressed_key[pygame.K_RSHIFT] or pressed_key[pygame.K_LSHIFT]:
                speed = 4

            if heart_y >= 580:
                speed = 0
            heart_y += speed

        if pressed_key[pygame.K_RIGHT]:
            speed = 6
            if pressed_key[pygame.K_RSHIFT] or pressed_key[pygame.K_LSHIFT]:
                speed = 4

            if heart_x >= 800:
                speed = 0
            heart_x += speed

        if pressed_key[pygame.K_LEFT]:
            speed = 6
            if pressed_key[pygame.K_RSHIFT] or pressed_key[pygame.K_LSHIFT]:
                speed = 4

            if heart_x <= 250:
                speed = 0

            heart_x -= speed

        return heart_x, heart_y
    

    def update_heart_view(
        self, screen: pygame.Surface, heart_x: int, heart_y: int, is_red_heart_mode
    ) -> None:
        heart_red = pygame.image.load(f"{IMAGE_ROOT}/heart_red.png")
        heart_blue = pygame.image.load(f"{IMAGE_ROOT}/heart_blue.png")

        if is_red_heart_mode:
            screen.blit(heart_red, (heart_x, heart_y))
        else:
            screen.blit(heart_blue, (heart_x, heart_y))


    def constants_view(self,screen):

        screen.blit(self.fight_image, (160, 670))
        screen.blit(self.act_image, (360, 670))
        screen.blit(self.item_image, (560, 670))
        screen.blit(self.mercy_image, (760, 670))

        screen.blit(self.ui1, (145, 625))
        screen.blit(self.ui2, (258, 620))
        screen.blit(self.ui3, (390, 625))
        screen.blit(self.ui4, (660, 625))
        screen.blit(self.ui5, (713, 621))

        pygame.draw.rect(screen, WHITE, [250, 360, 570, 240], 2)  # ハートが動き回る枠
        pygame.draw.rect(screen, RED, [450, 620, 184, 27], 0)  # HPゲージ(赤)
        pygame.draw.rect(screen, YELLOW, [450, 620, self.HP, 27], 0)  # HPゲージ(黄色)


class enemy_A:

    def update_enemy_A_move(self):
        pass

    def update_sans_view(self,screen: pygame.Surface):
        pass

    def enemy_A_attack(self,screen, heart_x, heart_y,attack_mode):

        if attack_mode == 0:
            pass

        else:
            right_irror_x_list = []
            left_mirror_y_list = []
            right_mirror_attack_X = 0
            right_mirror_attack_Y = 0
            left_mirror_attack_X = 0
            left_mirror_attack_Y = 0
            katamuki = 0
            sans_attack_path = []

            while True:
                mirror_attack_X
                mirror_attack_Y
                if mirror_attack_X < heart_x - 90 or mirror_attack_X > heart_x + 90 and sans_attack_Y < heart_y - 60 or sans_attack_Y > heart_y + 60:
                    break
            # この33は何フレームかけて進むかってこと(1フレーム30ミリ秒)
            #sans_attack_x_movespeed = max(abs(heart_x - sans_attack_X) // 33, 4)
            #sans_attack_y_movespeed = max(abs(heart_y - sans_attack_Y) // 33, 4)

            katamuki = abs((heart_y - sans_attack_Y)/(heart_x - sans_attack_X))

            sans_attack_x_movespeed = 5
            sans_attack_y_movespeed = katamuki*5

            if sans_attack_X > heart_x:
                sans_attack_x_movespeed *= -1
            elif sans_attack_Y > heart_y:
                sans_attack_y_movespeed *= -1

            while 250 < sans_attack_X < 820 and 360 < sans_attack_Y < 600:
                sans_attack_X += sans_attack_x_movespeed
                sans_attack_Y += sans_attack_y_movespeed
                sans_attack_path += [(sans_attack_X, sans_attack_Y)]
