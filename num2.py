text = input("Введите текст: ")
count = 0
vowel = set("аеиоуюяэ")
for letter in text:
    if letter in vowel:
        count = count + 1
print("Количество гласных: ", count)
count_2 = 0
consonant = set("бвгджзйклмнпрстфхцчшщ")
for letter in text:
    if letter in consonant:
        count_2 = count_2 + 1
print("Количество согласных: ", count_2)
if count == count_2:
    for letter in text:
        if letter in vowel:
            print(letter, end=" ")
word = text.split()
num_word = len(word)
print("Количество слов: ", num_word)
