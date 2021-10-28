# ==================== Importações ====================
from tkinter import *


# ==================== Funções ====================
def pressionar_teclas( num ):

    # Mostra as teclas pressionadas na tela
    global texto_equacao

    texto_equacao = texto_equacao + str ( num )
    rotulo_equacao.set ( texto_equacao )

def operacoes():
    
    try:
        # Calcula o resultado
        global texto_equacao

        total = str (   eval (  texto_equacao  )   ) # O Eval() calcula o resultado
        rotulo_equacao.set   (    total    )

        texto_equacao = total

    except ZeroDivisionError:

        rotulo_equacao.set (    "Erro: Impossível dividir por zero"    )

        texto_equacao = ""

    except SyntaxError:

        rotulo_equacao.set (    "Erro: erro de sintaxe"    )

        texto_equacao = ""    
    

def limpar():
    
    # Limpa a tela
    global texto_equacao

    rotulo_equacao.set ("")

    texto_equacao = ""


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
    tela, textvariable = rotulo_equacao, font = ('consolas', 20), bg = "white", width = 40, height = 2 )
rotulo_exibicao.pack()

# ===== Frame =====
frame = Frame ( tela )
frame.pack()

# ===== Botões =====
btn1 = Button ( frame, text = 1, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (1) )
btn1.grid ( row = 0, column = 0 )

btn2 = Button ( frame, text = 2, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (2) )
btn2.grid ( row = 0, column = 1 )

btn3 = Button ( frame, text = 3, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (3) )
btn3.grid ( row = 0, column = 2 )

btn4 = Button ( frame, text = 4, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (4) )
btn4.grid ( row = 1, column = 0 )

btn5 = Button ( frame, text = 5, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (5) )
btn5.grid ( row = 1, column = 1 )

btn6 = Button ( frame, text = 6, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (6) )
btn6.grid ( row = 1, column = 2 )

btn7 = Button ( frame, text = 7, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (7) )
btn7.grid ( row = 2, column = 0 )

btn8 = Button ( frame, text = 8, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (8) )
btn8.grid ( row = 2, column = 1 )

btn9 = Button ( frame, text = 9, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (9) )
btn9.grid ( row = 2, column = 2 )

btn0 = Button ( frame, text = 0, height = 4, width = 10, font = 35, command = lambda: pressionar_teclas (0) )
btn0.grid ( row = 3, column = 0 )

btn_somar = Button ( frame, text = '+', height = 4, width = 10, font = 35, command = lambda: pressionar_teclas ('+') )
btn_somar.grid ( row = 0, column = 3 )

btn_subt = Button ( frame, text = '-', height = 4, width = 10, font = 35, command = lambda: pressionar_teclas ('-') )
btn_subt.grid ( row = 1, column = 3 )

btn_mult = Button ( frame, text = '*', height = 4, width = 10, font = 35, command = lambda: pressionar_teclas ('*') )
btn_mult.grid ( row = 2, column = 3 )

btn_divi = Button ( frame, text = '/', height = 4, width = 10, font = 35, command = lambda: pressionar_teclas ('/') )
btn_divi.grid ( row = 3, column = 3 )

btn_resu = Button ( frame, text = '=', height = 4, width = 10, font = 35, command = operacoes )
btn_resu.grid ( row = 3, column = 2 )

btn_deci = Button ( frame, text = '.', height = 4, width = 10, font = 35, command = lambda: pressionar_teclas ('.') )
btn_deci.grid ( row = 3, column = 1 )

btn_limp = Button ( tela, text = 'Limpar', height = 4, width = 12, font = 35, command = limpar )
btn_limp.pack ()


# ==================== Criar a tela ====================
tela.mainloop()