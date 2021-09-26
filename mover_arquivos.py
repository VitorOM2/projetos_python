# ===== BIBLIOTECAS =====
import os
# ===== BIBLIOTECAS =====

# ===== VARIÁVEIS =====
origem  = 'teste3.txt'
destino = 'C:\\Users\\Cliente\\Desktop\\teste3.txt'
# ===== VARIAÁVEIS =====

try:
  if os.path.exists (destino):
      print ( "O arquivo já existe lá" )
  else:
      os.replace(origem, destino)
      print ( origem + ' foi movido' )
except FileNotFoundError as e:
  print (e)