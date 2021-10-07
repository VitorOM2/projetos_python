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

    if messagebox.askokcancel(title = 'Ok ou cancelar', message = 'Ok ou cancelar'):
        print ('ok')
    else:
        print ('cancelar')

    if messagebox.askretrycancel(title = 'Tentar de novo?', message = 'Tentar de novo'):
        print ('Você tentou de novo')
    else:
        print ('Você não tentou de novo')

    if messagebox.askyesno(title = 'Sim ou não', message = "Sim ou não"):
        print ('Sim')
    else:
        print ('Não')

    print (messagebox.askquestion(title = 'Pergunta', message = 'Gosta de pizza?') )

    print (messagebox.askyesnocancel(title = 'Sim, Não Cancelar', message = 'Sim, não ou cancelar') )
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