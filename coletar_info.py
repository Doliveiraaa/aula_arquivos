while True:
    while True:
        nome = input("Digite seu nome: ")
        if nome.strip():
            break
        else:   
            print("Por favor, insira o nome!")
        
    while True:
        try:    
            nota1 = int(input("Qual sua primeira nota? "))
            break
        except ValueError:
            print("Por favor, adicione um valor válido.")
            
    while True:
        try:
            nota2 = int(input("Qual sua segunda nota? "))
            break
        except ValueError:
            print("Por favor, adicione um valor válido.")

    while True:
        try:
            nota3 = int(input("Qual sua terceira nota? "))
            break
        except ValueError:
            print("Por favor, adicione um valor válido.")
        
    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"Nome do Aluno: {nome}, N.1: {nota1}, N.2: {nota2}, N.3: {nota3}\n")

    with open("notas.txt") as arquivo:
        print(arquivo.read())
        
    continuar = input("Deseja adicionar mais um aluno? (s/n) ")
    if continuar != "s":
        break
    
with open("notas.txt") as arquivo:
    print(arquivo.read())
    