# ==================== Importações ====================
from tkinter import *
from bola    import *
import time

# ==================== Instanciação da Tela ====================
tela = Tk()


# ==================== Constantes e Variáveis ====================
LARGURA = 500
ALTURA  = 500


# ==================== Instanciação dos widgets e objetos ====================

# ===== Canvas =====
canvas = Canvas (tela, width = LARGURA, height = ALTURA)
canvas.pack()

# ===== Bolas (Objetos) =====
bola_volei = Bola(canvas, 0, 0, 100, 1, 1, 'white')


# ==================== Loop ====================
while True: # Loop que cria a animação e atualiza a tela
    bola_volei.mover()
    tela.update()
    time.sleep(0.01)


# ==================== Criar Tela ====================
tela.mainloop()
