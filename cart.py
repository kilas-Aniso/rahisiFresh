class ShoppingCart:
    def __init__(self,quantity,price):
        self.products = []
        self.quantity = quantity
        self.price = price
    def add_item(self, product):
        # method to add a product to the shopping cart
        self.products.append(product)
    def remove_item(self, product):
        # method to remove a product from the shopping cart
        self.products.remove(product)
    def checkout(self, address, payment_method,price, quantity,product,category):
        self.adress =address
        self.payment_method = payment_method
        self.price=price
        self.quantity=quantity
        self.product=product
        self.category = category
        total = category.product.price * quantity
        return total

