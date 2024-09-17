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

nome_arquivo = "hamlet.txt" 
total_palavras = contar_palavras(nome_arquivo)

if total_palavras != -1:
    print(f"O livro Hamlet tem {total_palavras} palavras.")
