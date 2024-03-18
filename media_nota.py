def calcular_media(nota1, nota2, nota3):
    return round((nota1 + nota2 + nota3) / 3, 2)

alunos = []

with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    partes = linha.split(", ")
    
    aluno_info = {}
    
    for parte in partes:
        campo, valor = parte.split(": ")
        campo = campo.strip()
        valor = valor.strip().replace("\n", "")
        
        aluno_info[campo] = valor
    
    alunos.append(aluno_info)

resultados = []

for aluno in alunos:
    nome_aluno = aluno["Nome do Aluno"]
    nota1 = int(aluno["N.1"])
    nota2 = int(aluno["N.2"])
    nota3 = int(aluno["N.3"])
    media = calcular_media(nota1, nota2, nota3)
    
    if media >= 7:
        resultado = "Aprovado"
    elif 5 <= media < 7:
        resultado = "Exame"
    else:
        resultado = "Reprovado"
        
    resultados.append((nome_aluno, media, resultado))

aprovados = [(nome, media) for nome, media, resultado in resultados if resultado == "Aprovado"]
exame = [(nome, media) for nome, media, resultado in resultados if resultado == "Exame"]
reprovados = [(nome, media) for nome, media, resultado in resultados if resultado == "Reprovado"]


with open("aprovados.txt", "w") as arquivo:
    for nome, media in aprovados:
        arquivo.write(f"{nome}: {media}\n")

with open("exame.txt", "w") as arquivo:
    for nome, media in exame:
        arquivo.write(f"{nome}: {media}\n")

with open("reprovados.txt", "w") as arquivo:
    for nome, media in reprovados:
        arquivo.write(f"{nome}: {media}\n")

print("Resultados salvos! Alunos aprovados em: aprovados.txt, Alunos de exame em: exame.txt e Alunos reprovados em: reprovados.txt.")