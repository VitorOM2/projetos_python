# ==================== Importações ====================
from tkinter import *
from tkinter import filedialog
# ==================== Importações ====================


# ==================== Funções ====================

def abrir_arquivo():
    arquivo_path = filedialog.askopenfilename(title = 'Abrir arquivo')
    arquivo      = open (arquivo_path, 'r')
    print ( arquivo.read() )
    arquivo.close()

def salvar_arquivo():
    arquivo      = filedialog.asksaveasfile(
        defaultextension = '.txt',

        filetypes = [
            ('arquivo de texto', '.txt'),
            ('html', '.html'),
            ('todos os arquivos', '.*')
        ])

    if arquivo is None:
        return
    
    arquivo.close()

# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Menu =====
menu_barra   = Menu(tela)
menu_arquivo = Menu(menu_barra,
    tearoff = 0)

# ==================== Instanciação ====================


# ==================== Configurações ====================

# ===== Tela =====
tela.config(menu = menu_barra)

# ===== Menu =====
menu_barra.add_cascade(label = 'Arquivo', menu = menu_arquivo)

menu_arquivo.add_command(label = 'Abrir',  command = abrir_arquivo  )
menu_arquivo.add_command(label = 'Salvar', command = salvar_arquivo )
menu_arquivo.add_separator()
menu_arquivo.add_command(label = 'Sair', command = quit)

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================