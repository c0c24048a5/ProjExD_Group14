import os
import sys
import pygame as pg
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def title() -> None:

WIDTH = 1200  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ



class RedScreenOfDeath:
    """
    体力に応じて画面端が赤くなる効果を実装するクラス
    """
    def __init__(self, rsod_img: str = "fig/RSOB1.png"):
        """
        画像を読み込む
        引数1 rsod_img : 画像のパス
        """
        self.rsod_img = pg.image.load(rsod_img).convert_alpha() #rsod_imgのアルファ値を利用

    def effect(self, screen: pg.Surface, hp: int) -> None:
        """
        エフェクトを画面に適応する関数
        引数1 screen : 画面Surface
        引数2 hp : こうかとんの体力
        """
        if 1 <= hp <= 3:
            toumeido = 140 - (hp - 1) * 85
            self.rsod_img.set_alpha(toumeido)
            screen.blit(self.rsod_img, (0, 0))
            
class Enemy(pg.sprite.Sprite):
    """
    障害物, 敵に関するクラス
    ランダムの敵画像を表示する(出現範囲も指定)
    """
    imgs = [pg.image.load(f"fig/{i}.png") for i in range(1, 4)] # 画像
    
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.transform.rotozoom(random.choice(__class__.imgs), 0, 1)
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(WIDTH, WIDTH + 200), random.randint(HEIGHT - 300, HEIGHT) 
        self.vx, self.vy = -1, 0 #背景とともに移動

    def update(self) -> None:
        """
        敵を背景とともに左にスクロール
        画面外に出たら削除する
        """
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.right < 0:
            self.kill()


def main() -> None:

    """
    ・背景等が決定次第、タイトルの背景も変更
    ・score表示など出来るようにする
    ・chromedinoの様に開始したら滑らかにプレイ画面に移行するようなものにしたい
    test
    """
    screen = pg.display.set_mode((800, 600))
    title_font = pg.font.Font(None, 80)
    txt = title_font.render("KOUKATON RAN", 
                            True, (255, 255, 255))
    txt2 = title_font.render("START : ENTER", 
                            True, (255, 255, 255))
    text_width = txt.get_width()
    text_height = txt.get_height()
    x_position = (800 - text_width) // 2        #画面中央にタイトルを表示
    y_position = (600 - text_height) // 2
    x_position2 = (800 - text_width) // 2        #画面中央にタイトルを表示
    y_position2 = (900 - text_height) // 2
    screen.blit(txt, (x_position, y_position))  
    screen.blit(txt2, (x_position2, y_position2)) 
    pg.display.update()
    title_end = True
    while title_end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  #enterが押された際、ゲームを開始する。
                    title_end = False  
                    break

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習8
    kk_img = pg.image.load("fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect()#練習10-1
    kk_rct.center = 300, 200#練習10-2
    tmr = 0
    M = kk_rct.move_ip
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        X = tmr%3200 #練習6,9
        
        key_lst = pg.key.get_pressed()#練習10-3
        if key_lst[pg.K_UP]:#練習10-4
            M((-1,-1))
        elif key_lst[pg.K_DOWN]:
            M((-1,1))
        elif key_lst[pg.K_LEFT]:
            M((-1,0))
        elif key_lst[pg.K_RIGHT]:
            M((2,0))
        else: M((-1,0))
        
        screen.blit(bg_img, [-X, 0])
        screen.blit(bg_img2, [-X+1600,0])#練習7,8
        screen.blit(bg_img, [-X+3200,0])#練習9
        screen.blit(kk_img, kk_rct) #練習4,10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5

if __name__ == "__main__":
    pg.init()
    title()
    main()
    pg.quit()
    sys.exit()