class PaymentProcessor():
    def __init__(self, processorID, date, time):
        self.processorID = processorID
        self.date = date
        self.time = time
        self.status = 0
        self.order = None

    def getProcessorID(self):
        return self.processorID

    def setProcessorID(self, processorID):
        self.processorID = processorID
    
    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getOrder(self):
        return self.order

    def setOrder(self, order):
        self.order = order

    def processCard(self, card, price):
        print("Paid for",price,"using",card,".")

    def refundCard(self, card, price):
        print("Refunded",price,"on",card,".")

    def __str__(self):
        return self.processorID
