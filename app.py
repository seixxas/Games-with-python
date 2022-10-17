from ast import If
from re import I


print("**************************")
print("Bem vindo ao jogo de adivinhacao")
print("**************************")

numero_secreto = 47

chute = int(input("Digite um numero: "))

if (numero_secreto == chute):
    print("Voce acertou!")
else:
    print("Voce errou :(")
