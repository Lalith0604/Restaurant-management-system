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
       order_no=int(input("Enter the order no."))
       orders=order(order_no)
       dish_id=int(input("Enter the dish no."))
       target_dish=None
       for dish in self.menu:
            if dish.item_no==dish_id:
                target_dish=dish
                break

       if not(target_dish):
            print("Sorry you cannot place order")
            return

       orders.dishs.append(target_dish)
       orders.total.append(target_dish.price)
       self.orders.append(orders)
       print("thank you for your order")


    #genarate bill
    def genarate_bill(self):
        order_no=int(input("Enter the order no."))
        target=None
        for customer in self.menu:
            if customer.item_no==order_no:
                target=customer
                break

        if not target:
            print("no order number found")
            return

        total=0
        for dish in target.total:
            total+=dish.price

        print("dish \t price")
        for dish in target:
            print(dish.item_no,"\t",dish.price)

        print(f"total amount : {total}")
        print("Thank's for ordering food")



def main():
    print("Welcome to the restaurant shop app.")


if __name__ == "__main__":
    main()




