import random
from treinador import jogador1
from treinador import inimigo1


def batalhaPokemon(pokemonDoJogador, pokemonInimigo, modo):
    
    def checarVantagens(vantagens, inimigo):
        vantagem = False
        if(inimigo.tipo in vantagens):
            vantagem = True
        return vantagem
    
    [hpPokemonJogador,hpPokemonInimigo] = [pokemonDoJogador.hp, pokemonInimigo.hp]
    [acertosPokemonJogador, acertosPokemonInimigo] = [0,0]
    contRound = 1
    
    vantagemPokemonJogador = checarVantagens(pokemonDoJogador.vantagens, pokemonInimigo)
    vantagemPokemonInimigo = checarVantagens(pokemonInimigo.vantagens, pokemonDoJogador)
    modificadorVantagemPokemonJogador = 0
    modificadorVantagemPokemonInimigo = 0
    
    if(vantagemPokemonJogador):
        modificadorVantagemPokemonJogador = 10
    if(vantagemPokemonInimigo):
        modificadorVantagemPokemonInimigo = 10

    while hpPokemonJogador > 0 and hpPokemonInimigo > 0:
        
        [tentativa1, tentativa2] = [random.random() - 0.5, random.random() - 0.5]
            
        if(tentativa1 > 0 and hpPokemonJogador > 0):
            hpPokemonInimigo -= (pokemonDoJogador.ataque  - (pokemonInimigo.defesa * 0.65)) + modificadorVantagemPokemonJogador
            acertosPokemonJogador+=1

                
        if(tentativa2 > 0 and hpPokemonInimigo > 0):
            hpPokemonJogador -= (pokemonInimigo.ataque  - (pokemonDoJogador.defesa * 0.65)) + modificadorVantagemPokemonInimigo
            acertosPokemonInimigo+=1
            
        print(f"""
              Round {contRound}
              {pokemonDoJogador.nome} acertou {acertosPokemonJogador} ataques
              {pokemonInimigo.nome} acertou {acertosPokemonInimigo} ataques
              Vida do {pokemonDoJogador.nome} = {round(hpPokemonJogador, 2)}
              Vida do {pokemonInimigo.nome} = {round(hpPokemonInimigo, 2)}""")
        
        contRound += 1
        
    if(hpPokemonJogador <= 0 and hpPokemonInimigo > hpPokemonJogador):
        print(f"{pokemonInimigo.nome} ganhou de {pokemonDoJogador.nome} e sobrou {round(hpPokemonInimigo, 2)} pontos de vida")
    elif(hpPokemonInimigo <= 0 and hpPokemonJogador > hpPokemonInimigo):
        print(f"{pokemonDoJogador.nome} ganhou de {pokemonInimigo.nome}  e sobrou {round(hpPokemonJogador, 2)} pontos de vida")
        if(modo == "captura"):
            print(f"{pokemonInimigo.nome} foi caturado")
            jogador1.listaPokemons.append(pokemonInimigo)
    else:
        print("Os pokemons empataram")
        
        
    print(f"O {pokemonDoJogador.nome} acertou {acertosPokemonJogador} ataques")
    print(f"O {pokemonInimigo.nome} acertou {acertosPokemonInimigo} ataques")
        
        
    

if __name__ == "__main__":
    
    print("Lista de Pokemons do Jogador:")
    for i in range(len(jogador1.listaPokemons)):
        print(f" {i} Nome: {jogador1.listaPokemons[i].nome} | HP: {jogador1.listaPokemons[i].hp} | Ataque: {jogador1.listaPokemons[i].ataque} | Defesa: {jogador1.listaPokemons[i].defesa}")

    print("\n")

    print("Lista de Pokemons do Inimigo:")
    for i in range(len(inimigo1.listaPokemons)):
        print(f" {i} Nome: {inimigo1.listaPokemons[i].nome} | HP: {inimigo1.listaPokemons[i].hp} | Ataque: {inimigo1.listaPokemons[i].ataque} | Defesa: {inimigo1.listaPokemons[i].defesa}")


    pokemon1 = int(input("Escolha o pokemon do jogador digitando seu número: "))
    pokemon2 = int(input("Escolha o pokemon do inimigo digitando seu número: "))

    batalhaPokemon(jogador1.listaPokemons[pokemon1],inimigo1.listaPokemons[pokemon2], "batalha")