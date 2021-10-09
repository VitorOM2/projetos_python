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

def cortar():
    pass

def copiar():
    pass

def colar():
    pass

# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Menu =====
menu_barra   = Menu( tela )

menu_arquivo = Menu( menu_barra,
    tearoff  = 0,
    font     = ( 'arial', 15 ) )
    
menu_editar  = Menu( menu_barra,
    tearoff  = 0,
    font     = ( 'arial', 15 ) )

# ==================== Instanciação ====================


# ==================== Configurações ====================

# ===== Tela =====
tela.config(menu = menu_barra)

# ===== Menu =====
menu_barra.add_cascade(label = 'Arquivo', menu = menu_arquivo)
menu_barra.add_cascade(label = 'Editar',  menu = menu_editar)

menu_arquivo.add_command(label = 'Abrir',  command = abrir_arquivo  )
menu_arquivo.add_command(label = 'Salvar', command = salvar_arquivo )
menu_arquivo.add_separator()
menu_arquivo.add_command(label = 'Sair', command = quit)

menu_editar.add_command(label = 'cortar', command = cortar )
menu_editar.add_command(label = 'copiar', command = copiar )
menu_editar.add_command(label = 'colar',  command = colar  )

# ==================== Configurações ====================


# ==================== Mostrar ====================

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================