import speech_recognition as sr
import openai
import gtts
from playsound import playsound
from funcoes_txt import *

def captar_audio():
    
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        
        playsound('sounds/question.mp3')
        print('Qual a sua pergunta?')
        
        audio_captado = mic.listen(source)
        
        frase = mic.recognize_google(audio_captado, language = 'pt-BR')
        
        print(frase)
        
        return frase
    
with open('resposta.txt', 'r') as file:
    for line in file:
       fala = gtts.gTTS(line, lang = 'pt-BR')
       fala.save('sound.mp3')
        
def consultarCHATGPT(frase):
    openai.api_key = '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'
    
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
        
frase_final = captar_audio() 

resposta = consultarCHATGPT(frase_final)

salvarProdutos(resposta)



print(resposta) 