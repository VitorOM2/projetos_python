# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Instanciação ====================
tela   = Tk()
rotulo = Label(tela, text = "Hello World",
                     font = ('Arial', 40, 'bold'),
                     fg = '#00ff00',
                     bg = 'black',
                     relief = 'raised', #Borda
                     bd   = 10, #Tamanho da borda
                     padx = 20,
                     pady = 20 ) 
# ==================== Instanciação ====================


# ==================== Mostrar ====================
rotulo.pack()
# rotulo.place(x = 70, y = 0)

tela.mainloop()
# ==================== Mostrar ====================