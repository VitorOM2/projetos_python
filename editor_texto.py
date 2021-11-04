# ==================== Importações ====================
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


# ==================== Funções ====================
def mudar_cor():
    cor = colorchooser.askcolor(title="Escolha uma cor")
    area_texto.config(fg=cor[1])

def mudar_fonte(*args):
    area_texto.config( font = ( fonte_nome.get(), caixa_tamanho.get() ) )

def novo_arquivo():
    tela.title ("Sem título")
    area_texto.delete (1.0, END)

def abrir_arquivo():
    arquivo = askopenfilename(defaultextension=".txt",
        filetypes=[("Todos arquivos", "*.*"),("Arquivos de texto", "*.txt")])

    if arquivo is None:
        return
    else:
        try:
            tela.title(os.path.basename(arquivo))
            area_texto.delete(1.0, END)
            arquivo = open(arquivo, "r")
            area_texto.insert(1.0, arquivo.read())
        except Exception:
            print("Algo deu errado")
        finally:
            arquivo.close()

def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename ( initialfile='Sem Título',
                                             defaultextension=".txt",
                                             filetypes=[("Todos arquivos", "*.*"     ),
                                                        ("Arquivos de texto", "*.txt")])
    
    if arquivo is None:
        return
    else:
        try:
            tela.title ( os.path.basename( arquivo ) )
            file = open( arquivo, "w")
            file.write( area_texto.get(1.0, END))
        except Exception:
            print("Não deu para salvar arquivo")
        finally:
            arquivo.close()

def cortar():
    area_texto.event_generate ("<<Cut>>")

def copiar():
    area_texto.event_generate ("<<Copy>>")

def colar():
    area_texto.event_generate ("<<Paste>>")

def sobre():
    showinfo ("Sobre o programa: uma progrma simple que funciona como um editor de texto")

def sair():
    tela.destroy ()


# ==================== Instanciação da Tela ====================
tela = Tk()
tela.title('Editor-V')
file = None

# ===== Configura o tamanho da tela =====
largura_janela = 500
largura_tela   = tela.winfo_screenwidth()

altura_janela  = 500
altura_tela    = tela.winfo_screenheight()

x = int ( ( largura_tela / 2 ) - ( largura_janela / 2 ) )
y = int ( ( altura_tela  / 2 ) - ( altura_janela  / 2 ) )

tela.geometry( "{}x{}+{}+{}" .format( largura_janela, altura_janela, x, y ) )


# ===== Configura a Fonte =====
fonte_nome = StringVar( tela )
fonte_nome.set ( 'Arial' )

fonte_tamanho = StringVar( tela )
fonte_tamanho.set ( '25' )


# ==================== Instanciação dos widgets ====================
# ===== Área de texto =====
area_texto = Text ( tela, font = (fonte_nome.get(), fonte_tamanho.get() ) )

# ===== Grid =====
tela.grid_rowconfigure    (0, weight = 1 ) # Permite a textbox expandir
tela.grid_columnconfigure (0, weight = 1 ) # Permite a textbox expandir
area_texto.grid( sticky = N + E + S + W )

# ===== Barra de rolagem =====
barra_rolagem = Scrollbar ( area_texto )
barra_rolagem.pack ( side = RIGHT, fill = Y )             # A barra vai ficar na direita e preencher o eixo y
area_texto.config  ( yscrollcommand = barra_rolagem.set ) # Adiciona a barra de rolagem no textbox

# ===== Frame =====
frame = Frame( tela )
frame.grid()

# ===== Botões =====
btn_mudar_cor = Button ( frame, text = "Cor", command = mudar_cor)
btn_mudar_cor.grid     ( row = 0, column = 0 )

# ===== OptionMenu =====
#Importa outras fontes para poder alterar entre elas
caixa_fonte = OptionMenu( frame, fonte_nome, *font.families(), command = mudar_fonte )
caixa_fonte.grid( row = 0, column = 1 )

# ===== SpinBox =====
#Cria uma caixa que permite altera o tamanho da fonte
caixa_tamanho = Spinbox ( frame, from_=1, to=100, textvariable = fonte_tamanho, command = mudar_fonte )
caixa_tamanho.grid(row=0, column=2)

# ===== Barra de Menu =====
menu_barra = Menu( tela )
tela.config( menu = menu_barra )
# -----Arquivo-----
menu_arquivo = Menu ( menu_barra, tearoff = 0 )
menu_barra.add_cascade   ( label = "Arquivo", menu   = menu_arquivo   )
menu_arquivo.add_command ( label = "Novo",   command = novo_arquivo   )
menu_arquivo.add_command ( label = "Abrir",  command = abrir_arquivo  )
menu_arquivo.add_command ( label = "Salvar", command = salvar_arquivo )
menu_arquivo.add_separator()
menu_arquivo.add_command ( label = "Sair",   command = sair           )
# -----Editar-----
menu_editar = Menu ( menu_barra, tearoff = 0 )
menu_barra. add_cascade  ( label = "Editar", menu     = menu_editar   )
menu_editar.add_command  ( label = "Cortar", command  = cortar        )
menu_editar.add_command  ( label = "Copiar", command  = copiar        )
menu_editar.add_command  ( label = "Colar",  command  = colar         )
#-----Ajuda-----
menu_ajuda = Menu ( menu_barra, tearoff = 0 )
menu_barra.add_cascade   ( label = "Ajuda",  menu    = menu_ajuda     )
menu_ajuda.add_command   ( label = "Sobre",  command  = sobre          )



# ==================== Cria Tela ====================
tela.mainloop()