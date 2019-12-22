class Bus:
    def __init__(self, number, fromm, to, driver, price, departure, arrival):
        self.number = number
        self.fromm = fromm
        self.to = to
        self.driver = driver
        self.price = price
        self.departure = departure
        self.arrival = arrival

    def get_number(self):
        return self.number

    def get_from(self):
        return self.fromm

    def get_to(self):
        return self.to

    def get_driver(self):
        return self.driver

    def get_price(self):
        return self.price

    def get_departure(self):
        return self.departure

    def get_arrival(self):
        return self.arrival

    def get_info(self):
        return "Bus Num - {0} \n From - {1} \n To - {2} \n Bus Driver - {3}\n " \
               "Bus Price - {4}\n Departure time - {5}\n" \
               " Arrival Time - {6}\n".format(self.number,
                self.fromm, self.to, self.driver, self.price,
                self.departure, self.arrival)


class BusStation:
    def __init__(self):
        self.all_buses = []

    def add_bus(self, new_bus):
        self.all_buses.append(new_bus)

    def get_bus(self):
        return self.all_buses


user_bus = []

bus2 = BusStation()
bus2.add_bus(Bus('1', 'Uzhgorod', 'Mukachevo', 'Ivan', '120', '7.25', '9.00'))
bus2.add_bus(Bus('2', 'Uzhgorod', 'Lviv', 'Petro', '180', '6.40', '10.15'))
bus2.add_bus(Bus('3', 'Kyiv', 'Lviv', 'Yuriy', '460', '11.30', '16.00'))
user_bus.append(bus2)

bus1 = BusStation()
while True:
    print('Search by:\n--number\n--from\n--to\n--driver\n--price\n'
          '--departure\n--arrival\n--all buses\n--add bus\n--exit')
    choice = input('My choice: ')

    if choice == 'exit':
        break
    elif choice == 'all buses':
        for buses in user_bus:
            for bus in buses.get_bus():
                print('\n', bus.get_info())

    elif choice == 'add':
        bus1.add_bus(Bus(input('Number: '), input('From: '), input('To: '), input('Driver: '), input('Price: '),
                         input('Departure: '), input('Arrival: ')))
        user_bus.append(bus1)
        continue
    elif choice == 'from':
        user_from = input('From: ')
        for buses in user_bus:
            for bus in buses.get_bus():
                if bus.get_from() == user_from:
                    print('\n', bus.get_info())

    elif choice == 'to':
        user_to = input('To: ')
        for buses in user_bus:
            for bus in buses.get_bus():
                if bus.get_to() == user_to:
                    print('\n', bus.get_info())

    elif choice == 'driver':
        user_driver = input('Driver: ')
        for buses in user_bus:
            for bus in buses.get_bus():
                if bus.get_driver() == user_driver:
                    print('\n', bus.get_info())

    elif choice == 'price':
        print('Enter range of price')
        max_price = int(input('Max price: '))
        min_price = int(input('Min price: '))
        for buses in user_bus:
            for bus in buses.get_bus():
                if min_price <= int(bus.get_price()) <= max_price:
                    print('\n', bus.get_info())

    elif choice == 'number':
        user_num = int(input('Num: '))
        for buses in user_bus:
            for bus in buses.get_bus():
                if int(bus.get_number()) == user_num:
                    print('\n', bus.get_info())

    elif choice == 'departure':
        print('Enter range of departure time')
        max_departure = float(input('Latest: '))
        min_departure = float(input('Earliest: '))
        for buses in user_bus:
            for bus in buses.get_bus():
                if min_departure <= int(bus.get_departure()) <= max_departure:
                    print('\n', bus.get_info())

    elif choice == 'arrival':
        print('Enter range of arrival time')
        max_arrival = float(input('Latest: '))
        min_arrival = float(input('Earliest: '))
        for buses in user_bus:
            for bus in buses.get_bus():
                if min_arrival <= float(bus.get_arrival()) <= max_arrival:
                    print('\n', bus.get_info())

    else:
        print('Try again!')
