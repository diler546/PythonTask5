count = int(input("Введите количество слов:"))

words = ""
for i in range(count):
    word = input("Введите слово:")
    words += word + " "
print(words)

