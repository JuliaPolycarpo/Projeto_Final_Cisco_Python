import random 
import time 

# Atribuindo o que cada jogador vai ser no tabuleiro
computador = "X"
usuario = "O"

# Cria o tabuleiro inicial e define as posições de cada espaço.
# Três listas diferentes, pois cada uma representa uma linha do tabuleiro.
def posiçoes_tabuleiro():
    return [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']]


# Mostra o tabuleiro na tela.
def mostrar_tabuleiro(tabuleiro):
    print('+-------+-------+-------+') 
    for linha in tabuleiro:
        print('|       |       |       |')
        print(f'|   {linha[0]}   |   {linha[1]}   |   {linha[2]}   |') # Coloca cada item das listas presentes na função "posiçoes_tabuleiro" ao centro do quadrado.
        print('|       |       |       |')
        print('+-------+-------+-------+') # Imprime a divisoria no final de cada lista/linha impressa na tela.


def iniciar_jogo():
    print("O jogo será iniciado em:")
    print("3")
    time.sleep(0.5) # Usei para causar um "delay" na contagem regressiva e deixar o jogo mais dinâmico.
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("Vamos começar!")
   

def primeiro_movimmento(tabuleiro):
    tabuleiro[1][1] = computador # Coloca o primeiro movimento do computador ao centro do tabuleiro, na segunda lista de "posiçoes_tabuleiro" e no elemento de indice 1 (segundo elemento) da mesma lista.

def movimento_jogador(tabuleiro):
    while True:
        posiçao = input("Selecione uma casa vazia para ocupar: ")# Se colocar "int(input)" não funciona, pois o a def "posiçoes_tabuleiro" armazena strings.

        # Verifica o que o usuario digitou.
        if posiçao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: # Se colocar os valores sem os parenteses não funciona, pois são strings e não números e se tentar colocar a função "posiçoes_tabuleiro" tambem não funciona
            print("Somente números no intevalo de 1 a 9 são aceitos.\nTente novamente:") 
            continue 

        # Verifica se a posição está disponivel 
        for linha in range(3): # Vê a linha do tabuleiro
            for coluna in range(3): # Vê a coluna do tabuleiro 
                if tabuleiro[linha][coluna] == posiçao: # Verifica se os indices representados pelo numero digitado pelo usario estão vazios
                    tabuleiro[linha][coluna] = usuario
                    return
        # Caso as condições do "for" não forem atentidas, o codigo ira imprimir:         
        print("Essa posição já foi ocupada.\nFaça sua jogada em uma posição vazia:")       


def movimento_computador(tabuleiro):
    print("O computador está pensando em sua jogada...")    
    while True: 
        posiçao = str(random.randint (1, 9)) # Faz com que o computador escolha um número aleatorio de 1 a 9 e se não converter para string o codigo não funicona e dá erro, pois na def "posiçoes_tabuleiros" armazena strings.

        # Verifica se a posição está disponivel 
        for linha in range(3): # Vê a linha do tabuleiro
            for coluna in range(3): # Vê a coluna do tabuleiro 
                if tabuleiro[linha][coluna] == posiçao: # Verifica se os indices representados pelo numero digitado pelo usario estão vazios
                    tabuleiro[linha][coluna] = computador
                    return

        # Caso as condições do "for" não forem atentidas, o codigo ira imprimir:      
        # Removi isso pois fica muito feio e confuso ao decorrer do jogo   
        #print("O computador escolheu uma posição já ocupada.\nEle fará outra jogada em uma posição vazia:") 


def verificacao(tabuleiro):
    # Verificar as linhas 
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2]:
            print(f"O jogador {linha[0]} é o vencedor!")
            #return linha [0]]
            exit() # Ao inves de usar o return, uso o exit, para que o resultado seja impresso na tela e não armazenado.
        

    # Verifica as colunas 
    for coluna in range(3): # Se colocar "tabuleiro" não funciona pois os indices da lista precisam ser numeros inteiros e não listas
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            print(f"O jogador {tabuleiro[0][coluna]} é o vencedor!")
            #return tabuleiro[0][coluna]
            exit()

    # Verifica as diagonais 
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        print(f"O jogador {tabuleiro[0][0]} é o vencedor!")
        #return tabuleiro[0][0]
        exit()
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        print(f"O jogador {tabuleiro[0][2]} é o vencedor!")
        #return tabuleiro[0][2]  
        exit()
    
    # Verifica se é empate ou não
    for linha in tabuleiro:
        for quadrado in linha:
            if quadrado not in (usuario, computador):
                return None # Se tiver algum quadrado vazio, o jogo continuará
   # Caso as condições do "for" não forem atentidas, o codigo ira imprimir:         
    #return "Empate :("
    print("Empate :(")
    exit()
        


# 1° Jogada - Computador
iniciar_jogo()
tabuleiro = posiçoes_tabuleiro() # Para fazer as duas funções trabalharem juntas tive que atribuir a variavel "tabuleiro" as posições do tabuleiro.
primeiro_movimmento(tabuleiro)
mostrar_tabuleiro(tabuleiro)

# 2° Jogada - Usuario
print("\033[1mATENÇÂO\033[0m: O computador já realizou o seu movimeto") # Deixei o "atenção" em negrito.
movimento_jogador(tabuleiro)
mostrar_tabuleiro(tabuleiro) # Colocar o tabuleiro para imprimir apos cada jogada
verificacao(tabuleiro)

# 3° Jogada - Computador 
movimento_computador(tabuleiro)
time.sleep(1.0) # para a transição entre o usuario e computador ficar mais clara
mostrar_tabuleiro(tabuleiro)
verificacao(tabuleiro)

# 4° Jogada - Usuario 
movimento_jogador(tabuleiro)
mostrar_tabuleiro(tabuleiro) # Colocar o tabuleiro para imprimir apos cada jogada
verificacao(tabuleiro)

# 5° Jogada - Computador 
movimento_computador(tabuleiro)
time.sleep(1.0) # para a transição entre o usuario e computador ficar mais clara
mostrar_tabuleiro(tabuleiro)
verificacao(tabuleiro)

# 6° Jogada Usuario
movimento_jogador(tabuleiro)
mostrar_tabuleiro(tabuleiro) # Colocar o tabuleiro para imprimir apos cada jogada
verificacao(tabuleiro)

# 7° Jogada - Computador 
movimento_computador(tabuleiro)
time.sleep(1.0) # para a transição entre o usuario e computador ficar mais clara
mostrar_tabuleiro(tabuleiro)
verificacao(tabuleiro)

# 8° Jogada - Usuario
movimento_jogador(tabuleiro)
mostrar_tabuleiro(tabuleiro) # Colocar o tabuleiro para imprimir apos cada jogada
verificacao(tabuleiro)

# 9° Jogada - Computador 
movimento_computador(tabuleiro)
time.sleep(1.0) # para a transição entre o usuario e computador ficar mais clara
mostrar_tabuleiro(tabuleiro)
verificacao(tabuleiro)





