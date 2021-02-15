class Invoice:
    def __init__(self, invoiceNumber, invoiceDate, company, companyAddress, billToName, billToAddress, invoiceItemHeadNode):
        self.invoiceNumber = invoiceNumber
        self.invoiceDate = invoiceDate
        self.company = company
        self.companyAddress = companyAddress
        self.billToName = billToName
        self.billToAddress = billToAddress
        self.invoiceItemHeadNode = invoiceItemHeadNode

    def amountDue(self, taxes):
        total = 0
        currentItem = self.invoiceItemHeadNode
        while currentItem != None:
            total += currentItem.getTotalPrice()
            currentItem = currentItem.next

        if taxes == True:
            total = total * 1.1

        return total

    def printBuyingItems(self):
        currentItem = self.invoiceItemHeadNode
        while currentItem != None:
            print("item :{}, price : {}, quantity : {}".format(currentItem.product.title, currentItem.product.price, currentItem.quantity))
            currentItem = currentItem.next

    def printInvoice(self):
        print("Invoice")
        print("No. : " + self.invoiceNumber)
        print("INVOICE Date : " + self.invoiceDate)
        print("SHIP TO : " + self.company)
        print("ADDRESS : " + self.companyAddress)
        print("BILL TO : " + self.billToName)
        print("ADDRESS : " + self.billToAddress)

        currentItem = self.invoiceItemHeadNode
        while currentItem != None:
            print("{}(${})--- {} pcs. --- AMOUNT: {}".format(currentItem.product.title, currentItem.product.price, currentItem.quantity, currentItem.getTotalPrice()))
            currentItem = currentItem.next

        print("SUBTOTAL : " + str(self.amountDue(False)))
        print("TAX : {}".format(self.amountDue(True) - self.amountDue(False)))
        print("TOTAL : " + str(self.amountDue(True)))

class InvoiceItemNode:
    def __init__(self, quantity, product):
        # このノードは、ノードと次のノードの値の、2つのインスタンス変数を持ちます。
        self.quantity = quantity
        self.product = product
        self.next = None
    
    def getTotalPrice(self):
        return self.product.price * self.quantity

    
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# shampoo, $10, 7pc
# conditioner, $5, 9pc
# tooth brush, $3, 10pc
product1 = Product("shampoo", 10)
product2 = Product("conditioner", 5)
product3 = Product("tooth brush", 3)

item1 = InvoiceItemNode(7, product1)
item2 = InvoiceItemNode(9, product2)
item1.next = item2
item3 = InvoiceItemNode(10, product3)
item2.next = item3

# invoice
# UC1234567890
# 2020/05/06
# Recursion
# Los Angles
# Steven
# Dallas

invoice = Invoice("UC1234567890", "2020/05/06", "Recursion", "Los Angeles", "Steven", "Dallas", item1)
invoice.printBuyingItems()
invoice.printInvoice()