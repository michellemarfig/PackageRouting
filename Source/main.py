# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from Source.Delivery import Delivery
from Driver import Driver
from Source.Route import Route
from Source.Truck import Truck

if __name__ == '__main__':
    d1 = Driver(1, 'john', 40)
    t1 = Truck(1, 'truck 1')
    del1 = Delivery(1, t1, d1, 0, 5)
    r1 = Route('8:00')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
