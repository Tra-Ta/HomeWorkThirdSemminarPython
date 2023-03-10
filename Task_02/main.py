# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.

# Например : ноутбук
#             12

listKey = 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т, D, G, Д, К, Л, М, П, У, B, C, M, P, Б, Г, Ё, Ь, Я, F, H, V, W, Y, Й, Ы, K, Ж, З, Х, Ц, Ч, J, X, Ш, Э, Ю, Q, Z, Ф, Щ, Ъ'
listValue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 8, 8, 8, 8, 8,10,10,10,10,10]
listKey = listKey.split(", ")

myDict = {listKey[i]: listValue[i] for i in range(0, len(listKey), 1)} 

wordUser = str(input('Введите ваше слово Большими буквами и ТОЛЬКО на русском или английском языке: -> '))
wordUser = list(wordUser)

res = 0

for k, v in myDict.items():
    for item in wordUser:
        if k == item:
            res += v

if res == 0:
    print('БОЛЬШИМИ БУКВАМИИИИИИ!!!!!')
else:
    print(f'Стоимость введенного вами слова равна {res}')