# Python 3.8

def inputInt(prompt=""):
    while True:
        try:
            res = int(input(prompt))
            return res
        except:
            print("Invalid input")


def inputFloat(prompt=""):
    while True:
        try:
            res = float(input(prompt))
            return res
        except:
            print("Invalid input")


def Menu(menuItems):
    i = 0
    while i < len(menuItems):
        print("[" + str(i) + "]", menuItems[i])
        i += 1

    while True:
        out = inputInt("Your choise: ")
        if out >= 0 and out < len(menuItems):
            return out
        else:
            print("Invalid input")


def CurrenciesSelection(currency):
    menu = list(currency)
    selected = list()

    while True:
        choise = Menu(menu)

        if len(selected) == 0:
            menu.insert(0, "Convert")
            choise += 1

        if choise == 0:
            return selected
        else:
            selected.append(menu[choise])
            menu.remove(menu[choise])

            if len(menu) == 1:
                return selected
        print("\n" * 2)


def EnterCurrRate(selCurr, srcCurr):
    currRate = list()

    i = 0
    while i < len(selCurr):
        while True:
            rate = inputFloat(f"Enter {srcCurr} cost in {selCurr[i]}: ")
            if rate > 0:
                currRate.append(rate)
                break
            else:
                print("Invalid input")
        i += 1
    return currRate


def Convert(srcCurr, selCurr, currRate, convValue):
    i = 0
    while i < len(selCurr):
        convResult = convValue * currRate[i]
        print(str(round(convValue, 2)), srcCurr, "=", str(round(convResult, 2)), selCurr[i])
        i += 1


def Main():
    currency = ["USD", "EUR", "UAH", "PLN", "BYR", "CNY", "RUB"]

    print("Convert from:")
    convFrom = Menu(currency)
    print("\n" * 2)

    print("Convert to:")
    selCurr = CurrenciesSelection(list(currency[0: convFrom]) +
                  list(currency[convFrom + 1: len(currency)]))
    print("\n" * 2)

    convValue = 0
    while True:
        convValue = inputFloat(f"Enter amoun in {currency[convFrom]}: ")
        if convValue > 0:
            break
        else:
            print("Invalid input")

    currRate = EnterCurrRate(selCurr, currency[convFrom])
    print("\n\n")
    Convert(currency[convFrom], selCurr, currRate, convValue)


Main()
convAgain = 'n'
while True:
    convAgain = input("\nConvert again? (y/n): ")
    if convAgain == 'y':
        Main()
    else:
        break