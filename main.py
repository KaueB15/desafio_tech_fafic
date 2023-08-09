import speech_recognition as sr
import openai

mic = sr.Recognizer()

def captar_audio(mic):
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        
        print('A')
        
        audio_captado = mic.listen(source)
        
        frase = mic.recognize_google(audio_captado, language = 'pt-BR')
        
        print(frase)
        
        return frase
        
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
        
frase_final = captar_audio(mic)

resposta = consultarCHATGPT(frase_final)

print(resposta)