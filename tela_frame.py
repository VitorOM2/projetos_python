# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
botao_w = Button(tela,
    text  = 'W',
    font  = ('Consolas', 25),
    width = 3 )

botao_a = Button(tela,
    text  = 'A',
    font  = ('Consolas', 25),
    width = 3 )

botao_s = Button(tela,
    text  = 'S',
    font  = ('Consolas', 25),
    width = 3 )

botao_d = Button(tela,
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

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================