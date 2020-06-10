#python_3.7

from sys import exit

def addCurrency(addedCurrency, addedCurrenciesList):
	if addedCurrency in addedCurrenciesList:
		print("Currency", addedCurrency, "is already exists on the list. Try another currency.")
	else:
		addedCurrenciesList.append(addedCurrency)
		print("Currency", addedCurrency, "added.")

def inputQuantity(default = 1, invitation = ""):
	try:
		value = input(invitation)
		if value == "":
			print("Default value", default, "selected.")
			return float(default)
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
		return value
	return -1

def inputMenu(default = 0, specialValue = "exit", menuItemsNum = 0, invitation = ""):
	isExcept = True
	while(isExcept):
		try:
			value = input(invitation)
			if value == "":
				print("Default element", int(default), "selected.")
				return int(default)
			if value == specialValue:
				return specialValue
			value = int(value)
			if value == menuItemsNum:
				return menuItemsNum
			if value < 0 or value > menuItemsNum:
				raise Exception()
		except ValueError:
			print("ERROR: Invalid data type.")
		except Exception:
			print("ERROR: Number does not correspond to any menu item.")

		else:
			isExcept = False

	return value

def printMenu(menuItemsList, specialValue = False, i = 0):
	while(i < len(menuItemsList)):
		print("[", i, "] -- ", menuItemsList[i], sep = "")
		i+=1

	if specialValue:
		print("[", len(menuItemsList), "] -- ", specialValue, sep = "")

def swap(list, serialNum):
	temp = list[0]
	list[0] = list[serialNum]
	list[serialNum] = temp

convert = lambda currency, rate: currency*rate

def main():
	currencyList = ["EUR", "USD", "RUB", "UAH", "PLN", "NOK", "PKR"]
	rateList = [0, 0, 0, 0, 0, 0, 0]
	convertToList = []

	lenght = len(currencyList)

	while True:
		print("=======================")
		print("Select currency to convert:")
		
		printMenu(currencyList, "close app")
		choice = inputMenu(invitation = "Your choice: ", specialValue = lenght, menuItemsNum = lenght)
	
		if choice == lenght:
			print("Closing app...")
			exit()
		else:
			swap(currencyList, choice)
		print("\n"*3)
		
		while True:
			print("How much", currencyList[0], " do you need to convert? ", end=" ")
			originCurrency = inputQuantity(default = 1)
			if originCurrency > 0:
				break		

		while True:
			print("Current currencies:\n", originCurrency, currencyList[0], "to:", convertToList)
			if len(convertToList) + 1 == lenght:
				print("All of currencies added. Adding stopped.")
				print("\n"*3)
				break	
				
			printMenu(currencyList, "stop adding", 1)
			choice = inputMenu(invitation = "Your choice: ", specialValue = lenght, menuItemsNum = lenght, default = 1)
			
			if choice == lenght:
				print("Adding stopped.")
				print("\n"*3)
				break	
			print("\n"*3)
			addCurrency(currencyList[choice], convertToList)
		
		
		i = 0
		while i < len(convertToList):
			print("Enter currency value:")
			while True:
				print(currencyList[0], "1 =", convertToList[i], "", end="")
				rateList[i] = inputQuantity(default = 1)
				if rateList[i] > 0:
					break
			i+=1

		print("\n"*3)
		print("Your result: ")		
		
		i=0
		while i < len(convertToList):
			print(currencyList[0], originCurrency, "=", convertToList[i], convert(rateList[i], originCurrency))
			i+=1

		convertToList.clear()
		print("\n"*3)

main()
