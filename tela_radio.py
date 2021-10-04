# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================

comidas = ['pizza', 'hamburguer', 'cachorro quente']


def pedido():
    if ( x.get() == 0 ):
        print ('Você pediu: Pizza')
    elif ( x.get() == 1 ):
        print ('Você pediu: Hamburguer')
    elif ( x.get() == 2 ):
        print ('Você pediu: Cachorro quente')
    else:
        print ('Pedido invalido')


# ==================== Instanciação ====================
tela = Tk()

# ===== Radio =====
x = IntVar()
for i in range( len(comidas) ):    # Loop para os radios buttons
    radio_comidas = Radiobutton(tela,
        text      = comidas [i],   # Adicona texto para os radiobuttons
        variable  = x,             # Agrupa os radio buttons se a variável for a mesma
        value     = i,             # Atribui para cada radiobutton um valor diferente
        padx      = 25,            # Adiciona padding no eixo x
        font      = ('Arial', 20),
        command   = pedido           
        )            
                    
    radio_comidas.pack(anchor = 'w')
# ==================== Instanciação ====================


# ==================== Mostrar ====================
tela.mainloop()
# ==================== Mostrar ====================