from pokemons import listaPokemon  # IMPORTO A LISTA DE POKEMONS
from duelo import duelar  # IMPORTO A FUNÇÃO DE DUELAR
from capturarPokemon import capturar  # IMPORTO A FUNÇÃO DE CAPTURAR
import random #IMPORO A BIBLIOTECA RANDOM

# CONSTRUINDO O TREINADOR -----------------------------------------------------------------------------------------------------------------------------------------------------------


class Treinador: #CLASSE CONSTRUTORA DOS TREINADORES
    def __init__(self, listaPokemons):
        self.listaPokemons = listaPokemons


class Jogador(Treinador): #OBJETO QUE VAI HERDAR A LISTA DO PAI E ADICIONAR CARACTERISTICAS DE JOGADOR
    def __init__(self, listaPokemons, nome, experiencia):
        super().__init__(listaPokemons)
        self.nome = nome
        self.experiencia = experiencia
        self.pokemonsJogador = listaPokemons

    def mostrarPokemons(self):  #METODO QUE MOSTRA TODOS OS POKEMONS QUE O JOGADOR TEM
        for i in range(len(self.pokemonsJogador)):
            print(f"Pokemon {i+1}: {self.pokemonsJogador[i].nome}")


class Inimigo(Treinador):#OBJETO QUE VAI HERDAR A LISTA DO PAI E ADICIONAR CARACTERISTICAS DE INIMIGO
    def __init__(self, listaPokemons, nivel):
        super().__init__(listaPokemons)
        self.nivel = nivel


def adicionarPokemon(lista, pokemons): #FUNÇÃO PARA ADICIONAR POKEMONS A UMA LISTA
    for pokemon in pokemons:
        lista.append(listaPokemon[pokemon])
    return lista


listaPokemonsInimigo = [] #ARRAY VAZIO QUE VAI SER PASSADO PARA SER PREENCHIDO
pokemonsInimigo = adicionarPokemon(
    listaPokemonsInimigo, [random.randint(0, 54), random.randint(0, 54), random.randint(0, 54)]) #CHAMANDO A FUNÇÃO ADICIONANDO 3 POKEMONS ALEATÓRIOS
inimigo = Inimigo(pokemonsInimigo, 1) #CRIANDO O INIMIGO COM A SUA LISTA DE POKEMONS E SEU NÍVEL


def cadastrarJogador(lista, nome, nivel): #CADASTRADOR DE JOGADOR
    global jogador #DECLARO A VARIAVEL COMO GLOBAL PARA QUE EU CONSIGA ACESSAR DE FORA DA FUNÇÃO
    listaPokemonsJogador = [] #ARRAY VAZIO QUE VAI SER PASSADO PARA SER PREENCHIDO
    pokemonsJogador = adicionarPokemon(listaPokemonsJogador, lista)  #CHAMANDO A FUNÇÃO ADICIONANDO OS POKEMONS ESCOLHIDOS PELO JOGADOR.
    jogador = Jogador(pokemonsJogador, nome, nivel) #CRIANDO O JOGADOR COM SUA LISTA DE POKEMONS, SEU NOME E SEU NÍVEL.

# COMEÇANDO O JOGO -----------------------------------------------------------------------------------------------------------------------------------------------------------


print("Bem vinda a Kanto!")

nomeJogador = input("Digite seu nome: ")

print("Escolha 3 pokemons!")

print(f"""
      1: {listaPokemon[0].nome}
      2: {listaPokemon[3].nome}
      3: {listaPokemon[6].nome}
      4: {listaPokemon[9].nome}
      5: {listaPokemon[12].nome}
      6: {listaPokemon[15].nome}
      7: {listaPokemon[18].nome}
      8: {listaPokemon[20].nome}
      9: {listaPokemon[22].nome}
      10: {listaPokemon[24].nome}\n""") #LISTA DE POKEMONS INICIAIS DISPONÍVEIS

pokemon1 = int(input("Escolha seu primeiro pokemon, digitando seu número: ")) #CAPTURANDO QUAL POKEMON FOI ESCOLHIDO
#TRANSFORMANDO OS NÚMEROS DE ESCOLHA DOS POKEMONS EM SEUS RESPECTIVOS NÚMEROS DE ARRAY.
numeroPokemon1 = 0 
if pokemon1 == 1: 
    numeroPokemon1 = 0
elif pokemon1 == 2:
    numeroPokemon1 = 3
elif pokemon1 == 3:
    numeroPokemon1 = 6
elif pokemon1 == 4:
    numeroPokemon1 = 9
elif pokemon1 == 5:
    numeroPokemon1 = 12
elif pokemon1 == 6:
    numeroPokemon1 = 15
elif pokemon1 == 7:
    numeroPokemon1 = 18
elif pokemon1 == 8:
    numeroPokemon1 = 20
elif pokemon1 == 9:
    numeroPokemon1 = 22
elif pokemon1 == 10:
    numeroPokemon1 = 24

pokemon2 = int(input("Escolha seu segundo pokemon, digitando seu número: "))
numeroPokemon2 = 0
if pokemon2 == 1:
    numeroPokemon2 = 0
elif pokemon2 == 2:
    numeroPokemon2 = 3
elif pokemon2 == 3:
    numeroPokemon2 = 6
elif pokemon2 == 4:
    numeroPokemon2 = 9
elif pokemon2 == 5:
    numeroPokemon2 = 12
elif pokemon2 == 6:
    numeroPokemon2 = 15
elif pokemon2 == 7:
    numeroPokemon2 = 18
elif pokemon2 == 8:
    numeroPokemon2 = 20
elif pokemon2 == 9:
    numeroPokemon2 = 22
elif pokemon2 == 10:
    numeroPokemon2 = 24

pokemon3 = int(input("Escolha seu terceiro pokemon, digitando seu número: "))
numeroPokemon3 = 0
if pokemon3 == 1:
    numeroPokemon3 = 0
elif pokemon3 == 2:
    numeroPokemon3 = 3
elif pokemon3 == 3:
    numeroPokemon3 = 6
elif pokemon3 == 4:
    numeroPokemon3 = 9
elif pokemon3 == 5:
    numeroPokemon3 = 12
elif pokemon3 == 6:
    numeroPokemon3 = 15
elif pokemon3 == 7:
    numeroPokemon3 = 18
elif pokemon3 == 8:
    numeroPokemon3 = 20
elif pokemon3 == 9:
    numeroPokemon3 = 22
elif pokemon3 == 10:
    numeroPokemon3 = 24

cadastrarJogador([numeroPokemon1, numeroPokemon2,
                 numeroPokemon3], nomeJogador, 1) #CADASTRANDO O JOGADOR COM OS POKEMONS ESCOLHIDOS E O NICKNAME ESCOLHIDO.

print("Menu")
print(f"O que você deseja fazer agora {nomeJogador}?")
escolhaMenu = input(f"""
    1- Capturar Pokemon
    2- Exibir Pokemons
    3- Buscar Batalha
    0 - Sair\n""")


while (escolhaMenu != "0"): #LOOP QUE VAI DEIXAR O JOGADOR DENTRO DO JOGO ATÉ QUE ELE DECIDA SAIR.

    print("Menu")
    print(f"O que você deseja fazer agora {nomeJogador}?")
    escolhaMenu = input(f"""
        1 - Capturar Pokemon
        2 - Exibir Pokemons
        3 - Buscar Batalha
        4 - Consultar Experiência
        0 - Sair\n""")

    if (escolhaMenu == "1"):
        capturar(jogador) #CHAMA A FUNÇÃO DE CAPTURAR E PASSA O JOGADOR ATUAL COMO PARÂMETRO
    elif (escolhaMenu == "2"):
        jogador.mostrarPokemons() #CHAMA O MÉTODO DE JOGADOR DE MOSTRAR SEUS POKEMONS
    elif (escolhaMenu == "3"):
        duelar(jogador, inimigo) #CHAMA A FUNÇÃO DE DUELAR E PASSA O JOGADOR ATUAL E O INIMIGO COMO PARÂMETRO
    elif (escolhaMenu == "4"):
        print(f"Sua experiência atual é: {jogador.experiencia}") #MOSTRA A EXPERIÊNCIA ATUAL DO JOGADOR.
