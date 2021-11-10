# ==================== Importações ====================
from tkinter import *
import random


# ==================== Funções ====================
def prox_turno():
    pass

def checar_vit():
    pass

def espaco_vazio():
    pass

def novo_jogo():
    pass



# ==================== Instanciação da Tela ====================
tela = Tk()
tela.title ( "Jogo da Velha" )


# ==================== Variáveis e Constantes ====================
jogadores = [ "x", "o" ]
jogador = random.choice ( jogadores )
botoes = [  [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0] ]


# ==================== Instanciação dos widgets ====================
# ===== Labels =====
label = Label ( text = "Turno do " + jogador, font = ( 'consolas', 40 ) )
label.pack    ( side = "top" )

# ===== Frames =====
frame = Frame ( tela )
frame.pack()

# ===== Botões =====
btn_resetar = Button ( text = "Resetar", font = ( 'consolas', 20 ), command = novo_jogo() )
btn_resetar.pack     ( side = "top" )

# Cria os botões para formar o tabuleiro
for row in range (3):
    for column in range (3):
        botoes[row][column] = Button ( frame, text = "", font = ( 'consolas', 40 ), height = 2, width = 5,
                                    command = lambda row = row, column = column: prox_turno(row, column) )

        botoes[row][column].grid (row = row, column = column)


# ==================== Cria Tela ====================
tela.mainloop()