def my_reference():
    name = input("Введите своё имя: ")
    surname = input("введите свою фамилию: ")
    date = int(input("Введите год рождения: "))
    city = input("Введите город проживания: ")
    email = int(input("Введите свой email: "))
    phone_number = int(input("Введите номер телефона: "))
    return print(f"Имя: {name}, Фамилия: {surname}, год рождения: {date},"
                 f" город: {city}, email: {email}, номер телефона: {phone_number}.")


my_reference()
