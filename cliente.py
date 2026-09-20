from colorama import Fore, init
init(autoreset=True)

class Cliente:
    def __init__(self, nome, e_mail, telefone):
        self.nome = nome
        self.e_mail = e_mail
        self.telefone = telefone

def nome():
    while True:
            nome = input("\nInforme seu nome: ").strip()
    
            if nome == "":
                print(Fore.RED + "Você deve informar o seu nome.")
            else:
                return nome

def email():
    while True:
        email = input("Digite seu e-mail: ")

        if "@" not in email:
            print(Fore.RED + "Seu e-mail deve conter o @.")
        else:
            return email

def telefone():
    while True:
        telefone = input("Digite seu telefone: ").strip()
        telefone_correto = telefone.replace("-", "").replace(" ", "")

        if not telefone_correto.isdigit():
            print(Fore.RED + "Telefone inválido. Digite apenas números.")

        elif len(telefone_correto) < 10:
            print(Fore.RED + "Seu número de telefone deve conter ao menos 10 dígitos.")

        else:
            return telefone_correto

print(Fore.CYAN + f"\n{'=' * 50}")
print(Fore.CYAN + f"{'CADASTRO DE CLIENTES':^50}")
print(Fore.CYAN + f"{'=' * 50}")

nome_cliente = nome()
email_cliente = email()
telefone_cliente = telefone()
print(Fore.GREEN + "Cliente cadastrado com sucesso!")

print(Fore.MAGENTA + f"\n{'=' * 60}")
print(Fore.MAGENTA + f"{'DADOS DO CLIENTE':^60}")
print(Fore.MAGENTA + f"{'=' * 60}")

print(Fore.YELLOW + f"{'| Nome:' :<15}" + Fore.WHITE + f"| {nome_cliente}")
print(Fore.YELLOW + f"{'| E-mail:' :<15}" + Fore.WHITE + f"| {email_cliente}")
print(Fore.YELLOW + f"{'| Telefone:' :<15}" + Fore.WHITE + f"| {telefone_cliente}")
print(Fore.MAGENTA + f"{'=' * 60}")