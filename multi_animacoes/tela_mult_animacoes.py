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
bola_volei    = Bola (canvas, 0, 0, 80, 1, 1, 'white'  )
bola_tenis    = Bola (canvas, 0, 0, 25 , 5, 3, 'yellow' )
bola_basquete = Bola (canvas, 0, 0, 100, 1, 3, 'red' )

# ==================== Loop ====================
while True: # Loop que cria a animação e atualiza a tela
    bola_volei.mover()
    bola_tenis.mover()
    bola_basquete.mover()
    tela.update()
    time.sleep(0.01)


# ==================== Criar Tela ====================
tela.mainloop()