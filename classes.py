# опис товарів, що є на складі
class Product():
    def __init__ (self, name, price, count, describe):
        self.__name:str = name
        self.__price = price
        self.__count = count
        self.__rent = 0
        self.__describe = describe

# get метод для отримання значення полів класу Product
def get(self,key):
    if(key=="name"):
        value=self.__name
    elif(key=="price"):
        value=self.__price
    elif(key=="count"):
        value=self.__count
    elif(key=="describe"):
        value=self.__describe
    elif(key=="rent"):
        value=self.__rent
    else:
        print("Задано неіснуюче поле")
    return value

# метод для редагування окремого поля рядка з іменем key
def edit(self, key, value):
    if (key == "name"):
        self.__name = value
    if (key == "price"):
        self.__price = value
    if (key == "count"):
        self.__count = value
    if (key == "rent"):
        self.__rent = value
    if (key == "describe"):
        self.__describe = value

# метод дял друку рядка
def print(self):
    print("{0:20} | {1:8} | {2:5d} | {3:5d} {4}".format(
            self.__name,
            self.__price,
            self.__count,
            self.__rent,
            self.__describe,
        )
    )   

# метод для об'єднання в один рядок всіх характеристик товару
def join(self):
    return(','.join(
            (self.__name,
            str(self.__price),
            str(self.__count),
            str(self.__rent),
            self.__describe)
        )
    )

# метод для конвертування текстового рядка в набір характеристик товару
def set(self, text_row:str):
    try:
        list = text_row.split(',')
        self.__name = list[0]
        self.__price = float(list[1])
        self.__count = int(list[2])
        self.__rent = int(list[3])
        self.__describe = list[4]
        print("Convert is successfull")
        return self
    except:
        print("String isn't converted")

# клас набір товарів на складі
class Storage():
    # в цьому класі зберігається масив об'єктів класу Product і метод для роботи з цим масивом
    def __init__(self):
        self.__products = []
    # додавання нового товару
    def add(self, product):
        self.__products.append(product)

# пошук товару по назві на складі
def get(self, name):
    for product in self.__products:
        if(product.get("name") == name):
            return product

# пошук по імені і видалення з списку
def delete(self, name):
    success = False
    for i in range(len(self.__products)):
        if(self.__products[i].get("name") == name):
            self.__products.remove(self.__products[i])
            success = True
            break
    return False

# друк всіх товарів або тільки тих товарів, що доступні для оренди
def print(self, key):
    self.__print_head()
    for product in self.__products:
        if (key == "all"):
            product.print()
        if ((key == "free") and (product.get("rent") < product.get("count"))):
            product.print()
    print("-"*100)

# обчислення кількості переданого в оренду товару
def rent(self, name, count):
    success = True
    for product in self.__products:
        if(product.get("name") == name):
            rent = product.get("rent") + count
            success = product.get("count") > rent
            if (success):
                product.edit("rent", rent)
            break
    return success

# зчитувати дані з файлу "dataStorage" в клас Storage()
def read_from_file(self, fileName):
    print("Stprage start read")
    if(len(self.__products) > 0):
        print("Storage set is full")
        return
    file_reader = open (fileName, mode = 'r', encoding = 'utf-8')
    data_list = file_reader.read().strip().split('\n')
    for row in data_list:
        product = Product('',0,0,'')
        self.__products.append(product.set(row))
    file_reader.close()
    
# зберегти дані з класу Storage() у файл "dateStorage.txt"
def save_to_file(self, fileName):
    file_writer = open (fileName, mode = 'w', encoding = 'utf-8')
    for product in self.__products:
        file_writer.write(product.join() + "\n")
    file_writer.close()

# друкувати дані по пошуку
def find(self, key, value):
    self.__print_head()
    for product in self.__products:
        if(value in product.get(key)):
            product.print()
    print("-"*100)

# шукати товар за назвою
def get_product(self, value):
    for product in self.__products:
        if(value == product.get("name")):
            return product

# друкувати заголовок таблиці
def __print_head(self):
    print("-"*100)
    print("{0:20} | {1:8} | {2:5} | {3:5} | {4}".format(
            "product's name",
            "price",
            "count",
            "rent",
            "describe"
        )
    )
    print("-"*100)
    
# клас Order() - набір даних про замовлення
class Order():
    def __init__(self, number, name, count, start, days, avance):
        self.__number = number
        self.__name = name
        self.__count = count
        self.__start = start
        self.__days = days
        self.__avance = avance
        self.__finish = datetime(1990,1,1)
        self.__cost = 0

# закрити замовлення
def finish(self, date, cost):
    self.__finish = date
    self.__cost = cost

# друк одного замовлення
def print(self):
    print("{0:3d} | {2:5d} | {3:19} | {4:4d} | {5:8} | {6:19} | {7:8}".format(
            self.__number,
            self.__name,
            self.__count,
            str(self.__start),
            self.__days,
            self.__avance,
            str(self.__finish),
            self.__cost
        )
    )

# об'єднати в один рядок всі характеристики замовлення
def join(self):
    return(','.join(
            (
                str(self.__number),
                self.__name,
                str(self.__count),
                str(self.__days),
                str(self.__avance),
                str(self.__finish),
                str(self.__cost),         
            )
        )
    )

# метод для отримання значення полів класу Order
def get(self, key):
    value = 0
    if (key == "name"):
        value = self.__name
    elif (key == "number"):
        value = self.__number
    elif (key == "count"):
        value = self.__count
    elif (key == "start"):
        value = self.__start
    elif (key == "days"):
        value = self.__days
    elif (key == "avance"):
        value = self.__avance
    elif (key == "finish"):
        value = self.__finish
    elif (key == "cost"):
        value = self.__cost
    else:
        print("задано не існуюче поле")
    return value

# конвертувати текстовий рядок в набір характеристик замовлення
def set(self, text_row:str):
    list = text_row.split(',')
    try:
        self.__number = int(list[0])
        self.__name = list[1]
        self.__count = int(list[2])
        self.__start = datetime.strptime(list[3], "%Y-%m-%d %H:%M:%S")
        self.__days = int(list[4])
        self.__avance = float(list[5])
        self.__finish = datetime.strptime(list[6], "%Y-%m-%d %H:%M:%S")
        self.__cost = int(list[7])
        return self
    except:
        print("String isn't converted")
        
# клас Orders() - набір замовлень
class Orders():
    def __init__(self):
        self.__orders = []
        self.__counter = 0

# створює замовлення та збергає його набір даних
def create(self, name, count, start, days, avance):
    try:
        number = self.__counter + 1
        order =  Order(number, name, count, start, days, avance)
        self.__orders.append(order)
        self.__counter = number
        print("Creating is succesfull")
        return number
    except:
        print("Creating is failed")

# закрити замовлення за номером order_number
def close(self, order_number, date_finish, order_cost):
    success = False
    for order in self.__orders:
        if (order.get("number") == order_number):
            order.finish(date_finish, order_cost)
            success = True
            break
    return success

# роздрукувати список замовлень
def print(self):
    self.__print_head()
    for order in self.__orders:
        order.print()
    print("-"*110)

# друкувати дані по пошуку
def find(self, key, value):
    self.__print_head()
    for order in self.__orders:
        if(order.get(key) == value):
            order.print()
    print("-"*110)

# зчитати дані з файлу "dataOrders.txt" в структуру Orders()
def read_from_file(self, fileName):
    print("Orders start read")
    if(len(self.__orders) > 0):
        print("Orders are already full")
        return
    file_reader = open (fileName, mode = 'r', encoding = 'utf-8')
    data_list = file_reader.read().strip().split('\n')
    for row in data_list:
        order = Order(0,'',0,0,0,0)
        self.__orders.append(order.set(row))
    self.__counter = len(self.__orders)
    file_reader.close()

# друкувати заголовок таблиці
def __print_head(self):
    print("-"*110)
    print("{0:3} | {1:20} | {2:3} | {3:19} | {4:3} | {5:8} | {6:19} | {7:8}".format(
            "№",
            "product's name",
            "count",
            "data start",
            "days",
            "avance",
            "data end",
            "total cost"
        )
    )
    print("-"*110)

# зберегти дані з набору Orders() у файл "dataOrders.txt"
def save_to_file(self, fileName):
    file_write = open (fileName, mode = 'w', encoding = 'utf-8')
    for order in self.__orders:
        file_write.write(order.join() + '\n')
    file_write.close()

# підключення модулів для роботи з датами та рядками
from tokenize import String
from datetime import datetime

