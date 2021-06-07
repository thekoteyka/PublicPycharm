def welcome_speech(t):
    print(f"""
    Добро пожаловать в игру!
    Ваша задача - угадать слово за несколько попыток,
    иначе Вы проиграете! :(
    загаданное слово состоит из {len(t)} букв
    """)


def start_template(w):
    t = []
    for l in w:
        t.append('_')
    return t


def list_to_string_convert(t):
    s = ''
    return s.join(t)


def get_word(w):
    return w[0]


def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

game()
