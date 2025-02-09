'''
модуль для классов приложения
'''

#---------------------

class Device:
    """
    Базовый класс "Устройство" - описывает любое устройство с его общими свойствами.
    Каждое устройство имеет Название, Описание, Тип, Путь до файла с картинкой 
    """
    def __init__(self, name, description, image_path):
        """Метод инициализации объектов класса Device"""
        self.Name = name
        self.Description = description
        self.ImagePath = image_path

    def __str__(self):
        return self.Name + ", " + self.Description

#--------------------

class Card:
    """ Класс "карта" описывает обычную банковскую карту, имеет бесконечный баланс

    """
    def __init__(self, pan, pin, exp_date):
        self.PAN = pan
        self.PIN = pin
        self.ExpDate = exp_date

    def __str__(self):
        return self.PAN + ", " + self.PIN + ", " + self.ExpDate

#--------------------

class ATM(Device):
    def __init__(self, name, description, image_path):
        """Метод инициализации объектов класса ATM"""
        super().__init__(name, description, image_path)
        self.Working = False
        self.MaxAmount = 50000
        self.AmountAvailable = self.MaxAmount
        self.Devices = []
        self.InsertedCard = None
        self.LastAmount = 0

    def turn_on(self):
        self.Working = True

    def turn_off(self):
        self.Working = False
        self.LastAmount = 0

    def add_cash(self):
        self.AmountAvailable = self.MaxAmount

    def insert_card(self, card):
        self.InsertedCard = card

    def remove_card(self):
        self.InsertedCard = None

    def cash_out(self, amount):
        self.AmountAvailable = self.AmountAvailable - amount

    def set_pin(self, new_pin):
        """данный метод устанавливает новый ПИН для карты, вставленной в банкомат"""
        self.InsertedCard.PIN = new_pin

    def __str__(self):
        return "Доступно в банкомате рублей: " + str(self.AmountAvailable)





#-------------------- VISUAL
        
dev1 = Device("Принтер чеков", "Служит для печати чеков", "")
dev2 = Device("Клавиатура", "Служит для ввода пинкода и суммы", "")
dev3 = Device("Экран", "Служит для отображения информации", "")
dev4 = Device("Картридер", "Служит для чтения карты", "")
dev5 = Device("Сейф", "Содержит Касеты с купюрами разных номиналов", "")

atm1 = ATM("Банкомат", "Аппарат для выдачи и приёма денег, а также оплаты услуг и погашения кредитов без участия сотрудника банка, с использованием банковских карт.", "")
atm1.Device = [dev1, dev2, dev3, dev4, dev5]
print(atm1)

card1 = Card("123445678900", "2009", "09/26")
print(card1)
atm1.insert_card(card1)


summa = 5000
if summa > atm1.AmountAvailable:
    print("В банкомате недостаточно денег пошел вон")
else:
    atm1.cash_out(summa)



print(atm1)





