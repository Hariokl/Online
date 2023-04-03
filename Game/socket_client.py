import pygame as pg
import socket


def update():
    data = " ".join(list(map(str, pg.mouse.get_pos()))) + "|"
    print(data)
    s.sendall(data.encode("utf-8"))


WIDTH, HEIGHT = (640, 480)
FPS = 60
display = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3030)) # Подключаемся к нашему серверу.


running = True

while running:
    display.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    update()
    pg.display.flip()
    clock.tick(FPS)

s.close()