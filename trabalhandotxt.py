#importar biblioteca padrão

import os
os.getcwd()
# retorna o diretório que está sendo utilizado pelo python

os.chdir('.../diretório') #altera para o diretório alvo

data = open('arquivo.txt')
print(data.readline(), end='') #retorna cada linha do arquivo

data.seek(0) 
#retorna para o início da linha do arquivo

for each_line in data:
    print(each_line, end='')
    
#retorna todo o arquivo

each_line.split("character")
#separa em listas os characteres entre o character mencionado no split


# alterando o txt ignorando o erro Pág. 95

for each_line in data:
	try:
		(role, line_spoken) = each_line.split(':',1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
	except:
		pass
