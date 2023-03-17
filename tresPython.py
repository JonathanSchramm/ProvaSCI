# Utilizado a funcao (while true) para fazer um loop e continuar a solicitar os nomes e notas dos alunos até que a funcao (break) seja ativa.
while True:
    # Solicitação do nome e notas atraves do (input), utilizado (float) porque se trata de numeros flutuantes.
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    # Calculo da média das notas e dividido pelo total de notas solicitado.
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Imprime o resultado e faz a verificacao se o aluno atingiu a media ou nao atraves do (if) e (else).
    print(f"O aluno {nome} obteve média {media:.2f}.")
    if media < 6:
        print("Resultado: Reprovado\n")
    else:
        print("Resultado: Aprovado\n")

    # Questiona o usuario se ele deseja encerrar ou nao o programa utilizando a funcao (break).
    opcao = input("Deseja encerrar o programa? (S/N) ")
    if opcao.upper() == "S":
        break