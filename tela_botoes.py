# ==================== Importações ====================
from tkinter import *
from tkinter import font
# ==================== Importações ====================


# ==================== Variáveis ====================
contador = 0
# ==================== Variáveis ====================



# ==================== Funções ====================
def clique():
    global contador
    contador += 1
    if contador == 1:
        print ( 'Você clicou {} vez'.format (contador) )
    else:
        print ( 'Você clicou {} vezes'.format (contador) )
# ==================== Funções ====================


# ==================== Instanciação ====================
tela  = Tk()
botao = Button(tela,
            text    = " Clique aqui ",
            command = clique,
            font    = ( "Times New Roman", 30 ),
            fg      = "#00FF00",
            bg      = "black",
            activeforeground = "#00FF00",
            activebackground = "black",
            state = ACTIVE )
# ==================== Instanciação ====================


# ==================== Mostrar ====================
botao.pack()
tela.mainloop()
# ==================== Mostrar ====================
