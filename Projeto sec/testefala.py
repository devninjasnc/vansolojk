import pyttsx3

# Cria um objeto da classe Text-to-speech engine
engine = pyttsx3.init()

# Define a taxa de fala (opcional)
engine.setProperty('rate', 150)  # Valor padrão: 200

# Define o volume (entre 0 e 1, opcional)
engine.setProperty('volume', 0.7)  # Valor padrão: 1

# Texto que você deseja transformar em fala
texto = "Olá, mundo!"

# Usa o mecanismo para converter o texto em fala
engine.say(texto)

# Reproduz a fala
engine.runAndWait()
