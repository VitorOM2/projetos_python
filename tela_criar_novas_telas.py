# ==================== Importações ====================
from tkinter import *
# ==================== Importações ====================


# ==================== Funções ====================

def criar_nova_tela():
    #tela_nova = Toplevel() #Cria um nova janela a cima da janela antiga. A janela é conectada a janela anterior
    tela_nova = Tk()        #Cria uma nova janela indepedente
    tela_antiga.destroy()   #Fecha a tela antiga

# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela_antiga = Tk()

# ===== Botões =====
btn_criar_tela = Button(tela_antiga,
    text    = 'Criar nova tela',
    command = criar_nova_tela)

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Botões =====
btn_criar_tela.pack()

# ===== Tela =====
tela_antiga.mainloop()

# ==================== Mostrar ====================