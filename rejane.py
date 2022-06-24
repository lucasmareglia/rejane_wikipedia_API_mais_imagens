from speech_recognition import Microphone, Recognizer, UnknownValueError
import pyautogui
import pyttsx3
import random
import pyperclip
import wikipediaapi
import time
criatura_calma = pyttsx3.init()
criatura = pyttsx3.init()
recog = Recognizer()
mic = Microphone()

def fala_criatura(fala):
    criatura.setProperty('rate', 195)
    criatura.say(fala)
    criatura.runAndWait()
    return()

def fala_criatura_calma(fala):
    criatura_calma.setProperty('rate', 150)
    criatura_calma.say(fala)
    criatura_calma.runAndWait()
    return()

while True:
    with mic:
        fala_criatura('diga a senha')
        audio1 = recog.listen(mic)
    try:
        recognizedsenha = recog.recognize_google(audio1, language='pt').lower()         
        if recognizedsenha in 'lucas':
            fala_criatura('acesso, liberado... Vamos começaar, luucas')            
            while True:
                with mic:
                    fala_criatura('')
                    audio = recog.listen(mic)
                try:
                    recognized = recog.recognize_google(audio, language='pt').lower()
                    print(f'você disse: {recognized}')

# COMANDOS CONVERSA >>>>>>>>>>>>>>>>>>>>>
                    if recognized in 'olá''oi''oie''olá rejane''oi rejane''oie rejane':
                        conv1 = ['olá, luucas ? no que posso ajudar ?','posso lhe ajudar? Luucas?','olá, Luucas ? o que vamos fazer agora ?', 'olá, o que iremos fazer hoje, Luucas']
                        fala_criatura(random.choice(conv1))
                    elif recognized in 'pesquisa''pesquise''pesquisar':
                        while True:
                            with mic:
                                fala_criatura('o que quer pesquisar')
                                audio2 = recog.listen(mic)
                                try:
                                    recognizedpesquisa = recog.recognize_google(audio2, language='pt')
                                    pyperclip.copy(recognizedpesquisa)
                                    if recognizedpesquisa in 'cancela''cancelar''cancele''cancelar a pesquisa''cancela a pesquisa':
                                        break
                                    else:
                                        pyautogui.hotkey('win', 't')
                                        time.sleep(1)
                                        pyautogui.press('enter')
                                        time.sleep(0.5)
                                        pyautogui.hotkey('ctrl', 't')
                                        time.sleep(2)
                                        pyautogui.write('https://images.google.com/')
                                        pyautogui.press('enter')
                                        time.sleep(3.5)
                                        pyautogui.hotkey('ctrl', 'v')
                                        time.sleep(0.7) 
                                        pyautogui.press('enter')
                                        wiki_wiki = wikipediaapi.Wikipedia(language='pt', extract_format=wikipediaapi.ExtractFormat.WIKI)
                                        p_wiki = wiki_wiki.page(recognizedpesquisa)
                                        print(p_wiki.summary)
                                        fala_criatura_calma('resultados da minha busca por ...{} foi de {}'.format(recognizedpesquisa, p_wiki.summary))  
                                        break
                                except UnknownValueError:
                                    fala_criatura('')


                except UnknownValueError:
                    fala_criatura('')
        else:
            fala_criatura('senha incorreta, acesso negado!')
    except UnknownValueError:
        fala_criatura('não intendi, repita a senha por favor')

