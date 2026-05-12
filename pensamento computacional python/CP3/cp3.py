temperaturas = [[28, 31, 34, 33], 
                [25, 27, 29, 28], 
                [32, 35, 36, 34], 
                [24, 26, 25, 27]]
total = 0
critico = 0
media = 0
maior = 0
maior_media = 0
for i in range(0, 4):
    for j in range (0,4):
        total += temperaturas[i][j]
        if temperaturas[i][j] >= 33:
            critico +=1
    media = total/4
    if media > maior_media:
        maior = i
        maior_media = media
    print(f"Sala {i+1}")
    print(f"Média: {media}")
    total = 0
    print(f"Registros críticos: {critico}\n")
    critico = 0
print(f"Sala com maior risco: Sala {maior}")
