# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.
'''Записываем строку в файл'''
with open('sequence.txt', 'w') as file:
    file.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

'''Считываем строку из файла'''
with open('sequence.txt', 'r') as file:
    sequence = file.read()

''' Сжимаем строку по RLE алгоритму – получаем список кортежей'''
def encode(sequence):
    count = 1
    zipped_text = []
 
    for x,item in enumerate(sequence): 
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:        
            zipped_text.append((sequence[x - 1], count))
            count = 1            
    zipped_text.append((sequence[len(sequence) - 1], count))
    return zipped_text

zipped_text = encode(sequence)

'''Записываем список кортежей в новый файл'''
with open('zipped_sequence.txt', 'w') as file:
    file.write(str(zipped_text))

'''Восстанавливаем строку из списка кортежей'''
def decode(zipped_text):
    unzipped_text = [] 
    for item in zipped_text:
        unzipped_text.append(item[0] * item[1]) 
    return "".join(unzipped_text)

'''Добавляем восстановленную сроку в первый файл'''
with open('sequence.txt', 'a') as file:
    file.write('\n')
    file.write(str(decode(zipped_text)))