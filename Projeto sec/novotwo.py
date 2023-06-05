import tkinter as tk
from PIL import ImageTk, Image
import customtkinter as ctk

# Cria a janela principal
root = tk.Tk()

# Maximiza a janela
root.state('zoomed')

# Carrega a imagem
image_path = "magens\omenovo.png"
image = Image.open(image_path)
image = image.resize((int(root.winfo_screenwidth()/2), root.winfo_screenheight()))
photo = ImageTk.PhotoImage(image)

# Cria o widget do rótulo para exibir a foto
photo_label = tk.Label(root, image=photo)
photo_label.pack(side="left", fill="both", expand=True)

# Cria o frame na metade direita
frame = tk.Frame(root, bg="white")
frame.pack(side="right", fill="both", expand=True)

# Adiciona widgets ao frame
label = tk.Label(frame, text="Olá como podemos te ajudar?", font=("Arial", 24), bg="green")
label.pack(padx=50, pady=50)

botao1=ctk.CTkButton(fr)

# Inicia o loop principal da janela
root.mainloop()
