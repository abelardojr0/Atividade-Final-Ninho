import random  # IMPORTO A BIBLIOTECA RANDOM PARA GERAR NÚMEROS ALEATÓRIOS

# FUNÇÃO DE BATALHAR -----------------------------------------------------------------------------------------------------------------------------------------------------------


def batalhaPokemon(pokemonDoJogador, pokemonInimigo, modo, jogador):

    # FUNÇÃO QUE CHECA SE O POKEMON TEM VANTAGEM SOBRE SEU INIMIGO
    def checarVantagens(vantagens, inimigo):
        vantagem = False  # A VARIAVEL COMEÇA EM FALSE
        if (inimigo.tipo in vantagens):  # SE O TIPO DO POKEMON INIMIGO EXISTIR A LISTA DE VANTAGENS DO POKEMON ATUAL, ISSO QUER DIZER QUE O POKEMON ATUAL TEM VANTAGEM SOBRE ESSE INIMIGO, ENTÃO A VARIAVEL SE TORNA TRUE
            vantagem = True
        return vantagem

    [hpPokemonJogador, hpPokemonInimigo] = [
        pokemonDoJogador.hp, pokemonInimigo.hp] #ATRIBUO A VIDA DOS DOIS POKEMONS EM QUESTÃO A DUAS VARIAVEIS PARA PODER MANIPULALAS LIVREMENTE
    [acertosPokemonJogador, acertosPokemonInimigo] = [0, 0] #VARIAVEL CRIADA PARA CONTAR QUANTOS ACERTOS CADA POKEMON OBTEVE
    contRound = 1

    vantagemPokemonJogador = checarVantagens(
        pokemonDoJogador.vantagens, pokemonInimigo) #VARIAVEL BOOLEANA QUE VAI REVIRIFICAR SE O POKEMON DO JOGADOR POSSUI VANTAGEM SOBRE O DO INIMIGO
    vantagemPokemonInimigo = checarVantagens(
        pokemonInimigo.vantagens, pokemonDoJogador) #VARIAVEL BOOLEANA QUE VAI REVIRIFICAR SE O POKEMON DO INIMIGO POSSUI VANTAGEM SOBRE O DO JOGADOR
    
    [modificadorVantagemPokemonJogador,modificadorVantagemPokemonInimigo ] = [0,0] #VARIAVEIS QUE VÃO RECEBER O MODIFICAR QUE VAI SER ADICIONADO NO DANO CASO O POKEMON TENHA VANTAGEM.

    if (vantagemPokemonJogador): #SE A VANTAGEM FOR TRUE...
        modificadorVantagemPokemonJogador = 10
    if (vantagemPokemonInimigo):
        modificadorVantagemPokemonInimigo = 10

    while hpPokemonJogador > 0 and hpPokemonInimigo > 0: #LOOP QUE VAI FAZER A BATALHA ACONTECER ENQUANTO TIVER UM POKEMON VIVO.

        [tentativaPokemonJogador, tentativaPokemonInimigo] = [random.random() - 0.5, random.random() - 0.5] #VARIÁVEIS QUE VÃO ARMAZENAR UM NÚMERO ALETÓRIO ENTRE 0 E 1 E DIMINUIR 0.5, GERANDO 50% DE CHANCE DE ACERTO PARA CADA TENTATIVA DE ATAQUE DE CADA POKEMON

        if (tentativaPokemonJogador > 0 and hpPokemonJogador > 0): # SE A TENTATIVA FOI BEM SUCEDIDA E O POKEMON ESTÁ VIVO ENTÃO...
            hpPokemonInimigo -= (pokemonDoJogador.ataque - (
                pokemonInimigo.defesa * 0.65)) + modificadorVantagemPokemonJogador #A VIDA DO INIMIGO É DIMINUIDA PELA FÓRMULA DESCRITA
            acertosPokemonJogador += 1

        if (tentativaPokemonInimigo > 0 and hpPokemonInimigo > 0):
            hpPokemonJogador -= (pokemonInimigo.ataque - (
                pokemonDoJogador.defesa * 0.65)) + modificadorVantagemPokemonInimigo
            acertosPokemonInimigo += 1

        print(f"""
              Round {contRound}
              {pokemonDoJogador.nome} acertou um total de {acertosPokemonJogador} ataques
              {pokemonInimigo.nome} acertou um total de {acertosPokemonInimigo} ataques
              Vida do {pokemonDoJogador.nome} = {round(hpPokemonJogador, 2)}
              Vida do {pokemonInimigo.nome} = {round(hpPokemonInimigo, 2)}""") #STATUS DE CADA RODADA DE BATALHA

        contRound += 1

    if (hpPokemonJogador <= 0 and hpPokemonInimigo > hpPokemonJogador):#CHECA SE O POKEMON DO INIMIGO GANHOU
        print(f"{pokemonInimigo.nome} ganhou de {pokemonDoJogador.nome} e sobrou {round(hpPokemonInimigo, 2)} pontos de vida")
    elif (hpPokemonInimigo <= 0 and hpPokemonJogador > hpPokemonInimigo):#CHECA SE O POKEMON DO JOGADOR GANHOU
        print(f"{pokemonDoJogador.nome} ganhou de {pokemonInimigo.nome}  e sobrou {round(hpPokemonJogador, 2)} pontos de vida")
        if (modo == "captura"): #SE TIVER GANHO E TIVER NO MODO CAPTURA ENTÃO..
            print(f"{pokemonInimigo.nome} foi caturado") #PRINTA UMA MENSAGEM 
            jogador.listaPokemons.append(pokemonInimigo) #ADICIONA O POKEMON CAPTURA NA LISTA DE POKEMONS DO JOGADOR
        elif (modo == "duelo"): #SE FOR MODO DUELO
            jogador.experiencia += 1 #O JOGADOR GANHA XP
    else: #SE NÃO EM CASOS RAROS, ELES EMPATAM
        print("Os pokemons empataram")
