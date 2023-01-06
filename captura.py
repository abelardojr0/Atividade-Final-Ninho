# FUNÇÃO DE CAPTURAR UM POKEMON SELVAGEM--------------------------------------------------------------------------------------------------------------------------------------------
from batalha import batalhaPokemon  # IMPORTO A FUNÇÃO DE BATALHAR
from pokemons import listaPokemonsNivel1 #IMPORTO AS 3 LISTAS DE POKEMONS DE TODOS OS NÍVEIS
from pokemons import listaPokemonsNivel2
from pokemons import listaPokemonsNivel3

def capturar(jogador):
    print("Lista de Pokemons do Jogador:")
    jogador.mostrarPokemons() #MOSTRAR OS POKEMONS DO JOGADOR
    pokemonJogador = int(
        input("Escolha o pokemon do jogador digitando seu número: "))  # INPUT PARA SABER QUAL POKEMON O JOGADOR ESCOLHEU

    print("\n")


    print("Lista de pokemons selvagens disponiveis")
    if jogador.experiencia <=5:
        for i in range(len(listaPokemonsNivel1)):
            print(
            f" {i} Nome: {listaPokemonsNivel1[i].nome} | HP: {listaPokemonsNivel1[i].hp} | Ataque: {listaPokemonsNivel1[i].ataque} | Defesa: {listaPokemonsNivel1[i].defesa}")
    elif jogador.experiencia >=6 and jogador.experiencia <=10:
        for i in range(len(listaPokemonsNivel2)):
            print(
            f" {i} Nome: {listaPokemonsNivel2[i].nome} | HP: {listaPokemonsNivel2[i].hp} | Ataque: {listaPokemonsNivel2[i].ataque} | Defesa: {listaPokemonsNivel2[i].defesa}")
    elif jogador.experiencia > 10:
        for i in range(len(listaPokemonsNivel3)):
            print(
            f" {i} Nome: {listaPokemonsNivel3[i].nome} | HP: {listaPokemonsNivel3[i].hp} | Ataque: {listaPokemonsNivel3[i].ataque} | Defesa: {listaPokemonsNivel3[i].defesa}")
    pokemonSelvagem = int(
        input("Escolha o pokemon que quer capturar digitando seu número: "))  # INPUT QUE VAI SABER QUAL POKEMON SELVAGEM FOI ESCOLHIDO


# CHAMO A FUNÇÃO DE BATALHA E PASSO OS DADOS EM QUESTÃO NO CASO, O POKEMON ESCOLHIDO PELO JOGADOR, O POKEMON SELVAGEM ESCOLHIDO, O MODO DA BATALHA E O JOGADOR
    if jogador.experiencia <=5:
        batalhaPokemon(jogador.listaPokemons[pokemonJogador], listaPokemonsNivel1[pokemonSelvagem], "captura", jogador)
    elif jogador.experiencia >=6 and jogador.experiencia <=10:
        batalhaPokemon(jogador.listaPokemons[pokemonJogador], listaPokemonsNivel2[pokemonSelvagem], "captura", jogador)
    elif jogador.experiencia > 10:
        batalhaPokemon(jogador.listaPokemons[pokemonJogador], listaPokemonsNivel3[pokemonSelvagem], "captura", jogador) 
