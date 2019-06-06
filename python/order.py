from payment-processor import PaymentProcessor
from menu-item import MenuItem
from card-scanner import CardScanner

class Order():
    def __init__(self, orderID, itemList, date, time, status, price, paymentStatus):
        self.orderID = orderID
        self.itemList = list()
        self.date = date
        self.time = time
        self.status = status
        self.price = price
        self.paymentStatus = paymentStatus
        self.paymentInfo = None
        self.name = None
        self.phone = None

    def getOrderID(self):
        return self.orderID

    def getItemList(self):
        return self.itemList

    def setItemList(self, index, item):
        self.itemlist[index] = item
    
    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTime(self):
        return self.time

    def setTime(time):
        self.time = time

    def getStatus(self):
        return self.status

    def setStatus(self, status)
        self.status = status

    def getPrice(self):
        return self.price

    def setPrice(price):
        self.price = price

    def getPaymentStatus(self):
        return self.paymentStatus

    def setPaymentStatus(paymentStatus):
        self.paymentStatus = paymentStatus

    def getPaymentInfo(self):
        return self.paymentInfo

    def setPaymentInfo(self, card):
        self.paymentInfo = card

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone

    def setPhone(phone):
        self.phone = phone

    def __str__(self):
        return self.orderID
