# Michelle Martinez-Figueroa
# May 17, 2022
# WGU C950
# WGUPS
# Delivery Class

class Delivery:
    def __init__(self, id, truck, driver, start, destination):
        self.Delivery_ID = id
        self.Truck = truck
        self.Driver = driver
        self.Start_Location = start
        self.Destination = destination

    def setID(self, id):
        self.Delivery_ID = id

    def setTruck(self, truck):
        self.Truck = truck

    def setDriver(self, driver):
        self.Driver = driver

    def setStart(self, start):
        self.Start_Location = start

    def setDestination(self, destination):
        self.Destination = destination

    def getID(self):
        return self.Delivery_ID

    def getTruck(self):
        return self.Truck

    def getDriver(self):
        return self.Driver

    def getStart(self):
        return self.Start_Location

    def getDestination(self):
        return self.Destination

    def toString(self):
        return self.getID(), self.getTruck(), self.getDriver(), self.getStart(), self.getDestination()
