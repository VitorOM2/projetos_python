# ==================== Importações ====================
from tkinter import *
from tkinter import font


# ==================== Funções ====================
def pressionar(evento):
    rotulo_tecla.config( text = evento.keysym )


# ==================== Instanciação da Tela ====================
tela = Tk()
tela.bind ('<Key>', pressionar)

# ==================== Instanciação dos widgets ====================

# ===== Labels =====
rotulo_tecla = Label(tela, font = ('Consolas', 100) )


# ==================== Mostrar ====================

# ===== Labels =====
rotulo_tecla.pack()

# ===== Tela =====
tela.mainloop()