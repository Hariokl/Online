import pygame as pg
import socket


def update():
    global pos
    data = conn.recv(1024)  # Получаем данные из сокета.
    message = data.decode('utf-8').split("|")[0].split()
    if message == "":
        return
    pos = tuple(map(int, message))
    print(pos)


WIDTH, HEIGHT = (640, 480)
FPS = 60
display = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 3030))  # Привязываем серверный сокет к localhost и 3030 порту.
s.listen(0)  # Начинаем прослушивать входящие соединения.
conn, addr = s.accept()  # Метод который принимает входящее соединение.

running = True
pos = WIDTH // 2, HEIGHT // 2

while running:
    display.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    update()
    pg.draw.circle(display, (250, 250, 250), pos, 20, 0)
    pg.display.flip()
    clock.tick(FPS)

s.close()