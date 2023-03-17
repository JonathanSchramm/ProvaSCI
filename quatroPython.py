# Vetor criado a partir de uma lista, predefinindo em 5.
vetor = [0] * 5

# Solicito atraves do loop (for) os 5 numeros do vetor.
for i in range(5):
    vetor[i] = int(input("Digite um número: "))

# Imprime no terminal o valor do numero na posicao tres.
print(f"O valor da posição três é {vetor[4]}.")