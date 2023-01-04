from pokemons import listaPokemonsNivel1
from pokemons import listaPokemonsNivel2
from pokemons import listaPokemonsNivel3

# CONSTRUINDO O TREINADOR -----------------------------------------------------------------------------------------------------------------------------------------------------------
class Treinador: #CLASSE CONSTRUTORA DOS TREINADORES
    def __init__(self, listaPokemons):
        self.listaPokemons = listaPokemons
        
    def mostrarPokemons(self):  #METODO QUE MOSTRA TODOS OS POKEMONS QUE O JOGADOR TEM
     print("Seus pokemons são: ") 
     for i in range(len(self.listaPokemons)):
        print(f"Pokemon {i}: {self.listaPokemons[i].nome} | HP: {self.listaPokemons[i].hp} | Ataque: {self.listaPokemons[i].ataque} | Defesa: {self.listaPokemons[i].defesa}")


class Jogador(Treinador): #OBJETO QUE VAI HERDAR A LISTA DO PAI E ADICIONAR CARACTERISTICAS DE JOGADOR
    def __init__(self, listaPokemons, nome, experiencia):
        super().__init__(listaPokemons)
        self.nome = nome
        self.experiencia = experiencia



class Inimigo(Treinador):#OBJETO QUE VAI HERDAR A LISTA DO PAI E ADICIONAR CARACTERISTICAS DE INIMIGO
    def __init__(self, listaPokemons, nivel):
        super().__init__(listaPokemons)
        self.nivel = nivel
        
def adicionarPokemon(lista, pokemons, nivel): #FUNÇÃO PARA ADICIONAR POKEMONS A UMA LISTA
    print(nivel)
    if nivel <= 5:
        for pokemon in pokemons:
            lista.append(listaPokemonsNivel1[pokemon])
    elif nivel >=6 and nivel <=10:
        for pokemon in pokemons:
            lista.append(listaPokemonsNivel2[pokemon])
    elif nivel > 10:
        for pokemon in pokemons:
            lista.append(listaPokemonsNivel3[pokemon])
    return lista
