from pokemons import listaPokemon  # IMPORTO A LISTA DE POKEMONS
from duelo import duelar  # IMPORTO A FUNÇÃO DE DUELAR
from capturarPokemon import capturar  # IMPORTO A FUNÇÃO DE CAPTURAR
import random #IMPORO A BIBLIOTECA RANDOM
from pokemons import listaPokemonsNivel1
from pokemons import listaPokemonsNivel2
from pokemons import listaPokemonsNivel3
import os

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


def cadastrarJogador(lista, nome, nivel): #CADASTRADOR DE JOGADOR
    global jogador #DECLARO A VARIAVEL COMO GLOBAL PARA QUE EU CONSIGA ACESSAR DE FORA DA FUNÇÃO
    listaPokemonsJogador = [] #ARRAY VAZIO QUE VAI SER PASSADO PARA SER PREENCHIDO
    pokemonsJogador = adicionarPokemon(listaPokemonsJogador, lista, nivel)  #CHAMANDO A FUNÇÃO ADICIONANDO OS POKEMONS ESCOLHIDOS PELO JOGADOR.
    jogador = Jogador(pokemonsJogador, nome, nivel) #CRIANDO O JOGADOR COM SUA LISTA DE POKEMONS, SEU NOME E SEU NÍVEL.
    

# COMEÇANDO O JOGO -----------------------------------------------------------------------------------------------------------------------------------------------------------


print("Bem vinda a Kanto!")

nomeJogador = input("Digite seu nome: ")

print("Escolha 3 pokemons!")

for i in range(len(listaPokemonsNivel1)): #LISTANDO AS OPÇÕES INICIAIS
    print(f"{i}: {listaPokemonsNivel1[i].nome}")


pokemonsEscolhidos = []
for i in range(3): #CAPTURANDO AS ESCOLHAS
    opcao = int(input(f"Escolha seu {i+1} pokemon, digitando seu número: "))
    pokemonsEscolhidos.append(opcao)
    
cadastrarJogador(pokemonsEscolhidos, nomeJogador, 1) #CADASTRANDO O JOGADOR COM OS POKEMONS ESCOLHIDOS E O NICKNAME ESCOLHIDO.

listaPokemonsInimigo = [] #ARRAY VAZIO QUE VAI SER PASSADO PARA SER PREENCHIDO
fim = 0
if(jogador.experiencia < 10):
    fim = 23
else:
    fim = 9
pokemonsInimigo = adicionarPokemon(
    listaPokemonsInimigo, [random.randint(0, fim), random.randint(0, fim), random.randint(0, fim)], jogador.experiencia) #CHAMANDO A FUNÇÃO ADICIONANDO 3 POKEMONS ALEATÓRIOS
inimigo = Inimigo(pokemonsInimigo, jogador.experiencia) #CRIANDO O INIMIGO COM A SUA LISTA DE POKEMONS E SEU NÍVEL


escolhaMenu = ""
while (escolhaMenu != "0"): #LOOP QUE VAI DEIXAR O JOGADOR DENTRO DO JOGO ATÉ QUE ELE DECIDA SAIR.
    print("Menu")
    print(f"O que você deseja fazer agora {nomeJogador}?")
    escolhaMenu = input(f"""
        1 - Capturar Pokemon
        2 - Exibir Pokemons
        3 - Buscar Batalha
        4 - Consultar Experiência
        0 - Sair\n""")
    os.system("cls") or None
    
    if (escolhaMenu == "1"):
        capturar(jogador) #CHAMA A FUNÇÃO DE CAPTURAR E PASSA O JOGADOR ATUAL COMO PARÂMETRO
    elif (escolhaMenu == "2"):
        jogador.mostrarPokemons() #CHAMA O MÉTODO DE JOGADOR DE MOSTRAR SEUS POKEMONS
    elif (escolhaMenu == "3"):
        duelar(jogador, inimigo) #CHAMA A FUNÇÃO DE DUELAR E PASSA O JOGADOR ATUAL E O INIMIGO COMO PARÂMETRO
    elif (escolhaMenu == "4"):
        print(f"Sua experiência atual é: {jogador.experiencia}") #MOSTRA A EXPERIÊNCIA ATUAL DO JOGADOR.
