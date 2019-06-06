from card_scanner import CardScanner
from card import Card
from menu_item import MenuItem
from order import Order
from payment_processor import PaymentProcessor

#Creating and scanning a card.
scan = CardScanner(1, "5/28/2019", "2:41")
card = scan.scanCard()
print(card)

#Creating an order with two items
myItem1 = MenuItem(1, "pizza", 10.99)
myItem2 = MenuItem(2, "soda", 2.99)

myList = [myItem1, myItem2]

myOrder = Order(1, myList, "6/6/2019", "1:13", 0, False)
print(myList[0])
print(str(myItem1.getItemPrice()))
myPrice = myOrder.getPrice()
print(str(myPrice))

#Paying for food
myProcessor = PaymentProcessor(1,"6/6/2019", "1:13")
myProcessor.processCard(card, myPrice)
myProcessor.refundCard(card, myPrice)