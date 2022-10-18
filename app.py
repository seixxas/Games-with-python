import random 


print("**************************")
print("Bem vindo ao jogo de adivinhacao")
print("**************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 5

print(numero_secreto)

for tentativa_atual in range(1, total_de_tentativas + 1): 
    print(f"Tentativa {tentativa_atual} de {total_de_tentativas}")
    chute = int(input("Digite um numero entre 1 e 100: "))
    
    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100")
        continue

    acertou     = chute == numero_secreto
    chute_menor = chute < numero_secreto
    chute_maior = chute > numero_secreto

    if(tentativa_atual == 5):
        print(f"Acabou as tentativas :( o numero secreto era, {numero_secreto}")         
    if(acertou):
        print("Voce acertou!")
        print("Fim de jogo")    
        break
    else: 
        if(tentativa_atual < 5):  
            if(chute_menor):
                print("Seu chute foi menor que o numero secreto.")
            elif(chute_maior):
                print("Seu chute foi maior que o numero secreto.")
                 
    
    
    

