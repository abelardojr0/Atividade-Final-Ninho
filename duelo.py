# FUNÇÃO DE BATALHAR CONTRA OUTRO TREINADOR-------------------------------------------------------------------------------------------------------------------------------------------
from batalha import batalhaPokemon  # IMPORTO A FUNÇÃO DE BATALHA


def duelar(jogador, inimigo):
    # VARIAVEL QUE VAI GUARDAR A LISTA DE POKEMONS DO JOGADOR
    listaPokemonsJogador = jogador.listaPokemons
    # VARIAVEL QUE VAI GUARDAR A LISTA DE POKEMONS DO INIMIGO
    listaPokemonsInimigo = inimigo.listaPokemons

    print("Lista de Pokemons do Jogador:")
    for i in range(len(listaPokemonsJogador)):  # LOOP POR TODOS OS POKEMONS DO JOGADOR
        print(
            f" {i} Nome: {listaPokemonsJogador[i].nome} | HP: {listaPokemonsJogador[i].hp} | Ataque: {listaPokemonsJogador[i].ataque} | Defesa: {listaPokemonsJogador[i].defesa}")
    pokemon1 = int(
        input("Escolha o pokemon do jogador digitando seu número: "))  # INPUT QUE VAI GUARDAR O POKEMON ESCOLHIDO PELO JOGADOR PARA A BATALHA
    print("\n")

    print("Lista de Pokemons do Inimigo:")
    for i in range(len(listaPokemonsInimigo)):  # LOOP POR TODOS OS POKEMONS DO INIMIGO
        print(
            f" {i} Nome: {listaPokemonsInimigo[i].nome} | HP: {listaPokemonsInimigo[i].hp} | Ataque: {listaPokemonsInimigo[i].ataque} | Defesa: {listaPokemonsInimigo[i].defesa}")
    pokemon2 = int(
        input("Escolha o pokemon do inimigo digitando seu número: "))  # INPUT QUE VAI GUARDAR O POKEMON ESCOLHIDO PELO INIMIGO PARA A BATALHA

    batalhaPokemon(listaPokemonsJogador[pokemon1],
                   listaPokemonsInimigo[pokemon2], "duelo", jogador)  # CHAMO A FUNÇÃO DE BATALHA E PASSO OS DADOS EM QUESTÃO NO CASO, O POKEMON ESCOLHIDO PELO JOGADOR, O POKEMON DO INIMIGO, O MODO DA BATALHA E O JOGADOR
