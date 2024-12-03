import os
import shutil


def imc():
    try:
        peso = float(input("Qaul a sua Peso em kg? "))
        altura = float(input("Qaul a sua Altura em Metros? "))
        imc = peso / (altura * 2)
        print(f"Seu Peso é {peso}, sua Altura é {altura} e seu IMC é {imc}")

        if imc > 25:
            print("Obesidade Grave")
        elif imc < 25 and imc > 22:
            print("Leve Obesidade")
        # pode continuar se quiser...
    except Exception as error: 
        if peso or altura <= 0:
            print("Peso ou Altura inválidos")

imc()



def convert_temp():
    temperatura = float(input("Informe uma Temperatura? "))
    escolha_temperatura = input("Digite 1 para converter para Celsios e 2 para Farenheit => ")

    if escolha_temperatura == "1":
        celsios = (temperatura - 32) * 5/9
        print(f"A temperatura em celsios é {celsios}")
    elif escolha_temperatura == "2":
        farenheit = (temperatura * 9/5) + 32
        print(f"A temperatura em farenheit é {farenheit}")
    else:
        print("Opções inválidas digite 1 ou 2!")



def organizar_por_extensao(diretorio_alvo):
    for filename in os.listdir(diretorio_alvo):
        if os.path.isfile(os.path.join(diretorio_alvo, filename)):
            extensao = filename.split('.')[-1]
            pasta_destino = os.path.join(diretorio_alvo, extensao)
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            shutil.move(os.path.join(diretorio_alvo, filename), os.path.join(pasta_destino, filename))


diretorio_alvo = "C:/Users/74992/exercicios-python/pasta"
organizar_por_extensao(diretorio_alvo)
print("Arquivos organizados por extensão")


