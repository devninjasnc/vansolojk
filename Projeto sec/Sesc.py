import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import pyttsx3
import speech_recognition as sr
rec = sr.Recognizer()

def falar():
    falar=pyttsx3.init()
    falar.say('''Olá, me chamo Júlia e sou atendente virtual do SESC IPARANA. Digite: 
        [1] Se você deseja fazer uma reserva
        [2] Se você deseja fazer um check-in
        [3] Serviços de comorbidade
        [4] Informações Locais e atrações turísticas''')
    falar.runAndWait()
    

# Criação da janela principal
janela = tk.Tk()


# Define as dimensões da janela
largura = 1366
altura = 768
janela.geometry(f"{largura}x{altura}")

# Carregamento e exibição da imagem em tela cheia
imagem_principal = Image.open("magens/iparan.jpg")
imagem_principal = imagem_principal.resize((largura, altura))
imagem_principal_tk = ImageTk.PhotoImage(imagem_principal)

label_imagem_principal = tk.Label(janela, image=imagem_principal_tk)
label_imagem_principal.pack()

frame = tk.Frame(label_imagem_principal, bg="white", width=750, height=500, bd=0)
frame.place(x=600, y=6)

bemvindol = ctk.CTkLabel(master=frame, text='Olá seja bem vindo, como posso ajudá-lo?', text_color='#006400', font=('Verdana', 28))
bemvindol.place(x=100, y=40)

sescecologico = ctk.CTkLabel(master=frame, text='''Proporcionar bem-estar é nossa natureza
O que já era bom ficou ainda mais incrível: Sesc Iparana - Hotel Ecológico, 
que teve sua estrutura ampliada e modernizada para oferecer aos seus hóspedes e visitantes
o máximo de conforto em meio à natureza.''', text_color='#006400', font=('Didot', 16))
sescecologico.place(x=90, y=100)

buttondereserva = ctk.CTkButton(master=frame, text='Reserva', width=200)
buttondereserva.place(x=90, y=300)

# Carregamento e exibição da segunda imagem
imagem_overlay = Image.open("magens/logo.png")
nova_largura = 100  # Defina a largura desejada para a imagem overlay
nova_altura = 100  # Defina a altura desejada para a imagem overlay
imagem_overlay = imagem_overlay.resize((nova_largura, nova_altura))
imagem_overlay_tk = ImageTk.PhotoImage(imagem_overlay)

# Exibição da imagem overlay em cima da imagem principal
label_imagem_overlay = tk.Label(janela, image=imagem_overlay_tk, bd=0)
label_imagem_overlay.place(x=0, y=0)
janela.after(199,falar)
janela.mainloop()