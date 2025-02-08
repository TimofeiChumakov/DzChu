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
    pass

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

#--------------------
        
dev1 = Device("Принтер чеков", "Служит для печати чеков", "")
dev2 = Device("Клавиатура", "Служит для ввода пинкода и суммы", "")
dev3 = Device("Экран", "Служит для отображения информации", "")
dev4 = Device("Картридер", "Служит для чтения карты", "")
dev5 = Device("Сейф", "Содержит Касеты с купюрами разных номиналов", "")

atm1 = ATM("Банкомат", "Аппарат для выдачи и приёма денег, а также оплаты услуг и погашения кредитов без участия сотрудника банка, с использованием банковских карт.", "")
atm1.Device = [dev1, dev2, dev3, dev4, dev5]

print(atm1)
