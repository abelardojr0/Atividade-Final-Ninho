from pokemons import listaPokemon
import random
class Treinador:
    def __init__(self, listaPokemons) :
        self.listaPokemons = listaPokemons
        
    
class Jogador(Treinador):
    def __init__(self, listaPokemons, nome):
        super().__init__(listaPokemons)
        self.nome = nome    
        self.pokemonsJogador = listaPokemons  
        
class Inimigo(Treinador):
    def __init__(self, listaPokemons, nivel):
        super().__init__(listaPokemons)
        self.nivel = nivel


def adicionarPokemon(lista, pokemons):
    for pokemon in pokemons:
        lista.append(listaPokemon[pokemon])
    return lista


lista1 = []
lista2 = []

pokemonsJogador = adicionarPokemon(lista1, [0,4,7])
pokemonsInimigo = adicionarPokemon(lista2, [random.randint(0,8), random.randint(0,8), random.randint(0,8)])

jogador1 = Jogador(pokemonsJogador, "Abel")
inimigo1 = Inimigo(pokemonsInimigo, 1)

# inimigo1.listarPokemons()

# for i in range(len(jogador1.listaPokemons)):
#     print(jogador1.listaPokemons[i].nome)