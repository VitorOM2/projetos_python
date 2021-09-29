# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================

# WIDGETS = elementos GUI: Botões, caixas de texto, rótulos, imagens
# WINDOWS = Serve como container para os widgets

# ==================== Instanciação ====================
tela  = Tk()
# ==================== Instanciação ====================


# ==================== Configurações ====================

# ===== Tamanho =====
tela.geometry("500x500")

# ===== Nome =====
tela.title("Primeiro programa GUI")

# ===== Imagem =====
# icone = PhotoImage( file = '' ) Define o icone da tela
# tela.iconphoto (True,icone)

# ===== Cor de Fundo =====
tela.config (background = "Grey")

# ==================== Configurações ====================


# ==================== Mostrar ====================
tela.mainloop() # Cria a tela 
# ==================== Mostrar ====================
