# ==================== Importações ====================
from tkinter import *


# ==================== Funções ====================
def pressionar_teclas(num):
    pass

def resultado():
    pass

def limpar():
    pass


# ==================== Instanciação da Tela ====================
tela = Tk()
tela.geometry ( "500x500"   ) # Tamanho da tela
tela.title    ("Calculadora") # Titulo da tela


# ==================== Constantes e Variáveis ====================
texto_equacao  = ""
rotulo_equacao = StringVar()


# ==================== Instanciação dos widgets ====================
# ===== Labels =====
rotulo_exibicao = Label( # Rotulo para exibir as equações e resultados
    tela, textvariable = rotulo_equacao, font = ('consolas', 20), bg = "white", width = 20, height = 2 )
rotulo_exibicao.pack()


# ==================== Criar a tela ====================
tela.mainloop()