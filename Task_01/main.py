# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

listRandomNumbers = []
listLength = int(input('Введите длину списка: -> '))
for i in range(listLength):
    listRandomNumbers.append(random.randint(1,100))

print(listRandomNumbers)

foundNumber = int(input('Введите искомое число: -> '))

if listRandomNumbers.count(foundNumber) == 0:
    minimalNumbers = listRandomNumbers[0]
    for i in listRandomNumbers:
        if abs(foundNumber - i) < abs(foundNumber - minimalNumbers):
            minimalNumbers = i
    print(f'Ближайшее число к {foundNumber} это {minimalNumbers}')
else:
    print(f'Искомое число встречается в списке {listRandomNumbers.count(foundNumber)} раз')

        
