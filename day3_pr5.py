from abc import ABC
class Mobile(ABC):
    def operatingsystem():
        pass
    def calling():
        print("provides calling")
class moto(Mobile):
    def Operatingsystem():
        print('Andriod')
class nokia(Mobile):
    def Operatingsystem():
        print('Android')
class iphone(Mobile):
    def Operatingsystem():
        print('ios')
obj=Mobile
moto.Operatingsystem()
moto.calling()
nokia.Operatingsystem()
iphone.calling()
