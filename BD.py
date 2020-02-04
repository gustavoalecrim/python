os.chdir('c:/Users/Eleutério Alecrim/Downloads')
Nomes=[]

data = open('data.txt')
print('Qual o seu nome?')
Nomes.append(input())
print('Olá')
print('é um prazer te conhecer')
print('Quantos anos você tem?')
anos=[]
anos.append(input())
print("Qual o seu bairro?")
bairro=[]
bairro.append(input())
print('Qual a rua?')
rua=[]
rua.append(input())
print('Ok! agora nos conhecemos.')
data = open("data.txt","w")
print(Nomes,file=data)
print(anos,file=data)
print(bairro,file=data)
print(rua,file=data)
data.close()


os.system("PAUSE")
