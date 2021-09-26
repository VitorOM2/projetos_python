# *** Copyfile() = Copia o conteúdo de um arquivo
# *** Copy    () = Copyfile() + mode de permissão + o destinatario pode ser um diretório
# *** Copy2   () = Copy + copia os metadados

import shutil

shutil.copyfile('teste.txt', 'teste2.txt') #Origem, Destino