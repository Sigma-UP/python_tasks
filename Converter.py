#python_3.7

from sys import exit

def addCurrency(addedCurrency, currenciesList, rateList): 
	#функция добавления в список
	#новых элементов с проверкой на повторения
	if addedCurrency in currenciesList:
		print("Currency", addedCurrency, "is already exists on the list. Try another currency.")
	else:
		currenciesList.append(addedCurrency)	#добавление элемента в конец списка
		rateList.append(1)						#добавление элемента в конец списка
		print("Currency", addedCurrency, "added.")

def inputQuantity(default = 1, invitation = ""):
	#функция проверки ввода 
	#вещественного значения
	try:
		value = input(invitation)
		if value == "":										#возвращение дефолтного значения при пустой строке
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
	#возвращение -1 при возникновении любого exception с выводом информации об исключении
	return -1		

def inputMenu(default = 0, menuItemsNum = 0, invitation = ""):
	#функция проверки ввода
	#int-значения от 0 до menuItemsNum
	
	#возвращение дефолтного значения при вводе пустой строки | (1)
	isExcept = True
	while(isExcept):
		try:
			value = input(invitation)
			if value == "":			# - 1
				print("Default element", int(default), "selected.")
				return int(default)

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

def printList(menuItemsList, specialValue = False, i = 0):
	#вывод элементов списка
	#возможность вывода 
	#доп. значения specialValue(по дефолту откл)
	while(i < len(menuItemsList)):
		print("[", i, "] -- ", menuItemsList[i], sep = "")
		i+=1

	if specialValue:
		print("[", len(menuItemsList), "] -- ", specialValue, sep = "")

def swap(list, serialNum):
	#функция для обмена
	#расположения элемента serialNum
	#и нулевого элемента
	temp = list[0]
	list[0] = list[serialNum]
	list[serialNum] = temp

convert = lambda currency, rate: currency*rate #функция для конвертации

####MAIN FUNC#####

def main():
	##LISTS
	currencyList = ["EUR", "USD", "RUB", "UAH", "PLN", "NOK", "PKR"]
	rateList = []
	convertToList = []			#для названия валют, в которые переводится количество переводимой валюты originCurrency(объявлена ниже) 

	length = len(currencyList)	#сохранение длинны общего списка валют (для сокращения надписи)

	##ОСНОВНАЯ ЧАСТЬ
	while True:
		print("=======================")
		
		##ВЫБОР КОНВЕРТИРУЕМОЙ ВАЛЮТЫ
		print("Select currency to convert:")
		printList(currencyList, specialValue = "close app")	#вывод списка валют
		choice = inputMenu(invitation = "Your choice: ", menuItemsNum = length) #выбор конвертируемой валюты
	
		if choice == length:	#выход из приложения
			print("Closing app...")
			exit()
		else:					
			swap(currencyList, choice)	#обмен позициями нулевого элемента и переводимой валюты
		print("\n"*3)
		

		##ВЫБОР КОЛИЧЕСТВА КОНВЕРТИРУЕМОЙ ВАЛЮТЫ
		while True:
			print("How much", currencyList[0], " do you need to convert? ", end=" ") 
			originCurrency = inputQuantity(default = 1)	#выбор количества конвертируемой валюты 
			if originCurrency > 0:
				break		

		##ВЫБОР ВАЛЮТ В КОТОРЫЕ КОНВЕРТИРУЕТ ПРОГРАММА
		##ВАЛЮТЫ ЗАПИСЫВАЮТСЯ В convertToList
		while True:
			print("Current currencies:\n", originCurrency, currencyList[0], "to:", convertToList)
			if len(convertToList) + 1 == length:	#завершение добавления валют, если все доступные валюты задействованы
				print("All of currencies added. Adding stopped.")
				print("\n"*3)
				break	
				
			printList(currencyList, "stop adding", 1)
			choice = inputMenu(invitation = "Your choice: ", menuItemsNum = length, default = 1) #выбор валюты
			
			if choice == length and len(convertToList) == 0: #проверка на наличие добавленных элементов в convertToList при выборе остановки выбора валют
				print("Select at least one currency to convert.")
				continue	#continue, о существовании которого я вспомнил спустя суммарных 10+часов работы с питоном
			
			elif choice == length:	#ручная остановка выбора валют
				print("Adding stopped.")
				print("\n"*3)
				break	
			print("\n"*3)
			addCurrency(currencyList[choice], convertToList, rateList) #добавление/проверка валюты в список/-ке convertToList
		
		##ВВОД КУРСА ДЛЯ КАЖДОЙ ВАЛЮТЫ ИЗ convertToList В СПИСОК rateList[i]
		i = 0
		while i < len(convertToList):
			print("Enter currency value:")
			while True:	#повтор цикла, пока не будет введено корректное значение
				print(currencyList[0], "1 =", convertToList[i], "", end="")
				rateList[i] = inputQuantity(default = 1)
				if rateList[i] > 0:
					break
			i+=1
		print("\n"*3)


		##ВЫВОД РЕЗУЛЬТАТА
		print("Your result: ")		
		i=0
		while i < len(convertToList):
			print(currencyList[0], originCurrency, "=", convertToList[i], convert(rateList[i], originCurrency))
			i+=1

		convertToList.clear()		#очистка списков
		rateList.clear()			#очистка списков


		print("\n"*3)

main()
