a = [0]*5
m=[0]*5

for i in range (len(a)):
    a[i]= int (input(f"Digite o número {i+1}: "))

x = int(input("Digite um número multiplicador: "))

for y in range (len(m)):
    m[y]= a[y] * x
    print(f"{a[y]} X {x} = {m[y]}")
print(m)
