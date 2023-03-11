x = int(input("Digite um número inteiro: "))
soma = 0
while x != 0:
        r = x % 10
        x = x // 10
        soma = soma + r
print(soma)
