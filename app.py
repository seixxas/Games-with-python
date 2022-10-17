from ast import If
from re import I


print("**************************")
print("Bem vindo ao jogo de adivinhacao")
print("**************************")

numero_secreto = 47

chute = int(input("Digite um numero: "))

acertou     = chute == numero_secreto
chute_menor = chute < numero_secreto
chute_maior = chute > numero_secreto


if(acertou):
    print("Voce acertou!")
else:
    if(chute_menor):
        print("Seu chute foi menor que o numero secreto.")
    elif(chute_maior):
        print("Seu chute foi maior que o numero secreto.")    
   

print("Fim de jogo")    

