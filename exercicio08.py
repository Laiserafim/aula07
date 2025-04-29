nomes = [""]*1
senhas = [0]*1

for i in range (len(nomes)):
    nomes[i] = input(f"Cadastre um nome para o usuário {i+1}: ")
    senhas[i] = int(input(f"Cadastre uma senha para o usuário {i+1}: "))

logNome= input("Nome do usuário: ")
logSenha = int (input("Senha do usuário: "))

for x in range (len(nomes)):
    if nomes[x] == logNome and senhas[x] == logSenha:
        print("Login efetuado com sucesso!")
        break

    elif nomes[x] == logNome and senhas[x] != logSenha:
        print("senha incorreta")
        break

    else:
        print("incorreto")
        break
