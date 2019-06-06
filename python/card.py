class Card():
    def __init__(self, cardNumber, cardExpiration, cardCVV):
        self.cardNumber = cardNumber
        self.cardExpiration = cardExpiration
        self.cardCVV = cardCVV

    def getCardNumber(self):
        return self.cardNumber

    def getCardExpiration(self):
        return self.cardExpiration

    def getCardCVV(self):
        return self.cardCVV

    def __str__(self):
        return str(self.cardNumber)