quantidade=int(input("Quantas pessoas serão convidadas para a festa: "))
lista_convidados=[]

for convidado in range(quantidade):
	nome=input("Insira o nome do convidado: ")
	lista_convidados.append(nome)
	
print(lista_convidados)