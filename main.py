class dish:
    def __init__(self,item_no, item_name, price):
        self.item_no = item_no
        self.item_name = item_name
        self.price = price

    def display_details(self):
        print(f"{self.item_no} {self.item_name} {self.price}")

class order:
    def __init__(self,order_no):
        self.order_no = order_no
        self.dishs = []
        self.total=[]


class restaurant:
    def __init__(self):
        self.menu=[]
        self.orders=[]

    #add memu
    def add_dish(self):
        item_no=int(input("Enter the item no."))
        item_name=str(input("Enter the item name."))
        price=float(input("Enter the item price."))
        self.menu.append(dish(item_no,item_name,price))
        print(f"successfully added dish {item_name} with price {price}")

    #view memu
    def view_menu(self):
        print("Dish no \t item Name \t price")
        for dish in self.menu:
            print(dish.item_no ,"\t", dish.item_name,"\t",dish.price)

    #place order
    def place_order(self):
        pass

    #genarate bill



def main():
    print("Welcome to the restaurant shop app.")


if __name__ == "__main__":
    main()




