from card import Card
import datetime

class CardScanner():
    def __init__(self, scannerID, date, time):
        self.scannerID = scannerID
        self.date = date
        self.time = time
        self.readerStatus = 0

    def getScannerID(self):
        return self.scannerID

    def setScannerID(self, scannerID):
        self.scannerID = scannerID

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def getReaderStatus(self):
        return self.readerStatus

    def setReaderStatus(self, readerStatus):
        self.readerStatus = readerStatus

    def scanCard(self):
        #This is hard set for now.
        card = Card(1234123412341234, "0522", 101)
        return card

    def __str__(self):
        return str(self.scannerID)
        