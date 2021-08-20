# Manipulacao de arquivos

# Gravacao
# Utiliza-se funcao open(), passando como parametro o nome do arquivo com a extensao e o parametro 'w'
# "w" significa write, ou seja, escrever/gravar no arquivo
# Funcao write() escreve o texto passado por parametro no arquivo criado
# Utilizar SEMPRE a funcao close() após abrir e manipular o arquivo, caso contrario as alteracoes nao sao salvas

arquivo = open("arqTexto.txt", 'w')

arquivo.write("Fundamentos Python \n")
arquivo.write("Gravando informacoes no arquivo")
arquivo.close()

# Ao executar o codigo, nada é mostrado.
# Procurar na pasta do projeto o arquivo arqTexto.txt

# Leitura
# Funcao read() le um arquivo
# Passa-se como parametro um caminho de diretorio completo e o parametro 'r'
leitura = open("arqTexto.txt", 'r')
print(leitura.read())
leitura.close()


# Modos de leitura de arquivo
# r	    Abre o arquivo somente para leitura. O arquivo deve já existir.
# r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir.
#       A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo,
#       as linhas serão reescritas, conforme formos escrevendo.
# w	    Abre o arquivo somente para escrita, no início do arquivo.
#       Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
# w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
# a	    Abre o arquivo para escrita no final do arquivo. Não apaga o conteúdo preexistente.
# a+	Abre o arquivo para escrita no final do arquivo e leitura.

