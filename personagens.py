import random


from pokemons import *


lista_nomes = ["John", "Mary", "James", "Jennifer", "Robert", "Susan", "Michael", "Linda", "William", "Karen"]
lista_pokemons = [PokemonGrama("Bulbasaur"), PokemonEletrico("Pikachu"), PokemonFogo("Charmander"), PokemonAgua("Squartle")]

class Personagens:
  def __init__(self, nome = None, pokemons = []):
    if nome:
      self.nome = nome
    else:
      self.nome = random.choice(lista_nomes)
    self.pokemons = pokemons

  def __str__(self):
    return f"Nome: {self.nome}"

  def mostrar_pokemons(self):
    if self.pokemons:
      for indice, pokemon in enumerate(self.pokemons, start = 0):
          print(f"{indice} - {pokemon}")
    else: 
      print(f"{self.nome} não possui nenhum pokemom!")

  def ganhar_moedas(self, quantidade):
    self.moedas += quantidade
    print("Você ganhou 50 moedas!")

  def perder_moedas(self, quantidade):
    self.moedas -= quantidade
    print("Você perdeu 50 moedas!")

  def batalhar(self, oponente):
    print(f"{self.nome} iniciou uma batalha com {oponente.nome}")
    print("\nPokemons do Oponente:")
    oponente.mostrar_pokemons()
    print("\nSeus Pokemons: ")
    self.mostrar_pokemons()  
    pokemon_escolhido_jogador = None
    while True:
      try:
        escolha = int(input("\nEscolha um pokemon para a batalha: "))
        pokemon_escolhido_jogador = self.pokemons[escolha]
        break
      except:
        print("Opção inválida!")
    print(f"\nPokemon escolhido por você: {pokemon_escolhido_jogador}")
    pokemon_escolhido_oponente = random.choice(oponente.pokemons)
    print(f"\nPokemon escolhido pelo oponente: {pokemon_escolhido_oponente}\n")
    if pokemon_escolhido_jogador and pokemon_escolhido_oponente:
      while True:
        pokemon_escolhido_jogador.atacar(pokemon_escolhido_oponente)
        if (pokemon_escolhido_jogador.hp <= 0):
          print(f"O pokemon {pokemon_escolhido_oponente.especie} de {oponente.nome} é o vencedor!")
          self.perder_moedas(50)
          break
        elif (pokemon_escolhido_oponente.hp <= 0):
          print(f"O pokemon {pokemon_escolhido_jogador.especie} de {self.nome} é o vencedor!")
          self.ganhar_moedas(50)
          break
        pokemon_escolhido_oponente.atacar(pokemon_escolhido_jogador)
        if (pokemon_escolhido_jogador.hp <= 0):
          print(f"O pokemon {pokemon_escolhido_oponente.especie} de {oponente.nome} é o vencedor!")
          self.perder_moedas(50)
          break
        elif (pokemon_escolhido_oponente.hp <= 0):
          print(f"O pokemon {pokemon_escolhido_jogador.especie} de {self.nome} é o vencedor!")
          self.ganhar_moedas(50)
          break
    else:
      print("Essa batalha não pode ocorrer!")

class Jogador(Personagens):
  def __init__(self, nome = None, pokemons = [], moedas = 100):
    if not pokemons: 
      pokemon_escolhido = random.choice(lista_pokemons)
      if pokemon_escolhido is not lista_pokemons:
        pokemons.append(pokemon_escolhido)
      print(f"Você irá iniciar sua jornada com um {pokemons[0]}!")
    self.moedas = moedas
    super().__init__(nome = nome, pokemons = pokemons)
  
  def __str__(self):
    return f"Nome: {self.nome} ({self.moedas} moedas)"

  def capturar_pokemon(self, pokemon_capturado):
    self.pokemons.append(pokemon_capturado)
    print(f"\n{pokemon_capturado.especie} capturado!\n")

  def explorar(self):
    probabilidades_exploratorias = random.random()
    if probabilidades_exploratorias <= 0.20:
      pokemon_selvagem = random.choice(lista_pokemons)
      opcao = input(f"Você encontrou um {pokemon_selvagem} selvagem, deseja capturá-lo? (1 - Sim / 2 - Não) ")
      if opcao == "1":
        self.capturar_pokemon(pokemon_selvagem)
        print("Meus pokemons: ")
        self.mostrar_pokemons()
      elif opcao == "2":
        pass
    elif probabilidades_exploratorias > 0.20 and probabilidades_exploratorias <= 40:
      oponente_1 = Oponente()
      opcao = input(f"Você foi desafiado por {oponente_1.nome}, deseja combatê-lo? (1 - Sim / 2 - Não) ")
      if opcao == "1":
        self.batalhar(oponente_1)
      elif opcao == "2":
        print("Você recusou o desafio!")
    else:
      print("A exploração não resultou em nada!")

class Oponente(Personagens):
  def __init__(self, nome = None, pokemons = []):
    if not pokemons:
      for i in range(random.randint(1, 3)): 
        pokemon_escolhido = random.choice(lista_pokemons)
        if pokemon_escolhido is not lista_pokemons:
          pokemons.append(pokemon_escolhido)
    super().__init__(nome = None, pokemons = pokemons)
 