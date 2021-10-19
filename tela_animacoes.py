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

# ===== Imagem =====
foto_imagem        = PhotoImage ( file = 'alien.png' )
foto_imagem_canvas = canvas.create_image (0, 0, image = foto_imagem, anchor = NW)

# ==================== Instanciação dos widgets ====================


# ==================== Mostrar ====================

# ===== Canvas =====
canvas.pack()

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================