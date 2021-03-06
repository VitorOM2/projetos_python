# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

frame = Frame(tela,
    bg = 'blue',
    bd = 5,
    relief = RAISED)

# ===== Botões =====
botao_w = Button(frame,
    text  = 'W',
    font  = ('Consolas', 25),
    width = 3 )

botao_a = Button(frame,
    text  = 'A',
    font  = ('Consolas', 25),
    width = 3 )

botao_s = Button(frame,
    text  = 'S',
    font  = ('Consolas', 25),
    width = 3 )

botao_d = Button(frame,
    text  = 'D',
    font  = ('Consolas', 25),
    width = 3 )

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Botões =====
botao_w.pack(side = TOP)
botao_a.pack(side = LEFT)
botao_s.pack(side = LEFT)
botao_d.pack(side = LEFT)

# ===== Frame =====
frame.place(x = 10, y = 10)

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================