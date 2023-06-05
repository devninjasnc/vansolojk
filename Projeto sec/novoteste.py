import speech_recognition as sr
from colorama import Fore
import pyttsx3
import time
import datetime
rec = sr.Recognizer()

with sr.Microphone(0) as mic:
    boasv = pyttsx3.init()
    boasv.setProperty('rate', 150)
    boasv.setProperty('volume', 0.7)
    texto2 = 'Olá pode me ajudar'
    boasv.say(texto2)
    boasv.runAndWait()
    rec.adjust_for_ambient_noise(mic)
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    if 'ajuda' in texto.lower():
        # Cria um objeto da classe Text-to-speech engine
        engine = pyttsx3.init()

        # Define a taxa de fala (opcional)
        engine.setProperty('rate', 150)  # Valor padrão: 200

        # Define o volume (entre 0 e 1, opcional)
        engine.setProperty('volume', 0.7)  # Valor padrão: 1

        # Texto que você deseja transformar em fala
        textofalar = '''Olá, me chamo Júlia e sou atendente virtual do SESC IPARANA. Digite: 
        [1] Se você deseja fazer uma reserva
        [2] Se você deseja fazer um check-in
        [3] Serviços de comorbidade
        [4] Informações Locais e atrações turísticas'''

        # Usa o mecanismo para converter o texto em fala
        engine.say(textofalar)

        # Reproduz a fala
        engine.runAndWait()

    # Reconhecimento de voz para seleção de opção
    opcao = None
    while opcao is None:
        audio2 = rec.listen(mic)
        opcao_texto = rec.recognize_google(audio2, language="pt-BR")
        if opcao_texto == '1':
            opcao = 1
            op1=pyttsx3.init()
            op1.setProperty('rate',150) #VELOCIDADE DA FALA
            op1.setProperty('volume',0.7) # VOLUME DA FALA
            texto3= 'Vi que você deseja fazer uma reserva, poderia me informar seu nome completo?'
            op1.say(texto3)
            op1.runAndWait()
            #RECEBER CPF  COMANDO DE VOZ
            op1cpf=pyttsx3.init()
            op1cpf.setProperty('rate',150) #VELOCIDADE DA FALA
            op1cpf.setProperty('volume',0.7) # VOLUME DA FALA
            audio3=rec.listen(mic)
            nomeop1 = rec.recognize_google(audio3,language='pt-BR') #VAI RECEBER O NOME DO CLIENTE
            texto4='Vi que seu nome é{},agora poderia me dizer qual seu CPF?'.format(nomeop1)
            op1cpf.say(texto4)
            op1cpf.runAndWait()
            audio4=rec.listen(mic)
            cpfop1=rec.recognize_google(audio3,language='pt-BR')
            op1hosp=pyttsx3.init()
            op1hosp.setProperty('rate',150)
            op1hosp.setProperty('volume',0.7)
 
            texto5='Agora que já tenho suas informações e seu CPF é  ,gostaria de saber quantos hospédes ficarão no quarto'.format(cpfop1)
            op1hosp.say(texto5)
            op1hosp.runAndWait
            print(Fore.RED+'''RESERVA OKAY
                                Nome:{}
            '''.format(nomeop1))
            
        elif opcao_texto == '2':
            opcao = 2
            op1=pyttsx3.init()
            op1.setProperty('rate',150) #VELOCIDADE DA FALA
            op1.setProperty('volume',0.7) # VOLUME DA FALA
            texto3= 'Vi que você deseja fazer um check-in, poderia me informar seu nome completo?'
            op1.say(texto3)
            op1.runAndWait()
            #RECEBER CPF  COMANDO DE VOZ
            op1cpf=pyttsx3.init()
            op1cpf.setProperty('rate',150) #VELOCIDADE DA FALA
            op1cpf.setProperty('volume',0.7) # VOLUME DA FALA
            audio3=rec.listen(mic)
            nomeop1 = rec.recognize_google(audio3,language='pt-BR') #VAI RECEBER O NOME DO CLIENTE
            op2=pyttsx3.init()
            op2.setProperty('rate',150) #VELOCIDADE DE FALA
            op2.setProperty('valume',0.7) #VOLUME DE FALA
            text4='Continuando, me fale o numero da reserva de confirmção do hotel'
            op2.say(text4)
            op2.runAndWait()
            op2con=pyttsx3.init()
            op2con.setProperty('rate',150) #VELOCIDADE DE FALA
            op2con .setProperty('volume',0.7) # VOLUME DA FALA
            audio21=rec.listen(mic)
            reservaop2 = rec.recognize_google(audio21,language='pt-BR') #VAI RECEBER a confirmação DO CLIENTE
            text4='Vi que seu numero da reserva é{},agora poderia me informar localização e datas de check-in e check-out'.format(reservaop2)
            op2con.say(text4)
            op2con.runAndWait()
            op2con=pyttsx3.init()
            op2con.setProperty('rate',150) #VELOCIDADE DE FALA
            op2con .setProperty('volume',0.7) # VOLUME DA FALA
            audio21=rec.listen(mic)
            dataop2 = rec.recognize_google(audio21,language='pt-BR') #VAI RECEBER a confirmação DO CLIENTE
            text4='Muito obrigado pelas informações maketa martelinho.'.format(dataop2)
            op2con.say(text4)
            op2con.runAndWait()
            print (Fore.GREEN+'''CHECK-IN OK
            [Nome]:{}
            [Número da Reserva]:{}
            [Data e Localização]:{}'''.format(nomeop1,reservaop2,dataop2))
            
        elif opcao_texto == '3':
            opcao = 3
        elif opcao_texto == '4':
            opcao = 4
            print(Fore.RED + 'MAKETA POLAR VULGO MARTELINHO')
        else:
            print(Fore.YELLOW + 'Opção inválida. Por favor, tente novamente.')

# Execute ações com base na opção selecionada
