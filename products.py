class Product: #classs
    def __init__(self, product_name, product_price): #initializer
        self.product_name = product_name
        self.product_price = product_price
        
    def get_name(self):
        return self.product_name
    
    def set_name(self, name):
        self.product_name = name
        
p1 = Product("Laptop", 157000)
print(p1.product_name)
print(p1.get_name())
p1.set_name("tablet")
print(p1.get_name())

# class Node:
#     def __init__(self, data, link):
#         self.data = data
#         self.link = link