from datetime import datetime

class Tour:
    def __init__(self, country, price, slots, description):
        self.__country = country
        self.__price = price
        self.__slots = slots
        self.__booked = 0
        self.__description = description

    def get(self, key):
        if key == "country": return self.__country
        if key == "price": return self.__price
        if key == "slots": return self.__slots
        if key == "description": return self.__description
        if key == "booked": return self.__booked
        print("Wrong key")

    def edit(self, key, value):
        if key == "country": self.__country = value
        elif key == "price": self.__price = float(value)
        elif key == "slots": self.__slots = int(value)
        elif key == "booked": self.__booked = int(value)
        elif key == "description": self.__description = value

    def print(self):
        print("{0:15} | {1:8} | {2:5d} | {3:5d} | {4}".format(
            self.__country, self.__price, self.__slots, self.__booked, self.__description
        ))

    def join(self):
        return ",".join((
            self.__country,
            str(self.__price),
            str(self.__slots),
            str(self.__booked),
            self.__description
        ))

    def set(self, text_row):
        try:
            lst = text_row.split(',')
            self.__country = lst[0]
            self.__price = float(lst[1])
            self.__slots = int(lst[2])
            self.__booked = int(lst[3])
            self.__description = lst[4]
            return self
        except:
            print("String isn't converted")


class Catalog:
    def __init__(self):
        self.__tours = []

    # Додати тур
    def add(self, country, price, slots, desc):
        self.__tours.append(Tour(country, price, slots, desc))

    # Отримати тур по країні
    def get_tour(self, country):
        for t in self.__tours:
            if t.get("country") == country:
                return t
        return None

    # Друк
    def print(self, key="all"):
        self.__print_head()
        for t in self.__tours:
            if key == "all":
                t.print()
            elif key == "free" and t.get("booked") < t.get("slots"):
                t.print()
        print("-" * 100)

    # Бронювання місць
    def book(self, country, count):
        t = self.get_tour(country)
        if t:
            if t.get("booked") + count <= t.get("slots"):
                t.edit("booked", t.get("booked") + count)
                return True
        return False

    # Зчитування
    def read_from_file(self, filename):
        try:
            file = open(filename, 'r', encoding='utf-8')
            lines = file.read().strip().split('\n')
            for row in lines:
                if row.strip() == "":
                    continue
                self.__tours.append(Tour("", 0, 0, "").set(row))
            file.close()
        except:
            print("Error reading tours file")

    # Збереження
    def save_to_file(self, filename):
        file = open(filename, 'w', encoding='utf-8')
        for t in self.__tours:
            file.write(t.join() + "\n")
        file.close()

    # Пошук
    def find(self, key, value):
        self.__print_head()
        for t in self.__tours:
            if value.lower() in str(t.get(key)).lower():
                t.print()
        print("-" * 100)

    def __print_head(self):
        print("-" * 100)
        print("{0:15} | {1:8} | {2:5} | {3:5} | {4}".format(
            "country", "price", "slots", "booked", "description"
        ))
        print("-" * 100)

class Booking:
    def __init__(self, number, country, count, start, days, prepay):
        self.__number = number
        self.__country = country
        self.__count = count
        self.__start = start
        self.__days = days
        self.__prepay = prepay
        self.__finish = datetime(1990,1,1)
        self.__cost = 0

    def get(self, key):
        if key == "number": return self.__number
        if key == "country": return self.__country
        if key == "count": return self.__count
        if key == "start": return self.__start
        if key == "days": return self.__days
        if key == "prepay": return self.__prepay
        if key == "finish": return self.__finish
        if key == "cost": return self.__cost
        print("Wrong key")

    def finish(self, date, cost):
        self.__finish = date
        self.__cost = cost

    def print(self):
        print("{0:3d} | {1:15} | {2:3d} | {3:19} | {4:3d} | {5:8} | {6:19} | {7:8}".format(
            self.__number, self.__country, self.__count,
            str(self.__start), self.__days, self.__prepay,
            str(self.__finish), self.__cost
        ))

    def join(self):
        return ",".join((
            str(self.__number),
            self.__country,
            str(self.__count),
            str(self.__start),
            str(self.__days),
            str(self.__prepay),
            str(self.__finish),
            str(self.__cost)
        ))

    def set(self, row):
        try:
            lst = row.split(',')
            self.__number = int(lst[0])
            self.__country = lst[1]
            self.__count = int(lst[2])
            self.__start = datetime.fromisoformat(lst[3])
            self.__days = int(lst[4])
            self.__prepay = float(lst[5])
            self.__finish = datetime.fromisoformat(lst[6])
            self.__cost = float(lst[7])
            return self
        except:
            print("String isn't converted")


class Bookings:
    def __init__(self):
        self.__list = []
        self.__counter = 0

    def create(self, country, count, start, days, prepay, catalog):
        if not catalog.book(country, count):
            return False

        self.__counter += 1
        b = Booking(self.__counter, country, count, start, days, prepay)
        self.__list.append(b)
        return True

    def print(self):
        self.__head()
        for b in self.__list:
            b.print()
        print("-" * 110)

    def find(self, key, value):
        self.__head()
        for b in self.__list:
            if b.get(key) == value:
                b.print()
        print("-" * 110)

    def close(self, number, finish_date, cost):
        for b in self.__list:
            if b.get("number") == number:
                b.finish(finish_date, cost)
                return True
        return False

    def read_from_file(self, filename):
        try:
            file = open(filename, 'r', encoding='utf-8')
            lines = file.read().strip().split("\n")
            for row in lines:
                if row.strip() == "":
                    continue
                b = Booking(0, "", 0, datetime.now(), 0, 0)
                b = b.set(row)
                self.__list.append(b)
                self.__counter += 1
            file.close()
        except:
            print("Error reading bookings file")

    def save_to_file(self, filename):
        file = open(filename, 'w', encoding='utf-8')
        for b in self.__list:
            file.write(b.join() + "\n")
        file.close()

    def __head(self):
        print("-" * 110)
        print("{0:3} | {1:15} | {2:3} | {3:19} | {4:3} | {5:8} | {6:19} | {7:8}".format(
            "№","country","qty","start","days","prepay","finish","cost"
        ))
        print("-" * 110)
