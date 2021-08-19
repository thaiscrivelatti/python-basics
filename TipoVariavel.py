# Variaveis
# A declaracao das variaveis pode ser feita em qualquer momento do codigo
# Não eh necessario definir o tipo da variavei, pois a linguagem interpreta o tipo de dado que esta sendo armazenado

codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

tipo = type(salario)
print(salario)
print(tipo)

# Concatenacao
# Utiliza-se virgula separando os textos e as variaveis
print("Código: ", codigo, "Nome: ", nome, "Salário atual: ", salario)

# Sequencia de escapes
# Auxilia na formatação da exibição dos dados
# \n	Insere uma quebra de linha
# \t	Insere tabulacao horizontal
# \v	Insere tabulacao vertical
# \r	Equivalente ao efeito da tecla Enter
# \’	Aspas simples
# \”	Aspas duplas
# \\	Insere uma barra invertida (backslash)
# \a	Chamado de ASC bell ou beep do sistema. Se houver suporte, aciona um bipe
# \b	Aciona o backspace, ou seja, apaga o caractere anterior
# \f	Insere uma quebra de pagina
# \u	Insere um caractere UNICODE. Deve acompanhar um codigo com 4 numeros