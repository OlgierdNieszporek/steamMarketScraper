class ProductModel:
    def __init__(self):
        pass
    def __init__(self, id, productName, productPrice, date):
        self.id = id
        self.productName = productName
        self.productPrice = productPrice
        self.date = date

    def __str__(self):
        return f'Product:{self.id} {self.productName} {self.productPrice} {self.last_name} {self.date}'
