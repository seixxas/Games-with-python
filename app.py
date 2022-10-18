from ast import If
from re import I


print("**************************")
print("Bem vindo ao jogo de adivinhacao")
print("**************************")

numero_secreto = 47
total_de_tentativas = 5

tentativa_atual = 1

for tentativa_atual in range(1, total_de_tentativas + 1): 
    print("Tentativa {} de {}".format(tentativa_atual, total_de_tentativas))
    chute = int(input("Digite um numero: "))

    acertou     = chute == numero_secreto
    chute_menor = chute < numero_secreto
    chute_maior = chute > numero_secreto

    if(acertou):
        print("Voce acertou!")
        break
    else:   
        if(chute_menor):
            print("Seu chute foi menor que o numero secreto.")
        elif(chute_maior):
             print("Seu chute foi maior que o numero secreto.")    
    
print("Fim de jogo")    
    
    

