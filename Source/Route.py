# Michelle Martinez-Figueroa
# May 17, 2022
# WGU C950
# WGUPS
# Route Class

import xlrd

class Route:
    def __init__(self, time):
        # self.Time = time
        # self.checkStart()

        self.table = []

        # self.Deliveries_Completed = 0

        # self.readFiles()

    # def checkStart(self):
    #     if self.Time == '8:00':
    #         print('It is 8:00 AM. Time to start deliveries')
    #
    # def checkStop(self, driver1, driver2):
    #     if driver1.getDeliveries_Made(self) + driver2.getDeliveries_Made(self) == 40:
    #         print('Deliveries Completed!')

    #calculate deliveries algo

    #read file for distances
    def readFiles(self):
        pass
        # packageLoc = "Files\Package_Table.xlsx"
        # packageFile = xlrd.open_workbook(packageLoc)
        # packageSheet = packageFile.sheet_by_index(0)
        #
        # packageSheet.cell_value(0, 0)
        #
        # packageColNames = []
        #
        # for i in range(packageColNames):
        #     packageColNames.add(packageSheet.cell_value(0, i))
        #
        # for s in range(packageColNames):
        #     print(s)

