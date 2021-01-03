Employees = {"Data": "", "Education": 0, "Specialty": 0, "Position": 0, "Salary": 0}
arrayofEmployees = []


def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayofEmployees)):
            if arrayofEmployees[i]["Data"] == criteria:
                print(arrayofEmployees[i])
    if choose == 2:
        for i in range(len(arrayofEmployees)):
            if arrayofEmployees[i]["Education"] == criteria:
                print(arrayofEmployees[i])
    if choose == 3:
        for i in range(len(arrayofEmployees)):
            if arrayofEmployees[i]["Specialty"] == criteria:
                print(arrayofEmployees[i])
    if choose == 4:
        for i in range(len(arrayofEmployees)):
            if arrayofEmployees[i]["Position"] == criteria:
                print(arrayofEmployees[i])
    if choose == 5:
        for i in range(len(arrayofEmployees)):
            if arrayofEmployees[i]["Salary"] == criteria:
                print(arrayofEmployees[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про співробітника\n"
          "3. Знайти співробітника\n"
          "4. Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(arrayofEmployees)
    elif choose == 2:
        '''----Ввід даних про студента----'''
        data = input("Введіть паспортні дані: ")
        education = int(input("Введіть освіту: "))
        specialty = input("Спеціальність: ")
        position = int(input("Рейтинг: "))
        selery = int(input("Введіть оклад"))

        '''---Заповнення словника---'''
        Employees["Adress"] = data
        Employees["Count of faculty"] = education
        Employees["Level of accreditation"] = specialty
        Employees["Rating"] = position
        Employees["Selery"] = selery
        arrayofEmployees.append(Employees)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Паспортними даними\n"
              "2.Освітою\n"
              "3.Спеціальністю\n"
              "4.Посадою\n"
              "5.Окладом\n")
        choose2 = int(input('Введіть критерій : '))
        if choose2 == 1:
            searchCriteria = int(input("Введіть паспортні дані "))
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = input("Введіть освіту: ")
            serch(2, searchCriteria)

        if choose2 == 3:
            searchCriteria = input("Введіть спеціальність: ")
            serch(3, searchCriteria)

        if choose2 == 4:
            searchCriteria = input("Введіть посаду: ")
            serch(4, searchCriteria)

        if choose2 == 5:
            searchCriteria = input("Введіть оклад: ")
            serch(5, searchCriteria)
        print("\n")

    elif choose == 4:
        break
    else:
        print('Write normal number\n')
