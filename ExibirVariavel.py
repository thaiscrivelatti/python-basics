# Mascara de formatacao
# Eh possivel utilizar identificadores para representar os tipos de dados das variaveis
#
# %d ou %i    Inteiro
# %f          Float ou decimal
# %ld         Long int
# %e ou %E    Decimal exponencial
# %c          Char/character
# %o          Int em formato octal
# %x ou %X    Int em formato hexadecimal
# %s          Char/string
# %r          Boolean

codigo = 105
nome = "Jose Santana"
salario = 1650.00
ativo = True

# Ao utilizar os identificadores, nao eh necessario utilizar virgula entre o texto e a variavel
# Mas eh preciso utilizar o sinal % antes da variavel
print("Código: %d" %codigo)
print("Nome: %s" %nome)
print("Salário: %.2f" %salario)
print("Ativo: %r" %ativo)
