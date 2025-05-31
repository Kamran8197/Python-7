from book import Book
from order_manager import OrderManager

def main():
    order_manager = OrderManager()
    while True:
        print("\n1. Kitab əlavə et")
        print("2. Kitab sil")
        print("3. Ümumi qiymət")
        print("4. Sifarişləri yaz")
        print("5. Çıxış")
        choice = input("Seçiminizi edin: ")

        if choice == '1':
            title = input("Kitabın adını daxil edin: ")
            author = input("Müəllifin adını daxil edin: ")
            genre = input("Janrı daxil edin: ")
            price = float(input("Qiyməti daxil edin: "))
            stock = int(input("Stokda sayı daxil edin: "))
            book = Book(title, author, genre, price, stock)
            order_manager.add_book(book)

        elif choice == '2':
            title = input("Silinəcək kitabın adını daxil edin: ")
            for book in order_manager.cart:
                if book.title == title:
                    order_manager.remove_book(book)
                    break
            else:
                print("Belə bir kitab səbətdə yoxdur.")

        elif choice == '3':
            print(f"Ümumi qiymət: {order_manager.total_price()}")

        elif choice == '4':
            order_manager.save_orders()
            print("Sifarişlər fayla yazıldı.")

        elif choice == '5':
            break

        else:
            print("Yanlış seçim, yenidən cəhd edin.")

if __name__ == "__main__":
    main()