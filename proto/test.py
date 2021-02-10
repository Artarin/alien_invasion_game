import sys
import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((320, 240))
    font = pg.font.Font(None, 30)
    clock = pg.time.Clock()
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        screen.fill(pg.Color('black'))
        fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
        screen.blit(fps, (50, 50))
        pg.display.flip()
        clock.tick(30)

    pg.quit()
    sys.exit()

# if __name__ == "__main__":
#     main()

main()