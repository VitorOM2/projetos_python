# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================

# ==================== Funções ====================
def mostrar():
    if x.get() == 1:
        print ('Você concorda')
    else:
        print ('Você não concorda')
# ==================== Funções ====================


# ==================== Instanciação ====================
tela = Tk()

#===== Caixa de assinalar =====
x = IntVar()
caixa_assinalar = Checkbutton(tela,
                            text = "Eu concordo com alguma coisa",
                            font = ('Arial', 16),
                            fg   = '#00ff00',
                            bg   = 'black',
                            activeforeground = "#00FF00",
                            activebackground = "black",
                            padx             = 25,
                            pady             = 10,
                            variable = x,
                            onvalue  = 1,
                            offvalue = 0,
                            command = mostrar)
# ==================== Instanciação ====================


# ==================== Mostrar ====================
#===== Caixa de assinalar =====
caixa_assinalar.pack()
# ===== Tela =====
tela.mainloop()
# ==================== Mostrar ====================
