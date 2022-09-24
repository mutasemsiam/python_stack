from pickle import APPEND


class Store:
    def __init__(self, storename, productlist):
        self.name = storename
        self.products = [productlist]

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        self.products.remove(id)
        print("Product:", self.products[id])

    def inflation(self, percent_increase):
        for product in self.products:
            product = product + product*percent_increase
    
    def set_clearance(self, category, percent_discount):
        pass
        

class Product:
    def __init__(self, productname = "", price = 0, category = ""):
        self.product_name = productname
        self.price = price
        self.category = category
        self.products =  Store(storename = "", productlist = 0)

    def update_price(self, percent_change, is_increased = False):
        if is_increased == True:
            self.price = self.price + self.price*percent_change
        elif is_increased == False:
            self.price = self.price - self.price*percent_change

    def print_info(self):
        print("Product name:", self.product_name,"| Category:", self.category,"| Price:", self.price )

store_m = Store("Allure", 0)
product1 = Product("Mango", 25, "Fruit")
product2 = Product("Apple", 30, "Fruit")
product3 = Product("Tomato", 15, "Vegs")

# product1.print_info()
# product1.update_price(0.1, False)
# print(store_m.products)
store_m.add_product("mango")
store_m.add_product("panana")
store_m.add_product("watermilon")
print(store_m.products)


