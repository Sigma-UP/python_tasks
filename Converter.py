from sys import exit

def inputFloat(default, invitation = ""):
	isExcept = True
	while(isExcept):
		try:
			value = input(invitation)
			if value == "":
				return default
			value = float(value)
			if value < 0:
				raise Exception("ERROR: Value is less than zero.")
			if(value == 0):
				raise Exception("ERROR: Value is zero.")
		except ValueError:
			print("ERROR: Invalid data type.")
		except Exception as CurrentException:
			print(CurrentException)
		else:
			isExcept = False
	return value
def inputMenu(default, exitCode = 1488, menuItemsNum = 0, invitation = ""):
	isExcept = True
	while(isExcept):
		try:
			value = input(invitation)
			if value == "":
				return default

			value = int(value)
			if value == exitCode:
				exit()
			if (value < 0 or value >= menuItemsNum) and value != exitCode:
				raise Exception()
		except ValueError:
			print("ERROR: Invalid data type.")
		except Exception:
			print("ERROR: Number does not correspond to any menu item.")

		else:
			isExcept = False

	return value

def swap(list, serialNum):
	temp = list[0]
	list[0] = list[serialNum]
	list[serialNum] = temp

convert = lambda currency, rate: currency*rate

def main():
	currencyList = ["EUR", "USD", "RUB", "UAH", "PLN", "NOK", "PKR"]
	rateList = [1, 1, 1, 1, 1, 1, 1]

	while True:
		print("=======================")

		i = 0
		while(i < len(currencyList)):
			print("[", i, "] -- ", currencyList[i], sep="")
			i+=1

		chosenCurrency = inputMenu(default = 0, exitCode = -1, menuItemsNum = len(currencyList), invitation = "Choose currency or enter -1 to exit: ")
		if chosenCurrency != 0:
			swap(currencyList, chosenCurrency)
		print()

		print("Enter currency rate:")
		i = 1
		while(i < len(currencyList)):
			print(currencyList[0], " 1 = ", currencyList[i], " ", sep = "", end ="")
			rateList[i] = inputFloat(rateList[i])
			i+=1

		i = 0
		print("How much", currencyList[0], " do you need to convert? ", end=" ")
		originCurrency = inputFloat(rateList[i])

		print("Currency rate table:")
		i = 1
		while(i < len(currencyList)):
			print(currencyList[0], originCurrency, " =", currencyList[i], convert(rateList[i], originCurrency))
			i+=1


main()
