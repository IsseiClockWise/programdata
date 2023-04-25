class Drink:
    def __init__(self, label, capacity):
        self._label = label
        self.capacity = capacity
    def print_info(self):
        print('{0} {1}ml'.format(self._label,self.capacity))
class Wine(Drink):
    def __init__(self, label, capacity, color, alcohol):
        super().__init__(label, capacity)
        self.color = color
        self.alcohol = alcohol
    def print_info(self):
        print('{0} {1}ml'.format(self._label,self.capacity))
        print('ワインの色{0} アルコール度数{1}'.format(self.color,self.alcohol))
class Soft_Drink(Drink):
    def __init__(self, label, capacity, category, vendor):
        super().__init__(label, capacity)
        self.category = category
        self.vendor = vendor
    def print_info(self):
        print('{0} {1}ml'.format(self._label,self.capacity))
        print('種類{0} 販売者{1}'.format(self.category,self.vendor))
wine = Wine('wine',750,'red',10)
cola = Soft_Drink('cola',500,'soda','coca cola')
wine.print_info()
cola.print_info()
