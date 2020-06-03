import sys

_continue = True
while _continue:
    print("=======================")
    print("Выберите валюту для конвертации:")
    print("[0] USD -- > UAH\n[1] UAH --> USD\n[9] Выход из программы.")
    choice = int(input("Ваш выбор: "))
    print()
    if choice == 0 or choice == 1:
        coeffic = float(input("Введите курс USD в UAH: "))
        if choice == 0:
            USD = float(input("Введите количество USD: "))
            UAH = USD*coeffic
            print(USD, "USD =", UAH, "UAH")
        elif choice == 1:
            UAH = float(input("Введите количество UAH: "))
            USD = UAH/coeffic
            print(UAH, " UAH = ", USD, " USD")
    elif choice == 9:
        print("Выход из программы...")
        sys.exit()
    print("=======================\n")
