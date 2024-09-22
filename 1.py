import numpy as np

'''
Весь код подходит и для кодов Хэмминга, поэтому
он в одном файле
'''














def mod2(a: int) -> int:
    '''
    Функция для перевода чисел в пространство Z2
    Принимает целое число
    Возвращает его в пространстве Z2
    '''
    return a % 2

def generate_binary_strings(k):
  '''
  Функция для генерации входящих сообщений
  Принимает длину k входящего сообщения
  Возвращает список из 2^k вариантов входящих сообщений
  '''
  strings = []
  for i in range(2**k):
    binary_string = bin(i)[2:].zfill(k)
    integer_list = [int(digit) for digit in binary_string]
    strings.append(integer_list)
  return strings


def coding(gMatrix, n, k):
    '''
    Функция для кодирования сообщений
    Принимает матрицу G и числа n и k
    Возвращает матрицу из закодированных сообщений(каждая строчка это закодированное сообщение) для возможности их дальнейшего использования
    Так же печатает их на экране
    '''
    origMessage = np.array(generate_binary_strings(k))
    finMessage = np.zeros((2**k, n), dtype=int)
    for i in range(2**k):
        t = mod2(np.transpose(np.matmul(gMatrix, np.transpose(origMessage[i]))))
        print(f"G{origMessage[i]} = ", t)
        finMessage[i] = t
    return finMessage


def checkErrors(hMatrix, message):
    '''
    Функция для проверки и исправления ошибок в сообщении
    Принимает матрицу H и сообщение, которое нужно проверить
    Возвращает исправленное сообщение или его же без исправления
    '''

    print("Сообщение: ", message)
    t = mod2(np.matmul(hMatrix, np.transpose(message)))
    binNum = ""
    for i in range(len(t)):
        binNum += f"{t[i]}"
    badBit = int(binNum, 2)
    print("Результат проверки:")
    if badBit == 0:
        print(t)
        print("Ошибок не обнаружено")
    else: 
        print(t)
        print(f"Обнаружена ошибка в бите под номером {badBit}")
        print("Исправляем")
        message[badBit-1] = mod2(message[badBit-1] + 1)
    print(message)
    return message



# Пример работы функции кодирования
print("Пример работы функции кодирования:")
g2 = np.array([[1, 0,0,0], [0,1,0,0],[0,0,1,0],[0,0,0,1],[0,1,1,1],[1,0,1,1],[1,1,0,1]])
coding(g2, 7, 4)

print("")
print("")
print("")

# Пример работы функции поиска и справления ошибки
print("Пример работы функции поиска и справления ошибки:")
h = np.array([[0, 1, 1, 1, 1, 0, 0],[1, 0, 1, 1, 0, 1, 0],[1, 1, 0, 1, 0, 0, 1]])
checkErrors(h, np.array([0,1,0,0,0,0,0]))