class MenuItem():
    def __init__(self, itemID, itemName, itemPrice):
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemMods = list()

    def getItemID(self):
        return self.itemID

    def setItemID(self, itemID):
        self.itemID = self.itemID

    def getItemName(self):
        return self.itemName

    def setItemName(self, name):
        self.itemName = self.itemName

    def getItemPrice(self):
        return self.itemPrice

    def setItemPrice(self, itemPrice):
        self.itemPrice = itemPrice

    def getItemMods(self):
        return self.itemMods

    def setItemMods(self, index, val):
        self.itemMods[index] = val

    def __str__(self):
        return self.itemName