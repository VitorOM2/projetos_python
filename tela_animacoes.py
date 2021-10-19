# ==================== Importações ====================
from tkinter import *
import time
# ==================== Importações ====================


# ==================== Constantes e Variáveis ====================
DIAMETRO = 500
TAMANHO  = 500
# ==================== Constantes e Variáveis ====================


# ==================== Instanciação da Tela ====================
tela = Tk()
# ==================== Instanciação da Tela ====================


# ==================== Instanciação dos widgets ====================

# ===== Canvas =====
canvas = Canvas (tela, width = DIAMETRO, height = TAMANHO)

# ==================== Instanciação dos widgets ====================


# ==================== Mostrar ====================

# ===== Canvas =====
canvas.pack()

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================