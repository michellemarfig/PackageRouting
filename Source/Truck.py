# Michelle Martinez-Figueroa
# May 17, 2022
# WGU C950
# WGUPS
# TRuckClass

class Truck:
    def __init__(self, id, description):
        self.Truck_ID = id
        self.Description = description

    def setID (self, id):
        self.Truck_ID = id

    def setDescription(self, description):
        self.Description = description

    def getID (self):
        return self.Truck_ID

    def getDescription(self):
        return self.Description

    def toString(self):
        return self.getID(), self.getDescription()
