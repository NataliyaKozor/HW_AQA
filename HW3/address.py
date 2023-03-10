
class Address:
 
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def info(self):
        return self.city + ", " + self.street + ", " + self.house + "-" + self.apartment 

class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def info_mailing(self):
        print("Отправление " + self.track + " из " + self.from_address + " в " + self.to_address + ". Стоимость " + str(self.cost) + " рублей.")
