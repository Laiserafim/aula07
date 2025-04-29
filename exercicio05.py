notas = [0.0]*5
soma = 0
cont = 0

for i in range (len (notas)):
    notas[i] = float (input(f"Digite a nota do aluno {i+1}: "))

for s in range (len (notas)):
    soma += notas[s]

media = soma / len(notas)


for c in range (len (notas)):
    if notas [c] > media:
        cont += 1
print(f"Encontramos {cont} alunos acima da média {media}")


