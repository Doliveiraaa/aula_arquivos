def calcular_media(nota1, nota2, nota3):
    return round((nota1 + nota2 + nota3) / 3, 2)

alunos_exame = []

with open("exame.txt", "r") as arquivo_exame:
    linhas_exame = arquivo_exame.readlines()

for linha_exame in linhas_exame:
    nome_exame, nota_exame = linha_exame.strip().split(": ")
    alunos_exame.append((nome_exame, float(nota_exame)))

medias_anteriores = {}
with open("aprovados.txt", "r") as arquivo_aprovados:
    for linha_aprovado in arquivo_aprovados:
        nome_aprovado, media_anterior = linha_aprovado.strip().split(": ")
        medias_anteriores[nome_aprovado] = float(media_anterior)

aprovados_apos_exame = []

for nome, nota_exame in alunos_exame:
    if nome in medias_anteriores:
        media_anterior = medias_anteriores[nome]
        nova_media = calcular_media(media_anterior, nota_exame, media_anterior)
        
        if nova_media >= 5:
            resultado = "Aprovado após exame"
            aprovados_apos_exame.append((nome, nova_media))
        else:
            resultado = "Reprovado após exame"
            
        with open("aprovados.txt", "a") as arquivo_aprovados:
            arquivo_aprovados.write(f"{nome}: {nova_media:.2f} - {resultado}\n")

print("Resultados do exame processados e salvos em aprovados.txt.")