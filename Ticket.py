class Ticket():
    
    def __init__(self, number:int, price:int):
        self.number = number
        self.price = price
    
    def __str__(self):
        return 'Билет №'+str(self.number)+', цена - '+str(self.price)    
