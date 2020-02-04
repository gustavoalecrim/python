# coding: utf-8

#Busca específica
exportar = 'não'
repetir = 'sim'
while (repetir == 'sim'):
#Informe qual o arquivo .txt deseja aplicar a busca
    data = open('TarifacaoSVA_5511989999079.txt','r')
    print('informe o dado que deseja buscar')
    busca = input()
    for linha in data:
        linha = linha.rstrip()
        if busca in linha:
            print(linha)
    print('Deseja exportar para arquivo?')
    exportar = input()
    if exportar == 'sim':
        print('exportando o arquivo resultado de busca.txt')
        arquivo = open('resultado de busca.txt','w')
        data = open('TarifacaoSVA_5511989999079.txt','r')
        for linha in data:
            if busca in linha:
                arquivo.write(linha)
        arquivo.close()
    print('Deseja realizar nova busca?')
    repetir = input()

