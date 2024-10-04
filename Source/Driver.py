# Michelle Martinez-Figueroa
# May 17, 2022
# Driver Class

class Driver:
    def __init__(self, id, name, deliveries):
        self.Driver_ID = id
        self.Name = name
        self.Deliveries_Made = deliveries

    def setID(self, id):
        self.Driver_ID = id

    def setName(self, name):
        self.Name = name

    def setDeliveriesMade(self, deliveries):
        self.Deliveries_Made = deliveries

    def getID(self):
        return self.Driver_ID

    def getName(self):
        return self.Name

    def getDeliveriesMade(self):
        return self.Deliveries_Made

    def toString(self):
        return self.getID(), self.getName(), 'Deliveries Made:', self.getDeliveriesMade()

