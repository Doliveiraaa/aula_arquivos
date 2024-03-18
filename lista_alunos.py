def imprimir_resultados(arquivo):
    try:
        with open(arquivo, "r") as f:
            print(f"\n{'Alunos Aprovados' if 'aprovados' in arquivo else 'Alunos Reprovados':^40}\n")
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")

imprimir_resultados("aprovados.txt")
imprimir_resultados("reprovados.txt")