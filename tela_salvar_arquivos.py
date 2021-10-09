# ==================== Importações ====================
from tkinter import *
from tkinter import filedialog
# ==================== Importações ====================


# ==================== Funções ====================
def salvar_arquivo():
    arquivo      = filedialog.asksaveasfile(
        defaultextension = '.txt',

        filetypes = [
            ('arquivo de texto', '.txt'),
            ('html', '.html'),
            ('todos os arquivos', '.*')
        ])

    arquivo_texto = str ( caixa_texto.get(1.0, END) )
    arquivo.write(arquivo_texto)
    arquivo.close()
# ==================== Funções ====================


# ==================== Instanciação ====================

# ===== Tela =====
tela = Tk()

# ===== Botões =====
btn_salvar = Button(
    text    = 'Salvar',
    command = salvar_arquivo)

# ===== Caixa de texto =====
caixa_texto = Text()

# ==================== Instanciação ====================


# ==================== Mostrar ====================

# ===== Botões =====
btn_salvar.pack()

# ===== Caixa de texto =====
caixa_texto.pack()

# ===== Tela =====
tela.mainloop()

# ==================== Mostrar ====================