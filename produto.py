largura = 50


def ler_texto(mensagem, obrigatorio=True):
    while True:
        valor = input(mensagem).strip()
        if valor or not obrigatorio:
            return valor
        print("Erro: este campo não pode ficar vazio.")


def ler_preco(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            preco = float(entrada.replace(",", "."))
            if preco <= 0:
                print("Erro: o preço deve ser maior que zero.")
                continue
            return round(preco, 2)
        except ValueError:
            print("Erro: valor inválido. Digite apenas números (ex.: 19,90).")


def ler_inteiro(mensagem, minimo=0):
    while True:
        entrada = input(mensagem).strip()
        try:
            numero = int(entrada)
            if numero < minimo:
                print(f"Erro: o valor deve ser no mínimo {minimo}.")
                continue
            return numero
        except ValueError:
            print("Erro: valor inválido. Digite um número inteiro.")


def formatar_preco(valor):
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def cadastrar_produto(produtos):
    print("\n" + "=" * largura)
    print("CADASTRAR PRODUTO".center(largura))
    print("=" * largura)

    nome = ler_texto("Nome do produto: ")