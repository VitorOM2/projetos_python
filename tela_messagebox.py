# ==================== Importações ====================
from tkinter import *
from tkinter import messagebox
# ==================== Importações ====================


# ==================== Funções ====================
def clique():
    pass
# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_caixa_de_texto = Button(tela,
    command = clique)

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== Botões =====
btn_caixa_de_texto.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ===================