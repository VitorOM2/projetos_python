# ===== BIBLIOTECAS =====
import os
import shutil
# ===== BIBLIOTECAS =====

# ===== VARIÁVEIS =====
path = 'teste4.txt'
# ===== VARIAÁVEIS =====

try:
  os.remove     ( path ) # deleta um arquivo
# os.rmdir      ( path ) * deleta um diretório vazio
# shutil.rmtree ( path ) * deleta um diretório com arquivos
except FileNotFoundError as e:
    print ( e )
except PermissionError as e:
    print ( e )
except OSError as e:
    print ( e )
else:
    print ( "O {} foi deletado".format( path ) )