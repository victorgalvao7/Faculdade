byte = 42
print(f"Decimal: {byte}")
print("Binário","{:00b}".format(byte,))

letra = "A"

codigo = ord(letra)

print(f"Letra: {letra}")
print(f"Código ASCII: {codigo}")
print("Binário", "{:00b}".format(codigo))
print("Hexadecimal:",hex(codigo))

#analiser uma palavra

texto = "Miguel é gay"

for letra in texto:
    codigo = ord(letra)

    print(
        letra,
        "->",
        codigo,
        "->",
        "{:08b}".format(codigo,)
    )