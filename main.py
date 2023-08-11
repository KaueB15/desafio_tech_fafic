import speech_recognition as sr
import openai
import gtts
from playsound import playsound
from funcoes_txt import *
import os

def captar_audio():
    
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        
        playsound('sounds/question.mp3')
        print('Qual a sua pergunta?')
        
        audio_captado = mic.listen(source)
        
        frase = mic.recognize_google(audio_captado, language = 'pt-BR')
        
        return frase
    
def continuarPerguntas():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        
        playsound('sounds/outrapergunta.mp3')
        print('Deseja fazer outra pergunta?')
        
        audio_captado = mic.listen(source)
        
        respostaContinuar = mic.recognize_google(audio_captado, language = 'pt-BR')
        
        return respostaContinuar
        
def consultarCHATGPT(frase):
    openai.api_key = 'chave'
    
    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = frase
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text

continuar = 'sim'
while(True):
    if(continuar == 'sim'):
        frase_final = captar_audio() 

        resposta = consultarCHATGPT(frase_final)

        salvarResposta(resposta)

        with open('resposta.txt', 'r') as file:
            for line in file:
                if(len(line) > 2):
                    fala = gtts.gTTS(line, lang = 'pt-BR')
                    fala.save('resposta.mp3')                    
        playsound('resposta.mp3')
        os.remove('resposta.txt')
        os.remove('resposta.mp3')
        continuar = continuarPerguntas()
    elif(continuar == 'não'):
        print('Programa finalizado')
        break
    else:
        break