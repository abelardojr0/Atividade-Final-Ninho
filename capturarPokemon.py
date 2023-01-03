# FUNÇÃO DE CAPTURAR UM POKEMON SELVAGEM--------------------------------------------------------------------------------------------------------------------------------------------
from batalha import batalhaPokemon  # IMPORTO A FUNÇÃO DE BATALHAR
from pokemons import listaPokemon  # IMPORTO A LISTA COM TODOS OS POKEMONS


def capturar(jogador):
    print("Lista de Pokemons do Jogador:")
    # LOOP QUE VAI MOSTRAR TODOS OS POKEMONS DO JOGADOR
    for i in range(len(jogador.listaPokemons)):
        print(
            f" {i} Nome: {jogador.listaPokemons[i].nome} | HP: {jogador.listaPokemons[i].hp} | Ataque: {jogador.listaPokemons[i].ataque} | Defesa: {jogador.listaPokemons[i].defesa}")

    pokemon1 = int(
        input("Escolha o pokemon do jogador digitando seu número: "))  # INPUT PARA SABER QUAL POKEMON O JOGADOR ESCOLHEU

    print("\n")

    print("Lista de pokemons disponiveis")
    for i in range(len(listaPokemon)):  # LOOP QUE VAI MOSTRAR TODOS OS POKEMONS SELVAGENS
        print(
            f" {i} Nome: {listaPokemon[i].nome} | HP: {listaPokemon[i].hp} | Ataque: {listaPokemon[i].ataque} | Defesa: {listaPokemon[i].defesa}")
    pokemon2 = int(
        input("Escolha o pokemon que quer capturar digitando seu número: "))  # INPUT QUE VAI SABER QUAL POKEMON SELVAGEM FOI ESCOLHIDO

    batalhaPokemon(
        jogador.listaPokemons[pokemon1], listaPokemon[pokemon2], "captura", jogador)  # CHAMO A FUNÇÃO DE BATALHA E PASSO OS DADOS EM QUESTÃO NO CASO, O POKEMON ESCOLHIDO PELO JOGADOR, O POKEMON SELVAGEM ESCOLHIDO, O MODO DA BATALHA E O JOGADOR
