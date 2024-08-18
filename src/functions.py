#functions.py

# pyright: reportGeneralTypeIssues=false
import random
import math
import pygame
import os
from .constants import *


def update_sans_head(
    timer: int,
    sans_move_num_x: int,
    sans_move_num_y: int,
    sans_head_xy: list[float],
) -> list[float]:
    sans_move_num_x = timer % 48
    if sans_move_num_x < 24:  # 24
        sans_head_xy = [sans_head_xy[0] + 0.15, sans_head_xy[1]]
    elif sans_move_num_x >= 24:  # 24
        sans_head_xy = [sans_head_xy[0] - 0.15, sans_head_xy[1]]

    sans_move_num_y = timer % 48
    if 17 <= sans_move_num_y < 24:  # 7
        sans_head_xy = [sans_head_xy[0], sans_head_xy[1] + 0.15]
    elif 25 <= sans_move_num_y < 32:  # 7
        sans_head_xy = [sans_head_xy[0], sans_head_xy[1] - 0.15]
    elif 0 <= sans_move_num_y < 16:  # 16
        sans_head_xy = [sans_head_xy[0], sans_head_xy[1] - 0.15]
    elif 32 <= sans_move_num_y <= 47:  # 15
        sans_head_xy = [sans_head_xy[0], sans_head_xy[1] + 0.15]

    sans_move_num_y = timer % 32
    if 0 <= sans_move_num_y < 16:
        sans_head_xy = [sans_head_xy[0], sans_head_xy[1] + 0.15]
    elif 16 <= sans_move_num_y <= 31:
        sans_head_xy = [sans_head_xy[0], sans_head_xy[1] - 0.15]

    return sans_head_xy


def update_sans_body(
    timer: int,
    sans_move_num_x: int,
    sans_move_num_y: int,
    sans_body_xy: list[float],
) -> list[float]:
    sans_move_num_x = timer % 48
    if sans_move_num_x < 24:
        sans_body_xy = [sans_body_xy[0] + 0.15, sans_body_xy[1]]
    elif sans_move_num_x >= 24:
        sans_body_xy = [sans_body_xy[0] - 0.15, sans_body_xy[1]]

    sans_move_num_y = timer % 48
    if 16 <= sans_move_num_y < 24:  # 8
        sans_body_xy = [sans_body_xy[0], sans_body_xy[1] + 0.15]
    elif 25 <= sans_move_num_y <= 32:  # 7
        sans_body_xy = [sans_body_xy[0], sans_body_xy[1] - 0.15]
    elif 0 <= sans_move_num_y < 15:  # 15
        sans_body_xy = [sans_body_xy[0], sans_body_xy[1] - 0.15]
    elif 33 <= sans_move_num_y <= 47:  # 14
        sans_body_xy = [sans_body_xy[0], sans_body_xy[1] + 0.15]

    return sans_body_xy


def update_red_heart(heart_x: float, heart_y: float) -> tuple[float, float]:
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


def update_constant_view(screen: pygame.Surface, hp) -> None:
    fight_image = pygame.image.load(f"{IMAGE_ROOT}/fight.png")
    act_image = pygame.image.load(f"{IMAGE_ROOT}/act.png")
    item_image = pygame.image.load(f"{IMAGE_ROOT}/item.png")
    mercy_image = pygame.image.load(f"{IMAGE_ROOT}/mercy.png")

    screen.blit(fight_image, (160, 670))
    screen.blit(act_image, (360, 670))
    screen.blit(item_image, (560, 670))
    screen.blit(mercy_image, (760, 670))

    HP = hp * 2

    # TODO: 完成後にNoneをfonts/内の各フォントに書き換える
    font1 = pygame.font.Font(None, 35)
    font2 = pygame.font.Font(None, 43)
    font3 = pygame.font.Font(None, 30)

    ui1 = font1.render("Frisk", True, WHITE, BLACK)
    ui2 = font2.render("LV 19", True, WHITE, BLACK)
    ui3 = font3.render("HP", True, WHITE, BLACK)
    ui4 = font3.render("KR", True, WHITE, BLACK)
    ui5 = font2.render(f"{hp} / 92", True, WHITE, BLACK)

    screen.blit(ui1, (145, 625))#625
    screen.blit(ui2, (258, 620))
    screen.blit(ui3, (390, 625))
    screen.blit(ui4, (660, 625))
    screen.blit(ui5, (713, 621))

    pygame.draw.rect(screen, WHITE, [250, 360, 570, 240], 2)  # ハートが動き回る枠
    pygame.draw.rect(screen, RED, [450, 620, 184, 27], 0)  # HPゲージ(赤)
    pygame.draw.rect(screen, YELLOW, [450, 620, HP, 27], 0)  # HPゲージ(黄色)


def update_sans_view(screen: pygame.Surface, sans_head_point, sans_body_point) -> None:
    sans_head_image = pygame.image.load(f"{IMAGE_ROOT}/sans_head.png")
    sans_body_image = pygame.image.load(f"{IMAGE_ROOT}/sans_body.png")
    sans_legs_image = pygame.image.load(f"{IMAGE_ROOT}/sans_legs.png")

    screen.blit(sans_legs_image, (485, 275))
    screen.blit(sans_body_image, sans_body_point)
    screen.blit(sans_head_image, sans_head_point)
    pass


def update_heart_view(
    screen: pygame.Surface, heart_x: int, heart_y: int, is_red_heart_mode
) -> None:
    heart_red = pygame.image.load(f"{IMAGE_ROOT}/heart_red.png")
    heart_blue = pygame.image.load(f"{IMAGE_ROOT}/heart_blue.png")

    if is_red_heart_mode:
        screen.blit(heart_red, (heart_x, heart_y))
    else:
        screen.blit(heart_blue, (heart_x, heart_y))


def jump(heart_y):
    half_moves = [-50, -35, -25, -13, -10, -8, -7]
    relative_moves = half_moves + [0] + [abs(x) for x in reversed(half_moves)]
    moves = []
    cur = heart_y
    for move in relative_moves:
        cur += move
        moves.append(cur)
    return moves


def update_blue_heart(
    heart_x: float, heart_y: float, is_jumping: bool
) -> tuple[float, float, bool]:
    pressed_key = pygame.key.get_pressed()

    tmr = 0
    # 更新
    if heart_y <= Y_GROUND:  # 地面についたら
        heart_y = Y_GROUND
        tmr += 1
    elif heart_y > Y_GROUND:
        is_jumping = False

    if pressed_key[pygame.K_UP]:
        is_jumping = True
        heart_x, heart_y, is_jumping

    if pressed_key[pygame.K_RIGHT]:
        speed = 10
        if pressed_key[pygame.K_RSHIFT] or pressed_key[pygame.K_LSHIFT]:
            speed = 6

        if heart_x >= 800:
            speed = 0
        heart_x += speed

    if pressed_key[pygame.K_LEFT]:
        speed = 10
        if pressed_key[pygame.K_RSHIFT] or pressed_key[pygame.K_LSHIFT]:
            speed = 6

        if heart_x <= 250:
            speed = 0

        heart_x -= speed

    return heart_x, heart_y, is_jumping


def generate_bone_view(heart_x, heart_y):
    while True:
        sans_attack_X = random.randint(250, 820)
        sans_attack_Y = random.randint(360, 600)
        if (sans_attack_X < heart_x - 90 or sans_attack_X > heart_x + 90) and \
           (sans_attack_Y < heart_y - 60 or sans_attack_Y > heart_y + 60):
            break

    # 目標までの直線距離と角度を計算
    delta_x = heart_x - sans_attack_X
    delta_y = heart_y - sans_attack_Y
    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
    if distance == 0:
        distance = 1  # Avoid division by zero

    # 角度の計算
    angle = math.degrees(math.atan2(delta_y, delta_x))  # atan2 is used for better angle calculation
    if angle < 0:
        angle += 360

    # 骨の移動速度
    speed = 7
    sans_attack_x_movespeed = (delta_x / distance) * speed
    sans_attack_y_movespeed = (delta_y / distance) * speed

    # 移動パスを生成
    sans_attack_path = []
    while 250 < sans_attack_X < 820 and 360 < sans_attack_Y < 600:
        sans_attack_X += sans_attack_x_movespeed
        sans_attack_Y += sans_attack_y_movespeed
        sans_attack_path.append((sans_attack_X, sans_attack_Y))

    return(angle,sans_attack_path)
    """sans_attack_X = 0
    sans_attack_Y = 0
    katamuki = 0
    sans_attack_path = []
    kakudo = 0
    tan = 0
    while True:
        sans_attack_X = random.randint(250, 820)
        sans_attack_Y = random.randint(360, 600)
        if sans_attack_X < heart_x - 90 or sans_attack_X > heart_x + 90 and sans_attack_Y < heart_y - 60 or sans_attack_Y > heart_y + 60:
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

    if sans_attack_X > heart_x and sans_attack_Y < heart_y:
        tan = (heart_y - sans_attack_Y) / (sans_attack_X - heart_x)
        kakudo = math.degrees(math.atan(tan))#tanは+/+で+、tan式は(b-y/x-a)、角度は270-tanθ
        kakudo = 270 - round(kakudo)

    if sans_attack_X < heart_x and sans_attack_Y > heart_y:
        tan = (heart_y - sans_attack_Y) / (sans_attack_X - heart_x)
        kakudo = math.degrees(math.atan(tan))#tanは-/-で+、tan式は(b-y/x-a)、角度は90-tanθ
        kakudo = 90 - round(kakudo)


    if sans_attack_X > heart_x and sans_attack_Y > heart_y:
        tan = (heart_x - sans_attack_X) / (heart_y - sans_attack_Y)
        kakudo = math.degrees(math.atan(tan))#tanは-/-で+、tan式は(a-x/b-y)、角度は360-tanθ
        kakudo = 360 - round(kakudo)


    if sans_attack_X < heart_x and sans_attack_Y < heart_y:
        tan = (heart_x - sans_attack_X) / (heart_y - sans_attack_Y)
        kakudo = math.degrees(math.atan(tan))#tanは+/+で+、tan式は(a-x/b-y)、角度は180-tanθ
        kakudo = 180 - round(kakudo)
    
    return kakudo,sans_attack_path"""


def update_bone_view(
    screen: pygame.Surface, sans_attack_X, sans_attack_Y, heart_x, heart_y, kakudo
):
    is_dameged1 = 0  # ０ならダメージ食らわない1ならくらくらう
    attack_knifebone_image = pygame.image.load(os.path.join(IMAGE_ROOT, "attack_knifebone.png"))

    # 画像を回転させる
    rotated_image = pygame.transform.rotate(attack_knifebone_image, kakudo)
    rotated_rect = rotated_image.get_rect(center=(sans_attack_X, sans_attack_Y))

    # 回転した画像をスクリーンに描画
    screen.blit(rotated_image, rotated_rect.topleft)

    # ダメージ判定
    if (
        sans_attack_X - 6 <= heart_x <= sans_attack_X + 6
        and sans_attack_Y - 18 <= heart_y <= sans_attack_Y + 60
    ):
        is_dameged1 = 1

    return is_dameged1
    """is_dameged1 = 0  # ０ならダメージ食らわない1ならくらくらう
    pygame.image.load(f"{IMAGE_ROOT}/attack_singlebone.png")
    pygame.image.load(f"{IMAGE_ROOT}/attack_bluebone.png")
    pygame.image.load(f"{IMAGE_ROOT}/attack_orangebone.png")
    attack_knifebone_image = pygame.image.load(f"{IMAGE_ROOT}/attack_knifebone.png")

    rotated_image = pygame.transform.rotate(attack_knifebone_image, kakudo)
    screen.blit(rotated_image, (sans_attack_X, sans_attack_Y))
    if (
        sans_attack_X - 6 <= heart_x <= sans_attack_X + 6
        and sans_attack_Y - 18 <= heart_y <= sans_attack_Y + 60
    ):
        is_dameged1 = 1

    return is_dameged1"""


def sans_attack2(screen: pygame.Surface, heart_x, heart_y, safe_zone_x, safe_zone_y, is_dameged2):
    pygame.draw.rect(screen, WHITE, [250, 360, 570, 240], 0)
    pygame.draw.rect(screen, BLACK, [safe_zone_x, safe_zone_y, 75, 75], 0)
    if (
        safe_zone_x <= heart_x <= safe_zone_x + 75
        and safe_zone_y <= heart_y <= safe_zone_y + 75
    ):
        pass
    else:
        is_dameged2 = True

    return is_dameged2

def sans_attack3(screen: pygame.Surface, heart_x, heart_y, blaster1_x,blaster2_x,blaster3_y,blaster4_y,count=0,) -> tuple: #(bool, int)
    blaster1_x_damage = False
    blaster2_x_damage = False
    blaster3_y_damage = False
    blaster4_y_damage = False
    if 1 <= count <= 45:
        gasterblaster_image = pygame.image.load(f"{IMAGE_ROOT}/attack_gasterblaster3.jpeg")
        gasterblaster_left_image = pygame.image.load(
            f"{IMAGE_ROOT}/attack_gasterblaster_left.png"
        )
        gasterblaster_right_image = pygame.image.load(
            f"{IMAGE_ROOT}/attack_gasterblaster_right.png"
        )
        screen.blit(
            pygame.transform.scale(gasterblaster_image, (130, 127)), (blaster1_x - 48, 265)
        )  # 上から
            
        screen.blit(
            pygame.transform.scale(gasterblaster_image, (130, 127)), (blaster2_x - 48, 265)
        )  # 上から

        screen.blit(
            pygame.transform.scale(gasterblaster_right_image, (130, 127)),
            (160, blaster3_y - 46),
        )  # 左から

        screen.blit(
            pygame.transform.scale(gasterblaster_left_image, (130, 127)),
            (785, blaster4_y - 46),
        )  # 右から

    if 35 <= count <= 45:
        pygame.draw.rect(screen, WHITE, [blaster1_x, 360, 35, 240], 0)  # 上から
        pygame.draw.rect(screen, WHITE, [blaster2_x, 360, 35, 240], 0)  # 上からその2
        pygame.draw.rect(screen, WHITE, [250, blaster3_y, 570, 35], 0)  # 左から
        pygame.draw.rect(screen, WHITE, [250, blaster4_y, 570, 35], 0)  # 右から

        blaster1_x_damage = (
            blaster1_x <= heart_x <= blaster1_x + 35 and 360 <= heart_y <= 600
        )
        blaster2_x_damage = (
            blaster2_x <= heart_x <= blaster2_x + 35 and 360 <= heart_y <= 600
        )
        blaster3_y_damage = (
            250 <= heart_x <= 820 and blaster3_y <= heart_y <= blaster3_y + 35
        )
        blaster4_y_damage = (
            250 <= heart_x <= 820 and blaster4_y <= heart_y <= blaster4_y + 35
        )

    is_damaged3 = [
        blaster1_x_damage,
        blaster2_x_damage,
        blaster3_y_damage,
        blaster4_y_damage,
    ]
    
    return any(is_damaged3), count+1


def game_over(screen):
    font1 = pygame.font.Font(None, 85)
    gameover_txt = font1.render("Press F3 to End the Game", True, WHITE, BLACK)
    gameover_image = pygame.image.load(f"{IMAGE_ROOT}/game_over.png")
    screen.blit(pygame.transform.scale(gameover_image, (1100, 800)), (0, 0))
    screen.blit(gameover_txt, (210, 680))
