class Storage:
    storage = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            Storage.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return Storage.storage


# Part below is test code from example

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

#################################### TASK CONDITION ############################
'''
                               1.	Storage
Create a class Storage. The __init__ method should accept one 
parameter - the capacity of the storage. The Storage class should also have an
 attribute called storage - empty list, where all the items will be stored. 
The class should have two additional methods:
•	add_product(product: str) - adds the product in the storage if there is enough space for it
•	get_products() - returns the storage list

_______________________________________________
Example

Test Code	(no input data in this task)

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

Output
["apple", "banana", "potato", "tomato"]

'''
