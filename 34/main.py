# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке


# Вводим стих:
stix = list(input().split())
print(stix)

# Функция подсчета слогов в слове
def counter(text):
    count = 0
    for i in text:
        if i == 'а':
            count += 1
    return count

# Функция проверки на количество слогов (гласных букв)
def count_of_a(counter, data):
    counts = list(map(counter, data))
    print(counts)
    return len(set(counts)) == 1

if count_of_a(counter, stix):
    print('Парам пам-пам')
else: print('Пам парам')

