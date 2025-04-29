nomes = [""]*3

for i in range (len (nomes)):
    nomes[i] = (input("Digite o nome do aluno: "))

for i in range (len(nomes)):
    print(f"{nomes[i]} está na posição {i}")