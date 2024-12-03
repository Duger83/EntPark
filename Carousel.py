from Maintanance import Maintanance
from Ticket import Ticket

class Carousel(Maintanance):
    
    pass
    
    def __init__(self, title:str, capacity:int, price:int):
        self.title = title
        self.capacity = capacity
        self.price = price
    
    def order(self):
        print('Распечатывает список билетов на карусель')
        for i in range(self.capacity):
            print(Ticket(i+1, self.price))