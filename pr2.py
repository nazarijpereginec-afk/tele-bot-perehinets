from datetime import date, datetime
import os

from pr1 import Catalog, Booking, Bookings

fileNameTours = "dataTours.txt"
fileNameBookings = "dataBookings.txt"

tours = Catalog()
bookings = Bookings()

def options(): 
    print("\n-------------- ГОЛОВНЕ МЕНЮ --------------")
    print("1: Список доступних турів")
    print("2: Список бронювань")
    print("3: Додати новий тур")
    print("4: Забронювати тур")
    print("5: Пошук туру")
    print("6: Пошук серед бронювань")
    print("7: Очистити екран")
    print("8: Зберегти дані у файл")
    print("9: Закрити бронювання")
    print("10: EXIT")

def options_tours_find():
    print("\n------- ПОШУК ТУРІВ -------")
    print("1: Пошук за країною")
    print("2: Пошук за описом")
    print("3: Редагувати тур")
    print("4: Очистити вікно")
    print("5: Назад")

def options_bookings_find():
    print("\n------- ПОШУК БРОНЮВАНЬ -------")
    print("1: Пошук за номером")
    print("2: Пошук за країною")
    print("3: Очистити вікно")
    print("4: Назад")

tours.read_from_file(fileNameTours)
bookings.read_from_file(fileNameBookings)

options()

while True:
    option = input("-- Виберіть пункт меню: ")

    if option == '1':
        tours.print("all")
        
    elif option == '2':
        bookings.print()

    elif option == '3':
        country = input("Введіть країну: ")
        price = float(input("Введіть ціну туру: "))
        slots = int(input("Введіть кількість місць: "))
        desc = input("Введіть опис туру: ")

        tours.add(country, price, slots, desc)
        print("Новий тур додано")

    elif option == '4':
        print("Початок туру:", date.today())
        country = input("Введіть країну: ")
        count = int(input("Скільки місць бронюєте: "))
        start = date.today()
        days = int(input("На скільки днів тур: "))
        avance = float(input("Введіть аванс: "))

        ok = bookings.create(country, count, start, days, avance, tours)
        if ok:
            print("Бронювання створено")
        else:
            print("Не вдалося створити бронювання — недостатньо місць")

    elif option == '5':
        os.system('cls')
        while True:
            options_tours_find()
            sub = input("==> ")

            if sub == '1':
                country = input("Країна: ")
                tours.find('country', country)

            elif sub == '2':
                text = input("Введіть частину опису: ")
                tours.find('description', text)

            elif sub == '3':
                country = input("Введіть країну туру: ")
                tour = tours.get_tour(country)

                if tour:
                    while input("--- Введіть '+' щоб редагувати: ") == '+':
                        key = input("Введіть поле: ")
                        val = input("Нове значення: ")

                        if key in ["price", "slots"]:
                            val = int(val)

                        tour.edit(key, val)
                        print("Тур оновлено!")
                else:
                    print("Тур не знайдено")

            elif sub == '4':
                os.system("cls")

            elif sub == '5':
                os.system("cls")
                options()
                break

            else:
                print("Помилка вводу")

    elif option == '6':
        os.system('cls')
        while True:
            options_bookings_find()
            sub = input("==> ")

            if sub == '1':
                num = int(input("Номер бронювання: "))
                bookings.find('number', num)

            elif sub == '2':
                country = input("Країна: ")
                bookings.find('country', country)

            elif sub == '3':
                os.system("cls")

            elif sub == '4':
                os.system("cls")
                options()
                break

            else:
                print("Помилка вводу.")

    elif option == '7':
        os.system("cls")
        options()

    elif option == '8':
        tours.save_to_file(fileNameTours)
        bookings.save_to_file(fileNameBookings)
        print("Дані збережені")

    elif option == '9':
        date_finish = date.today()
        print("Бронювання буде закрите:", date_finish)
        number = int(input("Номер бронювання: "))
        full_price = float(input("Сума до оплати: "))

        ok = bookings.close(number, datetime.now(), full_price)
        if ok:
            print("Бронювання закрито")
        else:
            print("Помилка: бронювання не знайдено")

    elif option == '10':
        break

    else:
        print("Введіть коректний пункт")

print("Bye")
