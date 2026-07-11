print("Примечание! Пишите ваше выражение с пробелами, иначе программа выдаст ошибку/Note! Write your calculation with spaces, otherwise the program will give an error")
while True:
    we = input("Введите выражение(или 'exit' для выхода):" )
    if we == "exit":
        break

    try:
        a, sign, b = we.split()
        a = float(a)
        b = float(b)

        if sign == "+":
            print(a+b)
        elif sign == "-":
            print(a-b)
        elif sign == "*":
            print(a*b)
        elif sign == "/":
            if b == 0:
                print("Ошибка деления")
            else:
                print(a/b)
        else:
            print("Неподдерживаемая операция. Используйте +,-,*,/")


    except ValueError:
        print("Ошибка: введите выражение в формате 'число знак число'")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

