descrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))
valor = 1
while valor != 0 and decrescente:
	valor = int(input("Digite o proximo número da sequência: "))
	if valor > anterior:
		decrescente = false
	anterior = valor
if decrescente:
	print("A sequência está em ordem decrescente! :-) ")
else:
	print("A sequência não está em ordem decrescente! :-( ")