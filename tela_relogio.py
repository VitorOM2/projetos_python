# ==================== Importações ====================
from tkinter import *
from time    import *


# ==================== Instanciação da Tela ====================
tela = Tk()


# ==================== Funções ====================
def update():
    string_tempo = strftime ( '%I:%M:%S %p' )
    rotulo_tempo.config ( text = string_tempo )

    string_dia = strftime ( '%A' )
    rotulo_dia.config ( text = string_dia )

    rotulo_tempo.after (1000, update) # Atualiza a tela com o horário

# ==================== Instanciação dos widgets e objetos ====================

# ===== Labels =====
rotulo_tempo = Label (tela, font = ( 'arial', 25 ), fg = '#00FFFF', bg = "black" )
rotulo_tempo.pack()

rotulo_dia = Label (tela, font = ( 'arial', 25 ) )
rotulo_dia.pack()

update() # Chama uma função para mostrar o horário


# ==================== Criar Tela ====================
tela.mainloop()