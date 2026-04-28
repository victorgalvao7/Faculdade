# ▪ Escreva um algoritmo que recebe um inteiro positivo n e imprime todos os divisores positivos de n.
# ▪ Utilize o laço for.
# ▪ Exemplo:
# Suponha que n = 28, nessa situação devemos imprimir os números
# 1, 2, 4, 7, 14 e 28, que são todos os divisores do 28.
# ▪ Dica: para o número ser divisor de n, a divisão precisa ter resto nulo.
while True:
    n = int(input("Digite um valor possítivo: "))
    if n > -1:
        break
    else:
        ("Valor informado negativo digite novamente!")
for i in range(1,n+1):
    if n % i == 0:
        if i != n:
            print(f"{i}",end=", ")
        else:
            print(f"{i}")