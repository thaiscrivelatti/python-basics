# For/para
# Lista numeros ate 10
for n in range(10):
    print(n)

print("\n")

# Lista numeros do 5 ate no maximo 15
for n in range(5,16):
    print(n)

print("\n")

# Lista numeros ate 10, em ordem decrescente
for n in range(10, 0, -1):
    print(n)

print("\n")

# While/enquanto
# Lista numeros de 1 a 15 em ordem crescente
x = 1
while x<=15:
    print(x)
    x=x+1

# Calcula media dos valores. Encerra quando inserido um numero negativo
qtd=0
soma=0
media=0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um valor: "))

media = soma/qtd
print("\n Total da soma: ", soma)
print("\n Qtd valores digitados: ", qtd)
print("\n Media final: ", media)
