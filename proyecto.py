from random import choice

palabras = ['smartphone', 'libro', 'coche', 'palo', 'cuadro']
life = 5
intentos = 0
palabra = ''
palabra_adivina = []
palabras_dichas = []

def select_word():
    word = choice(palabras)
    for n in word:
        palabra_adivina.append('-')
    return word

def select_character():
    letra = '  '
    while len(letra) > 1:
        letra = input("Introduce una letra: ")
        if len(letra) == 1:
            return letra
        else:
            letra = '  '

def letra_in_word(word):
    global life, intentos
    if word in palabra:
        intentos += 1
        i = palabra.index(word)
        palabra_adivina[i] = word
    else:
        life -= 1
        intentos += 1
        if life == 0:
            game_over()
    palabras_dichas.append(word)

def game_over():
    print(f"Has perdido, la palabra a adivinar era {palabra}.")

palabra = select_word()
while life > 0:
    c = select_character()
    letra_in_word(c)
    print(f"Vidas restantes: {life}\n"
          f"Intentos: {intentos}\n"
          f"Palabras dichas: {palabras_dichas}\n"
          f"Estado del tablero: {palabra_adivina}")
    if palabra_adivina.count('-') == 0:
        life = 0
        print(f"Enhorabuena, has ganado!")