# Exemplo de estrutura de decisao simples

a = int(input("Informe um valor para A: "))
b = int(input("Informe um valor para B: "))

if (a>b):
    aux=a
    a=b
    b=aux

print("O valor de A agora eh: ", a)
print("O valor de B agora eh: ", b)

# Estrutura de decisao composta if-else
# Calcula a media entre duas notas

notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

mediaFinal = (notaA + notaB) / 2

if mediaFinal >= 7.0:
    print("A media: %.1f - Aprovado" %mediaFinal)
else:
    print("A media: %.1f - Reprovado" %mediaFinal)

# Estrutura if-elif-else
idade = int(input("Digite a idade: "))

if idade>18:
    print("Maior de idade")
elif idade>=16:
    print("Infanto juvenil")
else:
    print("Menor de idade")