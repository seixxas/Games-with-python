import forca
import adivinhacao

def escolhe_jogo(): 
    
    print("**************************")
    print("*****Escolha seu jogo*****")
    print("**************************")

    print("(1) Forca (2) adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo ==2):
        print("jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("Esse jogo nao existe")    

if(__name__ == "__main__"):
    escolhe_jogo()  