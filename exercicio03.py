nomes = [""]*3

for i in range (len (nomes)):
    nomes[i] = (input("Digite o nome do aluno: "))

for x in range (len(nomes)):
    print(f"{nomes[x]} está na posição {x}")