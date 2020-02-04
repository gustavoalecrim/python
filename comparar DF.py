# coding: utf-8
from datetime import datetime
now = datetime.now()

print('INICIANDO A ANГЃLISE DE DADOS...')
print('Este procedimento requer alguns minutos, por favor aguarde!')
print('')
print('')
    
Total = 0
# Abrir o arquivo de registros Г  serem pesquisados

data = open('testlist.txt','r')
for linha in data:
    linha = linha.rstrip()
    data2 = open('VPN_RJ1.txt','r')
    for linha2 in data2:
        linha2 = linha2.rstrip()
        if linha in linha2:
            Total = Total + 1
            print('Este terminal Г© comum no GOL2 e GOL3 ' + linha)
print('')
      
print('O total de terminais comuns encontrados foi')
print(Total)
print('')
print('ANГЃLISE CONCLUГЌDA COM SUCESSO!')

      
