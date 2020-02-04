#Programa para consolidar arquivo TXT (Muitos:1)

import os

os.chdir('/User/92035344/Documents/Python Scripts')
# Abre o arquivo redacao.txt para escrita:
with open("GOL_Consolidado.txt", "w") as file:

    # Percorre a lista de arquivos a serem lidos (INFORME OS ARQUIVOS):
    for temp in ['GOL2.txt','GOL3.txt']:

        # Abre cada arquivo para leitura:
        with open(temp, "r") as t:

            # Escreve no arquivo o conteúdo:
            file.writelines(t)

print('Consolidação concluída com SUCESSO!')

input()
exit()
