while True:
    try:
        m = int(input("Введите номер месяца от 1 до 12: "))
        my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
               10: "Осень", 11: "Осень", 12: "Зима"}
        if m in my_dict.keys():
            print(my_dict.get(m))
        else:
            print("Введенное значение не корректно, пожалуйста, попробуйте еще разок: ", )
        break
    except ValueError:
        print("Пожалуйста введите числовое значение")
