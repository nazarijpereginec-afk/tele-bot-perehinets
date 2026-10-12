from datetime import date 
from datetime import datetime
import os

from classes import Orders, Product, Storage

fileNameStorage = "dataStorage.txt"
fileNameOrders = "dataOrders.txt"
orders = Orders()
storage = Storage()

def options():
    print("\n--------------ГОЛОВНЕ МЕНЮ--------------")
    print("1: Список товарів на складі")
    print("2: Список замовлень")
    print("3: Список товарів, доступних для прокату")
    print("4: Додати новий товар")
    print("5: Ввід нового замовлення")
    print("6: Пошук на складі")
    print("7: Пошук серед замовлень")
    print("8: Очистити вікно")
    print("9: Зберегти дані у файл")
    print("10: Закрити замовлення")
    print("11: EXIT")

def options_storage_find():
    print("\n-------ПОШУК ТОВАРІВ-------")
    print("1: Пошук за назвою товару")
    print("2: Пошук за описом")
    print("3: Редагувати товар")
    print("4: Очистити вікно")
    print("5: Повернутися у основне меню")

def options_orders_find():
    print("\n-------ПОШУК ЗАМОВЛЕНЬ-------")
    print("1: Пошук за номером")
    print("2: Пошук за назвою товару")
    print("3: Редагувати замовленння")
    print("4: Очистити вікно")
    print("5: Повернутися у основне меню")

storage.read_from_file(fileNameStorage)
orders.read_from_file(fileNameOrders)

while True: 
    option = int(input("--Виберіть пункт меню: "))
    if option == 1:
        storage.print("all")
    elif option == 2:
        orders.print()
    elif option == 3:
        orders.print("free")
    elif option == 4:
        name=input("Введіть назву товару: ")
        price=input("Введіть ціну товару: ")
        count=input("Введіть кількість: ")
        describe=input("Введіть короткий опис: ")
        storage.add(Product(name,float(price), int(count), describe))
        print("Adding new product is success")
    elif option == 45:
        name=input("Введіть назву товару: ")
        storage.delete(name)
    elif option == 5:
        print('Початком оренди є сьогоднішня дата:', date.today())
        name=input("Введіть назву товару: ")
        count=int(input("Введіть кількість: "))
        start=date.today()
        days=int(input("Введіть кількість днів прокату: "))
        avance = float(input("Введіть внесений аванс: "))
        orders.create(name, count, start, days, avance)
        print("New order created")
        
    elif option == 6:
        os.system('cls')
        while True:
            options_storage_find()
            option = input("--Виберіть пнутк меню: ")
            if option == '1':
                name = input("Введіть назву повністю або частину: ")
                storage.find('name', name)
            elif option == '2':
                text=input("Введіть характеристику з опису: ")
                storage.find('describe', text)
            elif option == '3':
                name = input("--Введіть нрразву повністю: ")
                product = storage.get_product(name)
                if(product):
                    while input("---Введіть '+' щоб продовжити редагування: ") == '+':
                        key = input("Введіть назву поля: ")
                        value = input("Введіть нове значення: ")
                        if(key in "pricecount"):
                            value = int(value)
                        product.edit(key, value)
                        print("!!! Редагування заверешене успішно")
                else:
                    print("!!! Товар " + name + " не знайдено")
            elif option == '4':
                os.system('cls')
            elif option == '5':
                os.system('cls')
                options()
                break
            else:
                print("Виберіть коректне значення")
            
    elif option == 7:
        os.system('cls')
        while True:
            options_orders_find()
            option = input("--Виберіть пункт менб: ")
            if option == '1':
                number = int(input("Введіть номер замовлення: "))
                orders.find('number', number)
            elif option == '2':
                name = input("Введіть точну назву товару: ")
                orders.find('name', name)
            elif option == '3':
                os.system('cls')
            elif option == '4':
                os.system('cls')
                options()
                break
            else:
                print("Виберіть коректне значення")
    
    elif option == 9:
        storage.save_to_file(fileNameStorage)
        orders.save_to_file(fileNameOrders)
        print("Saving file is success")
    elif option == 10:
        date_finish = date.today()
        print("Замовлення буде закрито сьогоднішньою датою!", date_finish)
        order_number = int(input("Введіть номер замовлення: "))
        order_cost = int(input("Введіть вартість оренди: "))
        success = orders.close(order_number, datetime(date_finish.year, date_finish.month, date_finish.day), order_cost)
        if(success):
            print("Order N", order_number, " closed")
        else:
            print("Order N", order_number, " dpn't closed")
    elif option == 11:
        break
    else:
        print("Input menu number, pls\n")
print("By by!!!")
            
