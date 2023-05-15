class ProductCategory:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def search_products(self, query):
        # method to search for products based on user's query
        results = []
        for product in self.products:
            if query in product.name.lower():
                results.append(product)
        return results
    def filter_products(self, category):
        # method to filter products based on user's selected category
        results = []
        for product in self.products:
            if category == product.category:
                results.append(product)
        return results
    def add_product(self, product):
    # method to add a new product to the category
      self.products.append(product)
    def remove_product(self, product):
    # method to remove a product from the category
      self.products.remove(product)