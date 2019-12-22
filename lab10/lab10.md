# ЛАБОРАТОРНА РОБОТА № 10

## Завдання 1

| **Об'єкт** | **Число** |
| ------ | ------ |
| **Поля** | для зберігання натурального числа; |
| **Методи** | введення числа; |
|    | виведення числа; |
|    | знаходження кількості цифр; |
|    | знаходження суми цифр. |


```py
class Number:
    def __init__(self, number):
        self.number = number

    def enter_num(self):
        self.number = int(input('Enter num: '))
        return self.number

    def print_num(self):
        print(self.number)

    def num_count(self):
        return len(str(self.number))

    def sum_nums(self):
        return sum(map(int, str(self.number)))

    def __str__(self):
        return str(self.number)


num = Number(541)
print('Number is {0}'.format(num.print_num()))
print('Count of digits in {0} is {1}'.format(num, num.num_count()))
print('Sum of number in {0} is {1}'.format(num, num.sum_nums()))
num.enter_num()
num.print_num()
```


## Завдання 2

| **Об'єкт** | **Автомобіль(використати члени-класи)** |
| ------ | ------ |
| **Поля** | марка; |
|  | відомості про виробника (член-клас) (назва фірми, рік заснування, номер телефону, обсяги виробництва); |
|  | відомості про продавця (член-клас) (назва фірми, рік заснування, номер телефону, обсяги продажу); |
|  | відомості про власника (член-клас) (прізвище та ініціали,ідентифікаційний код) | [plugins/onedrive/README.md][PlOd] |
|  | колір; |
|  | номер; |
|  | дата випуску (член-клас);|
| **Методи** | Визначення віку автомобіля |
|        | Зміни власника  |

```py
import datetime

class Date:
    def __init__(self, year, month, day):
        if month > 12 or month < 1:
            raise Exception("wrong month")

        if day > 31 or day < 1:
            raise Exception("wrong day")

        self.__year = year
        self.__month = month
        self.__day = day
        self.__date = datetime.date(year, month, day)

    def __str__(self):
        return "{0:02}.{1:02}.{2}".format(self.__day, self.__month, self.__year)

    def get_date(self):
        return self.__date


class Producer:
    def __init__(self, prod_name, prod_year, prod_phone, production):
        self.prod_name = prod_name
        self.prod_year = prod_year
        self.prod_phone = prod_phone
        self.production = production

    def __str__(self):
        return " Name of producer: {0}\n Foundation year: {1}\n " \
               "Phone: {2}\n production volume: {3}".format(self.prod_name,
                            self.prod_year, self.prod_phone, self.production)


class Seller:
    def __init__(self, sell_name, sell_year, sell_phone, sales):
        self.sell_name = sell_name
        self.sell_year = sell_year
        self.sell_phone = sell_phone
        self.sales = sales

    def __str__(self):
        return " Name of seller: {0}\n Foundation year: {1}\n" \
               " Phone: {2}\n Sales: {3}".format(self.sell_name, self.sell_year,
                                                 self.sell_phone, self.sales)


class Owner:
    def __init__(self, full_name, code):
        self.full_name = full_name
        self.code = code

    def __str__(self):
        return " Name of owner: {0}\n Code: {1}".format(self.full_name, self.code)


class Automobile:
    def __init__(self, brand, color, number,  production_date, producer, seller, owner):
        self.brand = brand
        self.color = color
        self.number = number
        self.production_date = production_date
        self.producer = producer
        self.seller = seller
        self.owner = owner

    def get_age(self):
        return abs((datetime.date.today() - self.production_date.get_date()).days)//365

    def change_owner(self, changed_user):
        self.owner = changed_user
        return self.owner


date = Date(2017, 5, 21)
prod = Producer('Hyundai Motor Group', 1967, 3134775, 1000000)
seller = Seller('SellingCars', 2000, 22534, 20000)
own = Owner('Ivanov Ivan', 113)

auto = Automobile('Hyundai', 'black', 1991, date, prod, seller, own)
print('Age of car is {0}'.format(auto.get_age()))
print('New owner of car is {0}'.format(auto.change_owner('Kate')))
```
