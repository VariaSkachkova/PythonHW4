# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное 
# количество символов влево или вправо. При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2
# вправо, "юяяю" - сдвиг на 2 влево. Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


alphabet_en = ' abcdefghijklmnopqrstuvwxyz'
alphabet_ru = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

'''Функция для кодирования текста, написанного на латинице или кириллице, шифром Цезаря'''
def code_text(alphabet_en, alphabet_ru):    
    bias = int(input('Введите целое число – значение смещения: '))
    text = input('Введите слово, которое нужно зашифровать: ').strip()
    text = text.lower()
    coded_text = ''
    for i in text:
        if i in alphabet_en:
            coded_text += alphabet_en[(alphabet_en.index(i) + bias) % len(alphabet_en)]
        elif i in alphabet_ru:
            coded_text += alphabet_ru[(alphabet_ru.index(i) + bias) % len(alphabet_ru)]
        else:
            print('Неправильный ввод. Нужно ввести слово кириллицей или латиницей без специальных знаков.')
            break
    print(f'Зашифрованный текст: {coded_text}')

'''Функция для декодирования текста, написанного на латинице или кириллице, шифром Цезаря'''

def decode_text(alphabet_en, alphabet_ru):
    bias_to_decode = int(input('Введите значение смещения, которое использовалось для шифрования: '))
    text_to_decode = input('Введите зашифрованное слово: ').strip()
    decoded_text = ''
    for i in text_to_decode:
        if i in alphabet_en: 
            decoded_text += alphabet_en[(alphabet_en.index(i) - bias_to_decode) % len(alphabet_en)]
        elif i in alphabet_ru:
            decoded_text += alphabet_ru[(alphabet_ru.index(i) - bias_to_decode) % len(alphabet_ru)]
        else:
            print('Неправильный ввод. Нужно ввести слово кириллицей или латиницей без специальных знаков.')
            break
    print(f'Расшифрованный текст: {decoded_text}')

code_text(alphabet_en, alphabet_ru)
decode_text(alphabet_en, alphabet_ru)


