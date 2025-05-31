class OrderManager:
    def __init__(self):
        self.cart = []
        self.authors = set()
        self.genres = set()

    def add_book(self, book):
        if book.stock > 0:
            self.cart.append(book)
            self.authors.add(book.author)
            self.genres.add(book.genre)
            book.stock -= 1
        else:
            print(f"{book.title} kitabı stokda yoxdur.")

    def remove_book(self, book):
        if book in self.cart:
            self.cart.remove(book)
            book.stock += 1
        else:
            print(f"{book.title} kitabı səbətdə yoxdur.")

    def total_price(self):
        return sum(book.price for book in self.cart)

    def save_orders(self):
        with open("orders.txt", "a") as file:
            for book in self.cart:
                file.write(f"{book.title}, {book.author}, {book.price}\n")
