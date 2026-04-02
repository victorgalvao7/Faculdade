while True:
    dia = int(input("Qual dia você nasceu: "))
    if dia <= 31 and dia > 0:
        break
while True:
    mes = int(input("Qual més você nasceu: "))
    if mes <= 12 and mes > 0:
        break
while True:
    ano = int(input("Qual ano você nasceu: "))
    if ano <= 2026 and ano > 1926:
        break
print(f"Sua data de nascimento formatada é {dia:0>2}/{mes:0>2}/{ano}")