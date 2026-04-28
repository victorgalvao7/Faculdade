#▪ Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário.
n = int(input("Digite um valor: "))
for c in range(2,n,2):
    print(f"{c}",end=", ")