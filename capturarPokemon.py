import random
from pokemons import listaPokemon
from treinador import jogador1
from batalha import batalhaPokemon

def capturar():
    print("Lista de Pokemons do Jogador:")
    for i in range(len(jogador1.listaPokemons)):
        print(f" {i} Nome: {jogador1.listaPokemons[i].nome} | HP: {jogador1.listaPokemons[i].hp} | Ataque: {jogador1.listaPokemons[i].ataque} | Defesa: {jogador1.listaPokemons[i].defesa}")

    print("\n")


    print("Lista de pokemons disponiveis")
    for i in range(len(listaPokemon)):
        print(f" {i} Nome: {listaPokemon[i].nome} | HP: {listaPokemon[i].hp} | Ataque: {listaPokemon[i].ataque} | Defesa: {listaPokemon[i].defesa}")

    pokemon1 = int(input("Escolha o pokemon do jogador digitando seu número: "))
    pokemon2 = int(input("Escolha o pokemon que quer capturar digitando seu número: "))


    batalhaPokemon(jogador1.listaPokemons[pokemon1],listaPokemon[pokemon2],"captura")

# for i in range(len(jogador1.listaPokemons)):
#     print(jogador1.listaPokemons[i].nome)
    