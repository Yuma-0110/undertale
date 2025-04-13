#!/usr/bin/env python3
# undertale.py
# pyright: reportGeneralTypeIssues=false
import random
import sys

import pygame
import math
from src.constants import *
from src.functions import *

# TODO: 今後使う用↓
# mode = 1  # 0が自分のターン、1が相手のターン


def main() -> None:
    # Pygameの初期化
    pygame.init()
    pygame.display.set_caption("Undertale")
    screen = pygame.display.set_mode((1100, 800))
    clock = pygame.time.Clock()

    # 変数定義
    sans_head_xy: list[float] = [504, 143]
    sans_body_xy: list[float] = [475, 208]
    sans_move_num_x = 0
    sans_move_num_y = 0
    timer = 0
    heart_x: float = 550  # TODO: 本質的にPyGameにおける座標はintのため、floatを加減乗除する処理を見直す
    heart_y: float = 550
    is_jumping = True  # 青ハートがジャンプ中かどうか
    y_moves = []
    is_red_heart_mode = True  # True: 赤ハート, False: 青ハート
    hp = 92
    is_attacking = False  # 攻撃を受けている状態かどうか
    bone_moves = []  # 攻撃を仕掛けてくる bone の攻撃先座標のリスト
    kakudo = 0
    game_mode = 1  # 1ならプレイ中、0ならゲームオーバー
    attack_caution = pygame.image.load(f"{IMAGE_ROOT}/red.jpg")  # 赤長方形
    fight_image = pygame.image.load(f"{IMAGE_ROOT}/fight.png")
    fight2_image = pygame.image.load(f"{IMAGE_ROOT}/fight button 2")
    font1_2 = pygame.font.Font(None, 50)
    press_space = font1_2.render("Press Space To Fight", True, RED, BLACK)
    attack_caution.set_alpha(130)  # 透明度
    is_visible = True
    visible_count = 0
    safe_zone_x = random.randint(250, 745)
    safe_zone_y = random.randint(360, 525)
    safe_zone_flag = True
    sans_attack2_flag = False
    is_damaged3 = False
    is_dameged2 = False
    attack_modes = [False,False,False]
    count = 0
    attack_random = random.randint(0, 2)
    blaster1_x = random.randint(300, 735)
    blaster2_x = random.randint(300, 735)
    blaster3_y = random.randint(360, 565)
    blaster4_y = random.randint(360, 565)
    while blaster1_x - 100 <= blaster2_x <= blaster1_x + 100:
        blaster2_x = random.randint(300, 735)
    while blaster3_y - 100 <= blaster4_y <= blaster3_y + 100:
        blaster4_y = random.randint(360, 565)



    # 実処理
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

        if pressed_key[pygame.K_1] and attack_modes[1] is False and attack_modes[2] is False:
            attack_modes[0] = True
        if pressed_key[pygame.K_2]:
            attack_modes[0] = False
        if pressed_key[pygame.K_3] and attack_modes[0] is False and attack_modes[2] is False:
            attack_modes[1] = True
        if pressed_key[pygame.K_4]:
            attack_modes[1] = False
        if pressed_key[pygame.K_5] and attack_modes[1] is False and attack_modes[0] is False:
            attack_modes[2] = True
        if pressed_key[pygame.K_6]:
            attack_modes[2] = False

        if attack_modes[0] == False and attack_modes[1] == False and attack_modes[2] == False:
            screen.blit(fight_image, (450, 450))
            if 450 <= heart_x <= 610 and 450 <= heart_y <= 511:
                screen.blit(pygame.transform.scale(fight2_image, (160, 61)),(450, 450),)
                screen.blit(press_space, (370, 550))
                if pressed_key[pygame.K_SPACE]:
                    attack_modes[attack_random] = True
                    attack_random = random.randint(0, 2)
                    



        if attack_modes[2]:
            is_damaged3, count = sans_attack3(screen, heart_x, heart_y,blaster1_x,blaster2_x,blaster3_y,blaster4_y,count,)
            if count == 50:
                count = 0
                blaster1_x = random.randint(300, 735)
                blaster2_x = random.randint(300, 735)
                blaster3_y = random.randint(360, 565)
                blaster4_y = random.randint(360, 565)
                while blaster1_x - 100 <= blaster2_x <= blaster1_x + 100:
                    blaster2_x = random.randint(300, 735)
                while blaster3_y - 100 <= blaster4_y <= blaster3_y + 100:
                    blaster4_y = random.randint(360, 565)

            if is_damaged3:
                hp -= 1
                is_damaged3 = False



        # 攻撃の警告処理
        if attack_modes[1]:
            if visible_count <= 72:  # 点滅の間隔x6の値
                if is_visible:
                    screen.blit(attack_caution, (250, 360))

                visible_count += 1
                if visible_count % 12 == 0:  # 点滅の間隔
                    is_visible = not is_visible

                if visible_count == 72:
                    safe_zone_flag = False
                    sans_attack2_flag = True

                if safe_zone_flag:
                    pygame.draw.rect(
                        screen, BLACK, [safe_zone_x, safe_zone_y, 75, 75], 0
                    )

                if sans_attack2_flag:
                    is_dameged2 = sans_attack2(
                        screen, heart_x, heart_y, safe_zone_x, safe_zone_y, is_dameged2
                    )
                    if is_dameged2:
                        hp -= 20
                        is_dameged2 = False
                        sans_attack2_flag = False
                        is_visible = True
                        visible_count = 0
                        safe_zone_flag = True
                        #attack_modes[1] = False
                        safe_zone_x = random.randint(250, 745)
                        safe_zone_y = random.randint(360, 525)
                    else:
                        sans_attack2_flag = False
                        is_visible = True
                        visible_count = 0
                        safe_zone_flag = True
                        #attack_modes[1] = False
                        safe_zone_x = random.randint(250, 745)
                        safe_zone_y = random.randint(360, 525)

        update_constant_view(screen, hp)
        update_sans_view(screen, sans_head_xy, sans_body_xy)
        update_heart_view(screen, heart_x, heart_y, is_red_heart_mode)

        # TODO: Sansの胴体・頭の動きをupdate_sans_view()に吸収する
        sans_body_xy = update_sans_body(
            timer, sans_move_num_x, sans_move_num_y, sans_body_xy
        )
        sans_head_xy = update_sans_head(
            timer, sans_move_num_x, sans_move_num_y, sans_head_xy
        )

        if is_red_heart_mode == 1:  # 赤ハート
            heart_x, heart_y = update_red_heart(heart_x, heart_y)
        else:  # 青ハート
            if is_jumping:
                if y_moves:
                    heart_y = y_moves.pop(0)
                else:
                    is_jumping = False
            else:
                heart_x, heart_y, is_jumping = update_blue_heart(
                    heart_x, heart_y, is_jumping
                )
                if is_jumping:
                    y_moves = jump(heart_y)

        if attack_modes[0]:
            if is_attacking:
                if bone_moves:
                    attack_xy = bone_moves.pop(0)
                    is_dameged1 = update_bone_view(screen, *attack_xy, heart_x, heart_y,kakudo)
                    if is_dameged1:
                        hp -= 9
                        is_attacking = False
                else:
                    is_attacking = False
            else:
                kakudo,bone_moves = generate_bone_view(heart_x, heart_y)
                is_attacking = True

        if hp <= 0:
            game_mode = 0

        if game_mode == 0:
            game_over(screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.display.set_mode((1200, 1000), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))
                if event.key == pygame.K_F3:
                    pygame.quit()
                    sys.exit()

        timer += 1
        pygame.display.update()
        clock.tick(403
                   )


if __name__ == "__main__":
    main()
