text = input('Введите текст, который вы хотите зашифровать: ').lower()
code_word = input('Введите кодовое слово для создания шифра: ').lower()

alphabet = ' qwertyuiopasdfghjklzxcvbnm'

def create_key(k):
    result = 0
    for i in k:
        result += alphabet.index(i)
    return result

def cipher(t, w):
    if len(t) > create_key(w):
        key = len(t) % create_key(w)
    else:
        key = create_key(w) % len(t) 
    result = ""
    for i in t:
        index = alphabet.index(i) + key
        if index > len(alphabet) - 1:
            index = index - len(alphabet)
        result += alphabet[index]
    return result

def decipher(t, w):
    if len(t) > create_key(w):
        key = len(t) % create_key(w)
    else:
        key = create_key(w) % len(t) 
    result = ""
    for i in t:
        index = alphabet.index(i) - key
        result += alphabet[index]
    return result

with open('code.txt', 'w') as f:
    data = cipher(text, code_word)
    file = f.write(data)

print(f'Зашифрованный текст: {data}')

decipher_input = input('Введите кодовое слово для расшифровки: ').lower()
decipher_word = decipher(data, decipher_input)

print(f'Расшифрованный текст: {decipher_word}')