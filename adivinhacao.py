import random 

def jogar():

    print("**************************")
    print("Bem vindo ao jogo de adivinhacao")
    print("**************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa_atual in range(1, total_de_tentativas + 1): 
        print(f"Tentativa {tentativa_atual} de {total_de_tentativas}")
        chute = int(input("Digite um numero entre 1 e 100: "))
        
        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou     = chute == numero_secreto
        chute_menor = chute < numero_secreto
        chute_maior = chute > numero_secreto

        if(tentativa_atual == total_de_tentativas):
            print(f"Acabou as tentativas :( o numero secreto era, {numero_secreto}")         
        if(acertou):
            print(f"Voce acertou e fez {pontos} pontos!")
            print("Fim de jogo")    
            break
        else: 
            if(tentativa_atual < total_de_tentativas):  
                if(chute_menor):
                    print("Seu chute foi menor que o numero secreto.")
                elif(chute_maior):
                    print("Seu chute foi maior que o numero secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
if(__name__ == "__main__"):
    jogar()     
                 
    
    
    

