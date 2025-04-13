#!/usr/bin/env python3
# undertale.py
# pyright: reportGeneralTypeIssues=false
import random
import sys

import pygame
import math
from src_class.constants import *
from src_class.functions import *

# TODO: 今後使う用↓
# mode = 1  # 0が自分のターン、1が相手のターン


def main() -> None:
    # Pygameの初期化
    pygame.init()
    pygame.display.set_caption("Undertale")
    screen = pygame.display.set_mode((1100, 800))
    clock = pygame.time.Clock()

    game_mode = 1
    # TODO: 本質的にPyGameにおける座標はintのため、floatを加減乗除する処理を見直す
    heart_x: float = 550
    heart_y: float = 550

    frisk = Frisk(92)

    while True:

        if game_mode == 1:
            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_q] and (
                pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_RCTRL]
            ):  # Ctrl+Qが押されたら終了する
                return

            if pressed_key[pygame.K_z] and is_red_heart_mode:  # 青ハートに変更する
                is_red_heart_mode = False
                heart_y = 580
            elif pressed_key[pygame.K_q] and not is_red_heart_mode:  # 赤ハートに変更する
                is_red_heart_mode = True
                heart_y = 550

            # 描写処理
            screen.fill(BLACK)

        if pressed_key[pygame.K_1]:
            enemy_A.enemy_A_attack(screen,heart_x,heart_y)

        if pressed_key[pygame.K_2]:
            enemy_A.enemy_A_attack(screen,heart_x,heart_y,attack_mode)

        heart_x, heart_y = frisk.update_red_heart(heart_x, heart_y)
        frisk.update_heart_view(screen, heart_x, heart_y, 1)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.display.set_mode((1200, 1000), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))
                if event.key == pygame.K_F3:
                    pygame.quit()
                    sys.exit()

        frisk.constants_view(screen)
        pygame.display.update()
        clock.tick(403)


if __name__ == "__main__":
    main()
