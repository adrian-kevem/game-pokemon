import pickle
import os  # Importe o módulo os para verificar a existência do arquivo

from personagens import *
from pokemons import *

def salvar_jogo(jogador_1):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(jogador_1, arquivo)
    except Exception as error:
        print("Erro ao salvar o jogo!")
        print(error)

def carregar_jogo():
    if os.path.exists("database.db") and os.path.getsize("database.db") > 0:
        try:
            with open("database.db", "rb") as arquivo:
                jogador_1 = pickle.load(arquivo)
                print("Bem-vindo novamente ao Pokemon RPG!")
                return jogador_1
        except Exception as error:
            print("O jogo não foi carregado corretamente!")
            print(error)
    else:
        # Se o arquivo não existir ou estiver vazio, crie um novo jogador
        print("Bem-vindo ao Pokemon RPG: ")
        return Jogador(nome = input("Digite seu nome: "))

if __name__ == "__main__":
    jogador_1 = carregar_jogo()
    oponente_1 = Oponente()
    while True:
        print("\n0 - Sair")
        print("1 - Explorar")
        print("2 - Exibir Pokemons")
        print("3 - Exibir moedas")
        print("4 - Reiniciar progresso")
        opcao = int(input("Digite uma opção: "))
        if opcao == 0:
            salvar_jogo(jogador_1)
            break
        elif opcao == 1:
            jogador_1.explorar()
        elif opcao == 2:
            print("Seus pokemons são: ")
            jogador_1.mostrar_pokemons()
        elif opcao == 3:
            print(f"Você tem {jogador_1.moedas} moedas")
        elif opcao == 4:
            os.remove("database.db")
            break
        else:
            print("Opção inválida!")
        salvar_jogo(jogador_1)