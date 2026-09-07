# Linguagem de Programação I

Exercícios desenvolvidos durante a disciplina de Linguagem de Programação I (Engenharia de Software), com foco em estruturas de repetição, contadores, acumuladores e condicionais em Python.

## Desafios

### 1. Análise de Vendas (`for`)
📂 [`vendas.py`]

Sistema que analisa as vendas de um dia de uma loja: recebe a quantidade de vendas e o valor de cada uma, e apresenta um relatório com total vendido, média, percentual de vendas acima de R$100, maior e menor venda, e uma contagem regressiva de encerramento de caixa.

**Conceitos praticados:**
- `for` + `range()`
- Acumulador (soma total)
- Contadores (vendas acima/abaixo de um limite)
- Condicionais `if`
- Cálculo de média e percentual
- `range()` com passo negativo (contagem regressiva)
- Funções `max()` / `min()`

### 2. Registro de Notas (`while`)
📂 (./notas.py)

Sistema que registra notas de alunos até que o usuário digite `-1` (valor sentinela). Ao final, apresenta quantidade de notas, soma, média da turma, aprovados/reprovados e a maior/menor nota — tudo sem usar listas.

**Conceitos praticados:**
- `while` com valor sentinela
- Leitura antecipada (ler antes do loop para testar a condição)
- Acumulador e contadores
- Encontrar maior/menor valor sem lista, usando `None` como valor inicial "vazio"
- Tratamento de caso extremo (nenhuma nota informada)

## Tecnologias

- Python 3
