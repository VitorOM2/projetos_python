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

velocidade_x = 3 # Variável para controlar a velocidade que a animação vai se mover no eixo X
velocidade_y = 2  # Variável para controlar a velocidade que a animação vai se mover no eixo Y
# ==================== Constantes e Variáveis ====================


# ==================== Instanciação dos widgets ====================

# ===== Canvas =====
canvas = Canvas (tela, width = DIAMETRO, height = TAMANHO)
canvas.pack()

# ===== Imagem =====
foto_imagem        = PhotoImage ( file = 'alien.png' )
foto_imagem_canvas = canvas.create_image (0, 0, image = foto_imagem, anchor = NW)

# ==================== Instanciação dos widgets ====================


foto_imagem_diametro = foto_imagem.width()
foto_imagem_tamanho  = foto_imagem.height()
# ==================== Loop ====================
while True:          # Loop para atualizar a tela durante animação
    coordenadas = canvas.coords ( foto_imagem_canvas )      # Pega as coordenadas da imagem
    print (coordenadas)

    if (coordenadas[0] >= ( DIAMETRO - foto_imagem_diametro ) or coordenadas[0] < 0 ): # Inverte o movimento da imagem se chegar na borda do canvas
        velocidade_x = -velocidade_x
    if (coordenadas[1] >= ( DIAMETRO - foto_imagem_diametro ) or coordenadas[1] < 0 ): # Inverte o movimento da imagem se chegar na borda do canvas
        velocidade_y = -velocidade_y

    canvas.move ( foto_imagem_canvas, velocidade_x, velocidade_y )  #Movimenta a imagem
    tela.update ()                                                  # Atualiza a tela
    time.sleep  (0.01)                                              # Pausa o loop por determinado tempo 
# ==================== Loop ====================


# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================