# Michelle Martinez-Figueroa
# May 17, 2022
# WGU C950
# WGUPS
# package Class

class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes):
        self.Package_ID = id
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zip
        self.Deadline = deadline
        self.Mass = mass
        self.Notes = notes

    def toString(self):
            return self.getID(), self.getAddress(), self.getCity(), self.getState(), self.getZip(), self.getDeadline(), self.getMass(), self.getNotes()

    def setID (self, id):
        self.Package_ID = id;

    def setAddress(self, address):
        self.Address = address

    def setCity(self, city):
        self.City = city

    def setState(self, state):
        self.State = state

    def setZip(self, zip):
        self.Zip = zip

    def setDeadline(self, deadline):
        self.Deadline = deadline

    def setMass(self, mass):
        self.Mass = mass

    def setNotes(self, notes):
        self.Notes = notes

    def getID(self):
        return self.Package_ID

    def getAddress(self):
        return self.Address

    def getCity(self):
        return self.City

    def getState(self):
        return self.State

    def getZip(self):
        return self.Zip

    def getDeadline(self):
        return self.Deadline

    def getMass(self):
        return self.Mass

    def getNotes(self):
        return self.Notes
