import random
from colorama import Fore, init


init(autoreset=True)

def adivinhacao():
    print(Fore.CYAN + "Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    adivinhado = False

    while not adivinhado:
        tentativa = input(Fore.YELLOW + "Adivinhe um número entre 1 e 100: ")
        
        
        if not tentativa.isdigit():
            print(Fore.RED + "Por favor, insira um número válido.")
            continue
        
        tentativa = int(tentativa)
        
        
        if tentativa < 1 or tentativa > 100:
            print(Fore.RED + "Número inválido. Tente números de 1 a 100.")
            continue
        
        tentativas += 1
        
        if tentativa < (numero_secreto - 5):
            print(Fore.BLUE + "Muito baixo! Tente novamente.")
        elif tentativa > (numero_secreto + 5):
            print(Fore.MAGENTA + "Muito alto! Tente novamente.")
        elif tentativa < numero_secreto:
            print(Fore.BLUE + "Tá quase, mas ainda tá baixo!")
        elif tentativa > numero_secreto:
            print(Fore.MAGENTA + "Tá quase, mas ainda tá alto!")
        else:
            adivinhado = True
            print(Fore.GREEN + f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")

if __name__ == "__main__":
    adivinhacao()
