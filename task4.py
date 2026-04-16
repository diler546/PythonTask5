import random

mistakes = 0
correct_answer = 0
while mistakes < 3:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    try:
        answer = int(input(f"{num1} + {num2} = "))
    except:
        print("Введите число")
        continue
    if answer == num1 + num2:
        print("Правильно!")
        correct_answer +=1
    else:
        print("Ответ неверный")
        mistakes += 1
print(f"Игра окончена. Правильных ответов: {correct_answer}")
