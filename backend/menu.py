menu_items = {
    "Sadza & Beef Stew": 3.50,
    "Chicken Burger": 2.00,
    "Vegetable Rice": 1.50,
    "Fish & Chips": 4.00,
    "Fruit Salad": 1.00
}

def get_menu(cafeteria_name):
    print(f"Menu for {cafeteria_name}:")
    for item, price in menu_items.items():
        print(f"  {item}: ${price}")
