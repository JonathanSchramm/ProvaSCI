# Cria uma matriz bidimensional de três linhas e quatro colunas
matriz = [[0] * 4 for _ in range(3)]
maior_media = 0
menor_media = float("inf")
nome_maior_media = ""
nome_menor_media = ""

# Solicita os nomes dos três alunos e suas quatro notas
for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    for j in range(4):
        matriz[i][j] = float(input(f"Digite a {j+1}ª nota do aluno {nome}: "))
    media = sum(matriz[i]) / 4
    print(f"O aluno {nome} obteve média {media:.2f}.")
    if media > maior_media:
        maior_media = media
        nome_maior_media = nome
    if media < menor_media:
        menor_media = media
        nome_menor_media = nome

# Imprime o nome do aluno com a maior média e o nome do aluno com a menor média
print(f"O aluno com a maior média foi {nome_maior_media} com média {maior_media:.2f}.")
print(f"O aluno com a menor média foi {nome_menor_media} com média {menor_media:.2f}.")
