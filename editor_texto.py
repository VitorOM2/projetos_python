# ==================== Importações ====================
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


# ==================== Funções ====================
def mudar_cor():
    pass

def mudar_fonte(*args):
    pass

def novo_arquivo():
    pass

def salvar_arquivo():
    pass

def cortar():
    pass

def copiar():
    pass

def colar():
    pass

def sobre():
    pass

def sair():
    pass


# ==================== Instanciação da Tela ====================
tela = Tk()
tela.title('Editor-V')
file = None

# ===== Configura o tamanho da tela =====
largura_janela = 500
largura_tela   = tela.winfo_screenwidth()

altura_janela  = 500
altura_tela    = tela.winfo_screenheight()

x = int ( ( largura_tela / 2 ) - ( largura_janela / 2 ) )
y = int ( ( altura_tela  / 2 ) - ( altura_janela  / 2 ) )

tela.geometry( "{}x{}+{}+{}" .format( largura_janela, altura_janela, x, y ) )


# ===== Configura a Fonte =====
fonte_nome = StringVar( tela )
fonte_nome.set ( 'Arial' )

fonte_tamanho = StringVar( tela )
fonte_tamanho.set ( '25' )


# ==================== Instanciação dos widgets ====================
# ===== Área de texto =====
area_texto = Text ( tela, font = (fonte_nome.get(), fonte_tamanho.get() ) )

# ===== Barra de rolagem =====
barra_rolagem = Scrollbar ( area_texto )

# ==================== Cria Tela ====================
tela.mainloop()