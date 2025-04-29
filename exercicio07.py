numeros = [0]*5

for x in range (len(numeros)):
    numeros[x] = int(input(f"Digite o número {x+1}: "))

for i in range (len(numeros)-1,-1,-1):
    print(numeros[i])