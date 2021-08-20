# Calculo de media de notas
# O usuario deve digitar duas notas. O programa deve calcular e exibir a media das notas informando se
# o aluno está aprovado, caso nota igual ou acima de 7.0, ou reprovado, se menor que 7.0
# O programa deverá duas funcoes: uma para leitura das notas, outra para calculo da media.

def lerNotas():
    nota = float(input("Digite a nota do aluno: "))
    return nota


def calculoMedia(n1, n2):
    media = (n1+n2)/2
    print("Media do aluno: %f" %media)
    if media >= 7.0:
        print("APROVADO")
    else:
        print("REPROVADO")


n1 = lerNotas()
n2 = lerNotas()
calculoMedia(n1, n2)

