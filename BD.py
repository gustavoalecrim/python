#Determina o diretório
os.chdir('PATH')

#Cria o banco de dados
Nomes=[]
data = open('ARQUIVO.txt')

#Cria o primeiro campo
print('CAMPO1')
CAMPO1.append(input())
print('MENSAGEM 1')
print('MENSAGEM 2')

#Cria o segundo campo
print('CAMPO2')
CAMPO2=[]
CAMPO2.append(input())

#Cria o terceiro campo
print("CAMPO3")
CAMPO3=[]
CAMPO3.append(input())

#Cria o quarto campo
print('CAMPO4')
CAMPO4=[]
CAMPO4.append(input())

#Salva os campos no arquito
print('MENSAGEM 4')
data = open("data.txt","w")
print(CAMPO1,file=data)
print(CAMPO2,file=data)
print(CAMPO3,file=data)
print(CAMPO4,file=data)
data.close()


os.system("PAUSE")
