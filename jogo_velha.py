# ==================== Importações ====================
from tkinter import *
import random


# ==================== Funções ====================
def prox_turno(row, column):
    
    global jogador

    # Verifica se o lugar escolhido esta vazio
    if botoes [row][column]["text"] == "" and checar_vit() is False:

        if jogador == jogadores[0]:

            botoes[row][column]["text"] = jogador # Coloca o simbolo do jogador no botão

            if checar_vit() is False: # Verifica se não houve vitória após movimento
                jogador = jogadores[1] # Troca de jogador
                label.config ( text = " Turno do " + jogadores[0] )

            elif checar_vit() is True:
                label.config ( text = jogadores[0] + "Venceu!!!" )

            elif checar_vit() == "Empate":
                label.config ( text = "Empate" )
    
    else:
        botoes[row][column]["text"] = jogador # Coloca o simbolo do jogador no botão

        if checar_vit() is False:
            jogador = jogadores[0]
            label.config ( text = " Turno do " + jogadores[0] )

        elif checar_vit() is True:
            label.config ( text = jogadores[1] + "Venceu!!!" )

        elif checar_vit() == "Empate":
            label.config ( text = "Empate" )        

def checar_vit():

    for row in range(3):
        if  botoes[row][0]['text'] == botoes[row][1]['text'] == botoes[row][2]['text'] != "":
            botoes[row][0].config ( bg = "green" )
            botoes[row][1].config ( bg = "green" )
            botoes[row][2].config ( bg = "green" )
            return True

    for row in range(3):
        if  botoes[row][0]['text'] == botoes[row][1]['text'] == botoes[row][2]['text'] != "":
            botoes[row][0].config ( bg ="green" )
            botoes[row][1].config ( bg ="green" )
            botoes[row][2].config ( bg ="green" )
            return True

    if  botoes[0][0]['text'] == botoes[1][1]['text'] == botoes[2][2]['text'] != "":
        botoes[0][0].config ( bg = "green" )
        botoes[1][1].config ( bg = "green" )
        botoes[2][2].config ( bg = "green" )
        return True

    elif botoes[0][2]['text'] == botoes[1][1]['text'] == botoes[2][0]['text'] != "":
         botoes[0][2].config( bg = "green" )
         botoes[1][1].config( bg = "green" )
         botoes[2][0].config( bg = "green" )
         return True

    elif espaco_vazio() is False:
        for row in range(3):
            for column in range(3):
                botoes[row][column].config( bg = "yellow" )
        return "Empate"
    else:
        return False


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