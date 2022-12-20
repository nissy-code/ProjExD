# アルファベット順にパッケージ読み出し
import pygame as pg
import random
import sys


class Screen():
    def __init__(self, title, wh, img_path):
        # 練習１
        pg.display.set_caption(title)           # "逃げろ！こうかとん"
        self.sfc = pg.display.set_mode(wh)      #(1600, 900)(幅/高さのタプル)
        self.rct = self.rct.get_rect()
        self.bgi_sfc = pg.image.load(img_path)      # "../fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_rect.get_rect()

    def blit(self):
        # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "../fig/pg_bg.jpg")

    # 練習３
    tori_sfc = pg.image.load("../fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    # 練習２
    while True:
        # scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_dct[key]:
                tori_rct.centerx += delta[0]
                tori_rct.centery += delta[1]
            # 練習7
            if check_bound(tori_rct, scrn_rct) != (+1, +1):
                tori_rct.centerx -= delta[0]
                tori_rct.centery -= delta[1]
        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        # 練習８
        if tori_rct.colliderect(bomb_rct):
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()