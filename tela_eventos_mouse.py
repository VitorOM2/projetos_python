# ==================== Importações ====================
from tkinter import *


# ==================== Funções ====================
def clique_mouse(evento):
    print ( 'Coordenadas do clique: X: ' + str ( evento.x ) + ", Y: " + str(evento.y) )

# ==================== Instanciação da Tela ====================
tela = Tk()
tela.bind( '<Button-1>' , clique_mouse ) # Botão esquerdo
tela.bind( '<Button-2>' , clique_mouse ) # Scroll
tela.bind( '<Button-3>' , clique_mouse ) # Botão direito

# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()