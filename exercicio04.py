nomes = ["joão", "carlos", "maria","luiza", "isabel" ]

nome = input("Digite um nome: ")

for i in range (len (nomes)):
    if nomes[i] == nome:
        print(f"{nome} está na posição {i}")


