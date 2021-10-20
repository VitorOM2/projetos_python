# ==================== Importações ====================
from tkinter import *
import time

# ==================== Instanciação da Tela ====================
tela = Tk()


# ==================== Constantes e Variáveis ====================
DIAMETRO = 500
ALTURA   = 500


# ==================== Instanciação dos widgets e objetos ====================

# ===== Canvas =====
canvas = Canvas (tela, width = DIAMETRO, height = ALTURA)
canvas.pack()


# ==================== Criar Tela ====================
tela.mainloop()
