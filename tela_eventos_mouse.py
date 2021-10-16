# ==================== Importações ====================
from tkinter import *


# ==================== Funções ====================
def clique_mouse(evento):
    print ( 'Você apertou o botão do mouse' )

# ==================== Instanciação da Tela ====================
tela = Tk()
tela.bind( '<Button-1>' , clique_mouse )
# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()