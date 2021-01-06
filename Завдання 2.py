

productionDict = {"Name": "", "Cost": "", "Genre": 0, "Levels": "", }
arrayOfProductionDict = []


def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Name"] == criteria:
                print(arrayOfProductionDict[i])
    if choose == 2:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Cost"] == criteria:
                print(arrayOfProductionDict[i])
    if choose == 3:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Genre"] == criteria:
                print(arrayOfProductionDict[i])
    if choose == 4:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Levels"] == criteria:
                print(arrayOfProductionDict[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про гру\n"
          "3. Знайти гру\n"
          "4. Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(arrayOfProductionDict)
    elif choose == 2:

        name = input("Введіть назву: ")
        cost = input("Введіть вартість гри: ")
        genre = input("Введіть жанр: ")
        levels = input("Введіть к-сть рівнів: ")


        productionDict["Name"] = name
        productionDict["Cost"] = cost
        productionDict["Genre"] = genre
        productionDict["Levels"] = levels
        arrayOfProductionDict.append(productionDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Назва\n"
              "2.Вартість гри\n"
              "3.Жанр\n"
              "4.К-сть рівнів\n")
        choose2 = int(input("Виберіть номер: "))
        if choose2 == 1:
            searchCriteria = input("Введіть назву: ")
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = int(input("Введіть вартість гри: "))
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = input("Введіть жанр: ")
            serch(3, searchCriteria)
        if choose2 == 4:
            searchCriteria = int(input("Введіть к-сть рівнів: "))
            serch(4, searchCriteria)
        print("\n")
    elif choose == 4:
        break
    else:
        print("Ведіть коректне число\n")