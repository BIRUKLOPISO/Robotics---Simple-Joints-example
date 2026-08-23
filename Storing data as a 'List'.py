class ShoppingCart:
    def __init__(self):
        self.items = ["Welcome Gift"]  # ← Starts with 1 item already

    def add_item(self, item):
        self.items.append(item)


cart = ShoppingCart()
print(cart.items)  # Output: ['Welcome Gift']  ← From constructor
cart.add_item("Book")
print(cart.items)  # Output: ['Welcome Gift', 'Book']