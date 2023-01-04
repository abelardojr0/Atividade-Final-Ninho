# FUNÇÃO DE BATALHAR CONTRA OUTRO TREINADOR-------------------------------------------------------------------------------------------------------------------------------------------
from batalha import batalhaPokemon  # IMPORTO A FUNÇÃO DE BATALHA


def duelar(jogador, inimigo):
    # VARIAVEL QUE VAI GUARDAR A LISTA DE POKEMONS DO JOGADOR
    listaPokemonsJogador = jogador.listaPokemons
    # VARIAVEL QUE VAI GUARDAR A LISTA DE POKEMONS DO INIMIGO
    listaPokemonsInimigo = inimigo.listaPokemons

    print("Lista de Pokemons do Jogador:")
    jogador.mostrarPokemons() #MOSTRAR POKEMONS DO JOGADOR
    pokemon1 = int(
        input("Escolha o pokemon do jogador digitando seu número: "))  # INPUT QUE VAI GUARDAR O POKEMON ESCOLHIDO PELO JOGADOR PARA A BATALHA
    print("\n")

    print("Lista de Pokemons do Inimigo:")
    inimigo.mostrarPokemons() #MOSTRAR POKEMONS DO INIMIGO
    pokemon2 = int(
        input("Escolha o pokemon do inimigo digitando seu número: "))  # INPUT QUE VAI GUARDAR O POKEMON ESCOLHIDO PELO INIMIGO PARA A BATALHA

    batalhaPokemon(listaPokemonsJogador[pokemon1],
                   listaPokemonsInimigo[pokemon2], "duelo", jogador)  # CHAMO A FUNÇÃO DE BATALHA E PASSO OS DADOS EM QUESTÃO NO CASO, O POKEMON ESCOLHIDO PELO JOGADOR, O POKEMON DO INIMIGO, O MODO DA BATALHA E O JOGADOR
