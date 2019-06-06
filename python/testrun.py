from card-scanner import CardScanner
from card import Card
from menu-item import MenuItem
from order import Order
from payment-processor import PaymentProcessor

#Creating and scanning a card.
scan = CardScanner(1, "5/28/2019", "2:41")
card = scan.scanCard()
print("Hi!")