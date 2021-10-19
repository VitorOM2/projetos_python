# ==================== Importações ====================
from tkinter import *
import time
# ==================== Importações ====================


# ==================== Instanciação da Tela ====================
tela = Tk()
# ==================== Instanciação da Tela ====================


# ==================== Constantes e Variáveis ====================
DIAMETRO = 500
TAMANHO  = 500

velocidade_x = 1 # Variável para controlar a velocidade que a animação vai se mover no eixo X
velocidade_y = 1 # Variável para controlar a velocidade que a animação vai se mover no eixo Y
# ==================== Constantes e Variáveis ====================


# ==================== Instanciação dos widgets ====================

# ===== Canvas =====
canvas = Canvas (tela, width = DIAMETRO, height = TAMANHO)
canvas.pack()

# ===== Imagem =====
foto_imagem        = PhotoImage ( file = 'alien.png' )
foto_imagem_canvas = canvas.create_image (0, 0, image = foto_imagem, anchor = NW)

# ==================== Instanciação dos widgets ====================


# ==================== Loop ====================
while True:          # Loop para atualizar a tela durante animação
    coordenadas = canvas.coords ( foto_imagem_canvas )      # Pega as coordenadas da imagem
    print (coordenadas)
    canvas.move (foto_imagem_canvas, velocidade_x, 0)
    tela.update ()                                          # Atualiza a tela
    time.sleep  (0.01)                                      # Pausa o loop por determinado tempo 
# ==================== Loop ====================


# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================