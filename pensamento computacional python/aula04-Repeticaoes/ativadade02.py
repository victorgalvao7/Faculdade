while True:
    notaA = float(input("Digite a primeira nota: "))
    if notaA < 0 or notaA > 10:
        print("A nota deve está entre 10 e 0 digite novamente!!!")
    else:
        break
while True:
    notaB = float(input("Digite a segunda nota: "))
    if notaB < 0 or notaB > 10:
        print("A nota deve está entre 10 e 0 digite novamente!!!")
    else:
        break
print(f"A média para o aulo que tirou {notaA} e {notaB} foi de {(notaA+ notaB) / 2}")