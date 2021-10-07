# ==================== Importações ====================
from tkinter import *
from tkinter import messagebox
# ==================== Importações ====================


# ==================== Funções ====================
def clique():
    #messagebox.showinfo(title = 'Isto é uma caixa de texto',
    #    message = 'Olá')

    #messagebox.showwarning(title = 'Aviso!',   #Exemplo de caixa de texto mostrando aviso
    #    message = 'Olá')

    #messagebox.showerror(title = 'Erro!',
    #    message = 'Olá')

    if messagebox.askokcancel(title = 'Sim ou não', message = 'Sim ou não'):
        print ('Sim')
    else:
        print ('Não')

# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_caixa_de_texto = Button(tela,
    command = clique,
    text    = 'Clique aqui')

# ==================== Instanciação ====================


# ==================== Mostrar ===================

# ===== Botões =====
btn_caixa_de_texto.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ===================