"""constants.py
ゲーム内で使用する定数を定義する
"""
from pathlib import Path

# プロジェクト用定数
APP_ROOT = Path(__file__).parent.parent
IMAGE_ROOT = f"{APP_ROOT}/images"
FONT_ROOT = f"{APP_ROOT}/fonts"

# ゲーム内定数
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

Y_GROUND = 580  # 地面に相当する下枠のY座標
