# ==================== Importações ====================
from tkinter import *
from bola    import *
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

# ===== Bolas (Objetos) =====
bola_volei = Bola(canvas, 0, 0, 100, 1, 1, 'white')


# ==================== Criar Tela ====================
tela.mainloop()
