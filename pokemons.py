import random


class Pokemons:
  def __init__(self, especie, nivel = None, hp = 100):
    self.especie = especie
    if nivel: 
      self.nivel = nivel
    else:
      self.nivel = random.randint(1, 100)
    self.hp = (hp + self.nivel) 

  def __str__(self):
    return f"{self.especie} (Level: {self.nivel} / HP: {self.hp})"

  def atacar(self, pokemon_atacado):
      print(f"{self.especie} atacou {pokemon_atacado.especie}!")

class PokemonEletrico(Pokemons):
  tipo = "Elétrico"
  def atacar(self, pokemon_atacado):
      self.dano_ataque = 10 + self.nivel
      print(f"{self.especie} atacou {pokemon_atacado.especie} com um choque do trovão! (Dano: -{self.dano_ataque})")
      pokemon_atacado.hp -= self.dano_ataque
      print(pokemon_atacado)

class PokemonFogo(Pokemons):
  tipo = "Fogo"
  def atacar(self, pokemon_atacado):
    self.dano_ataque = 10 + self.nivel
    print(f"{self.especie} atacou {pokemon_atacado.especie} com uma bola de fogo! (Dano: -{self.dano_ataque})")
    pokemon_atacado.hp -= self.dano_ataque
    print(pokemon_atacado)

class PokemonAgua(Pokemons):
  tipo = "Água"
  def atacar(self, pokemon_atacado):
    self.dano_ataque = 10 + self.nivel
    print(f"{self.especie} atacou {pokemon_atacado.especie} com um jato de água! (Dano: -{self.dano_ataque})")
    pokemon_atacado.hp -= self.dano_ataque
    print(pokemon_atacado)

class PokemonGrama(Pokemons):
  tipo = "Grama"
  def atacar(self, pokemon_atacado):
    self.dano_ataque = 10 + self.nivel
    print(f"{self.especie} atacou {pokemon_atacado.especie} com um chicote de cipó! (Dano: -{self.dano_ataque})")
    pokemon_atacado.hp -= self.dano_ataque
    print(pokemon_atacado)

