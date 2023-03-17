#Criado tres variaveis e uma lista vazia para armazenar os valores inseridos posteriormente.
pares = []
impares = []
numeros = []

#Utilizado aqui um loop (for) para inserção dos 5 numeros, atraves da função (input) e utilizado também a funão (int) para converter os numeros em inteiros.
for i in range(5):
    numeros.append(int(input(f"Insira o número {i+1}: ")))

#Utilizado a funão (sum) para somar todos os numeros inseridos, em seguida calculado a media dividindo a soma pelo tamanho (len) da lista dos numeros.
soma = sum(numeros)
media = soma / len(numeros)

#Utilizado a função (for) para percorrer a lista (numeros), em seguida feito a verificacao se o numero é impar ou par atraves do (if) e (else).
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#Utilizado função (print) para exibir no console o código.
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Média geral: {media}")