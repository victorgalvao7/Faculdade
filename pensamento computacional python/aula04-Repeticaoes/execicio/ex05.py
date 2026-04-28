for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    if i == 0:
        maior = n
    elif n > maior:
        maior = n
print(f"O maior valor digitado foi {maior}")