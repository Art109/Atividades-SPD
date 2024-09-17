import time

def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            palavras = texto.split()
            num_palavras = len(palavras)
        return num_palavras
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return -1

def medir_tempo_execucao(nome_arquivo, num_execucoes):
    tempos = []
    for _ in range(num_execucoes):
        inicio = time.time()
        contar_palavras(nome_arquivo)
        fim = time.time()
        tempos.append(fim - inicio)
    tempo_medio = sum(tempos) / len(tempos)
    return tempo_medio

nome_arquivo = "hamlet.txt"  

# a) apenas o tempo de uma execução do programa 1
tempo_execucao_unica = medir_tempo_execucao(nome_arquivo, 1)
print(f"Tempo de uma execução do programa 1: {tempo_execucao_unica} segundos")

# b) tempo médio de 5 execuções do programa 1
tempo_medio_5_execucoes = medir_tempo_execucao(nome_arquivo, 5)
print(f"Tempo médio de 5 execuções do programa 1: {tempo_medio_5_execucoes} segundos")

# c) tempo médio de 10 execuções do programa 1
tempo_medio_10_execucoes = medir_tempo_execucao(nome_arquivo, 10)
print(f"Tempo médio de 10 execuções do programa 1: {tempo_medio_10_execucoes} segundos")

# d) tempo médio de 50 execuções do programa 1
tempo_medio_50_execucoes = medir_tempo_execucao(nome_arquivo, 50)
print(f"Tempo médio de 50 execuções do programa 1: {tempo_medio_50_execucoes} segundos")

# e) tempo médio de 100 execuções do programa 1
tempo_medio_100_execucoes = medir_tempo_execucao(nome_arquivo, 100)
print(f"Tempo médio de 100 execuções do programa 1: {tempo_medio_100_execucoes} segundos")
