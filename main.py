import tkinter
import random


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    # Здесь нужно сделать так, чтобы ушедший
    # "за экран" игрок выходил с другой стороны


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    # Здесь нужно дописать то, что нужно,
    # чтобы все остальные клавиши работалиsss
    check_move()


master = tkinter.Tk()

step = 60
N_X = 10
N_Y = 10
canvas = tkinter.Canvas(master, bg='blue',
                        width=step * N_X, height=step * N_Y)

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
exit_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)

player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step),
                            fill='green')
exit = canvas.create_oval((exit_pos[0], exit_pos[1]),
                          (exit_pos[0] + step, exit_pos[1] + step),
                          fill='yellow')

label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()