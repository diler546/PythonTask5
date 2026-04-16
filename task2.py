words = ""
word = ""
while True:
    word = input("Введите слово(stop для остановки):")
    if word.lower() == "stop": break
    words += word + " "
print(words)

