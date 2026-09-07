quantidade = 0
soma = 0
aprovados = 0
reprovados = 0
maior_nota = None  # None significa "nada" ou "sem valor".
menor_nota = None  # Usado quando algo não tem um valor definido ou não retorna nada.

nota = float(input("Digite uma nota entre 1 e 10 (-1 para encerrar o programa): "))

while nota != -1:
    quantidade += 1
    soma += nota

    if nota >= 7 and nota <= 10:
        aprovados += 1
    elif nota < 7 and nota >= 0:
        reprovados += 1
    else:
        print("Digite uma nota entre 1 e 10")

    if maior_nota is None or nota > maior_nota:
        maior_nota = nota
    if menor_nota is None or nota < menor_nota:
        menor_nota = nota

    nota = float(input("Digite uma nota entre 1 e 10 (-1 para encerrar o programa): "))

if quantidade > 0:
    media = soma / quantidade

    print(f"Quantidade de notas: {quantidade}")
    print(f"Soma das notas: {soma}")
    print(f"Media da turma: {media}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
else:
    print("Nenhuma nota foi informada.")
