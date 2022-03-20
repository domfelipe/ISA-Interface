###### BIBLIOTECAS ######

import speech_recognition as sr
import PySimpleGUI as sg

###### MÓDULO DE APOIO ######

def reconheceraudiomicrofone(reconhecedor, microfone):

    with microfone as somprincipal:
        reconhecedor.adjust_for_ambient_noise(somprincipal)

        audio = reconhecedor.listen(somprincipal)
    
        response = {
            "sucesso": True,
            "erro": None,
            "transcricao": None
        }

        try:
            response["transcricao"] = reconhecedor.recognize_google(audio, language='pt_BR')

        except sr.RequestError:
            response["sucesso"] = False
            response["erro"] = "# Programa Indisponível"

        except sr.UnknownValueError:
            response["erro"] = "# Áudio Não Reconhecido"

        return response


###### MÓDULO PRINCIPAL DE RECONHECIMENTO DE ÁUDIO ######

if __name__ == "__main__":
    
    reconhecedor = sr.Recognizer()
    microfone = sr.Microphone()

    NFALA = 2
    NSEMFALA = 2

    print('\n ### ISA - Interface de Suporte a Acessibilidade - PROGRAMA FUNCIONANDO ###')

    for i in range(NFALA):

        for j in range(NSEMFALA):

            print('\nAguarde um momento estou identificando o áudio...\n'.format(i+1))

            somteste = reconheceraudiomicrofone(reconhecedor, microfone)

            if somteste["transcricao"]:
                break

            if not somteste["sucesso"]:
                print ("# Áudio não identificado, tentando novamente...")
                break

            if somteste["erro"]:
                print("ERRO: {}\n ".format(somteste["erro"]))
                break

        print("# Áudio Identificado: {}".format(somteste["transcricao"]))