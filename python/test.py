import unittest

from order import Order
from card import Card
from card_scanner import CardScanner
from payment_processor import PaymentProcessor
from menu_item import MenuItem

class MenuItemTest(unittest.TestCase):
    def setUp(self):
        self.myItem = MenuItem(1,"pizza",10.99)

    def test_string(self):
        self.assertEqual(str(self.myItem), self.myItem.itemName)

    def test_price(self):
        self.assertEqual(self.myItem.getItemPrice(), self.myItem.itemPrice)

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.myItem1 = MenuItem(1,"pizza",10.99)
        self.myItem2 = MenuItem(2,"soda",2.99)
        self.myList = [self.myItem1, self.myItem2]
        self.myOrder = Order(1,self.myList,"6/6/2019", "2:00", 0, False)

    def test_string(self):
        self.assertEqual(str(self.myOrder), str(self.myOrder.orderID))

    def test_price(self):
        self.assertEqual(self.myOrder.getPrice(), 13.98)

class CardTest(unittest.TestCase):
    def setUp(self):
        self.myCard = Card(1234123412341234, "0220", 123)

    def test_string(self):
        self.assertEqual(str(self.myCard), str(self.myCard.cardNumber))

    def test_date(self):
        self.assertEqual(self.myCard.cardExpiration, self.myCard.getCardExpiration())

class CardScannerTest(unittest.TestCase):
    def setUp(self):
        self.myScanner = CardScanner(1, "6/6/2019", "2:00")
        self.myCard = Card(1234123412341234, "0522", 101)

    def test_status(self):
        self.assertEqual(self.myScanner.getReaderStatus(), self.myScanner.readerStatus)

    def test_scan_card(self):
        self.assertEqual(str(self.myCard), str(self.myScanner.scanCard()))

class PaymentProcessorTest(unittest.TestCase):
    def setUp(self):
        self.myProcessor = PaymentProcessor(1, "6/6/2019", "2:00")
        self.myItem1 = MenuItem(1,"pizza",10.99)
        self.myItem2 = MenuItem(2,"soda",2.99)
        self.myList = [self.myItem1, self.myItem2]
        self.myOrder = Order(1,self.myList,"6/6/2019", "2:00", 0, False)

    def test_order(self):
        self.myProcessor.setOrder(self.myOrder)
        self.assertEqual(str(self.myOrder), str(self.myProcessor.getOrder()))

    def test_date(self):
        self.assertEqual(self.myProcessor.getDate(), self.myProcessor.date)
