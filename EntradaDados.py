# Input
# Para que o usuario possa interagir com o programa e informar dados, utiliza-se a funcao input()

fruta = input("Digite o nome de uma fruta: ")
print(fruta)

# Os dados do input sao considerados strings. Para dar entrada aos tipos numéricos, eh preciso converte-los.

codigo = int(input("Digite o codigo do funcionario: "))
nome = input("Digite o nome do funcionario: ")
salario = float(input("Informe o salario: "))
ativo = True

print("Codigo: %d" %codigo)
print("Nome: %s" %nome)
print("Salario: %.2f" %salario)
print("Ativo: %r" %ativo)