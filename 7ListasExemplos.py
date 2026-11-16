# Calcular média de um aluno
notas = [9, 7, 4, 8]
media = sum(notas) / len(notas)
print(f"A media obtida pelo aluno foi : {media}")

# Olá customizado
nomes = ["Ana", "Álvaro", "Letícia"]
for nome in nomes:
    print(f"Seja muito bem-vindo(a) {nome}. Aproveite o dia!")

# Filtro de nomes de alunos iniciados com a lera J
alunos = ["Ana", "João", "Jair", "Felipe"]
alunosJ = []
for aluno in alunos:
    if aluno.startswith("J"):
        alunosJ.append(aluno)
print(alunosJ)
