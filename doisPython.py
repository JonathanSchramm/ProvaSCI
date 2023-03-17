# Solicitação dos 5 numeros atraves do (input).
num1 = int(input("Digite aqui o primeiro número: "))
num2 = int(input("Digite aqui o segundo número: "))
num3 = int(input("Digite aqui o terceiro número: "))
num4 = int(input("Digite aqui o quarto número: "))
num5 = int(input("Digite aqui o quinto número: "))

# Verificacao do maior numero atraves do (max) e (min).
maior = max(num1, num2, num3, num4, num5)
menor = min(num1, num2, num3, num4, num5)

# Impressao do maior e menor numero.
print("O maior número é", maior)
print("O menor número é", menor)