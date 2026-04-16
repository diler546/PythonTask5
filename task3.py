while True:
    word = input("Введите слов(stop для остановки):")
    if word.lower() == "stop": break
    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

