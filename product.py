class Product:
    products = []

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    
    def add_product(cls, product):
        cls.products.append(product)

    
    def find_product_by_name(cls, name):
        for product in cls.products:
            if product.name == name:
                return product
        return None

    
    def find_product_by_price(cls, price):
        for product in cls.products:
            if product.price == price:
                return product
        return None
