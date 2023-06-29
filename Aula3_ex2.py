idade=int(input("Insira sua idade: "))
peso=float(input("Insira seu peso: "))
altura=float(input("Insira sua altura: "))

if (idade>=18) and (peso>=60) and (altura>=1.70):
	print("Aprovado")
else:
	print("Negado")