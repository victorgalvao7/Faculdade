# ▪ Determine e mostre todos os números primos no intervalo de 2 a 2000.
# Dicas:
# ▪ Para resolver esse problema, primeiro faça um algoritmo que verifica se um número inteiro qualquer é
# primo ou não.
# ▪ A seguir, com esse código em mãos, faça os ajustes necessários para mostrar todos os números primos
# no intervalo solicitado.
# ▪ Você precisará colocar uma estrutura de repetição dentro da outra.
# ▪ Laços aninhados!!!!
n = 0
for i in range(2,2000):
    for c in range(2,i):
        if c % i == 0:
            n = 1
        if n != 1:
            print(f"{i}",end=", ")

