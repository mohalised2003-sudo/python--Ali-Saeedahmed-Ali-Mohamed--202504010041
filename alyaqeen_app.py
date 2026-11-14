# Main file for the Al-Yaqeen Grocery System.

import math

import alyaqeen_core as operations


def main():
    # Product names and prices in RM
    inventory = {
        "Apple": 6.00,
        "Banana": 3.50,
        "Bread": 1.50,
        "Butter": 5.50,
        "Cheese": 8.00,
        "Chicken": 15.00,
        "Coffee": 14.00,
        "Eggs": 4.50,
        "Fish": 18.00,
        "Flour": 3.50,
        "Meat": 25.00,
        "Milk": 3.00,
        "Onion": 2.00,
        "Pasta": 4.00,
        "Potato": 3.50,
        "Rice": 12.00,
        "Salt": 1.00,
        "Soap": 2.80,
        "Sugar": 2.50,
        "Tea": 8.50,
        "Tissue": 4.00,
        "Tomato": 4.00,
        "Toothpaste": 6.50,
        "Water": 1.20
    }
    product_list = list(inventory.keys())
    cart = []

    print("*" * 42)
    print("   Welcome to Al-Yaqeen Grocery System")
    print("*" * 42)

    try:
        while True:
            print("\n--- MAIN MENU ---")
            print("1. View Products")
            print("2. View Cart")
            print("3. Checkout and Print Receipt")
            print("4. Exit")

            choice = input("\nPlease select an option (1-4): ").strip()

            if choice == "1":
                operations.display_products(inventory)
                while True:
                    num_input = input(
                        f"\nEnter product number (1-{len(product_list)}) or 0 to return: "
                    ).strip()
                    if num_input == "0":
                        break
                    if not num_input.isdigit():
                        print("[ERROR] Please enter a whole number.")
                        continue

                    product_index = int(num_input)
                    if product_index < 1 or product_index > len(product_list):
                        print(f"[ERROR] Enter a number from 1 to {len(product_list)}.")
                        continue

                    selected_item = product_list[product_index - 1]
                    qty_input = input(
                        f"Enter quantity for '{selected_item}' (or 0 to cancel): "
                    ).strip()
                    if not qty_input.isdigit():
                        print("[ERROR] Quantity must be a whole number.")
                        continue

                    quantity = int(qty_input)
                    if quantity == 0:
                        print(f"[INFO] Cancelled adding '{selected_item}'.")
                        continue
                    operations.add_to_cart(cart, inventory, selected_item, quantity)

            elif choice == "2":
                operations.display_cart(cart)
                if cart:
                    print("1. Change item quantity")
                    print("2. Remove an item")
                    print("0. Return to menu")
                    cart_choice = input("Choose an option: ").strip()

                    if cart_choice in ("1", "2"):
                        item_number = input("Enter the item number: ").strip()
                        if not item_number.isdigit():
                            print("[ERROR] Please enter a whole number.")
                        elif cart_choice == "1":
                            qty_input = input("Enter the new quantity: ").strip()
                            if qty_input.isdigit() and int(qty_input) > 0:
                                operations.change_quantity(cart, int(item_number), int(qty_input))
                            else:
                                print("[ERROR] Quantity must be a whole number greater than 0.")
                        else:
                            confirm = input("Remove this item? (y/n): ").strip().lower()
                            if confirm == "y":
                                operations.remove_from_cart(cart, int(item_number))
                            else:
                                print("[INFO] Item was not removed.")
                    elif cart_choice != "0":
                        print("[ERROR] Please choose 1, 2, or 0.")

            elif choice == "3":
                if not cart:
                    print("\n[INFO] Your cart is empty. Add items before checkout.")
                    continue

                grand_total = operations.calculate_total(cart)
                print(f"\nTotal Amount Due: RM {grand_total:.2f}")
                confirm = input("Continue to payment? (y/n): ").strip().lower()
                if confirm != "y":
                    print("[INFO] Checkout cancelled. Your cart is still saved.")
                    continue

                print("\n--- Select Payment Method ---")
                print("1. Cash")
                print("2. Card")
                print("0. Cancel and Return to Menu")
                pay_choice = input("Choose payment method (0-2): ").strip()

                if pay_choice == "0":
                    continue
                if pay_choice == "1":
                    payment_method = "Cash"
                    while True:
                        try:
                            amount_paid = float(input("Enter cash received (RM): "))
                            if not math.isfinite(amount_paid) or amount_paid < 0:
                                print("[ERROR] Enter a valid amount greater than or equal to 0.")
                            elif amount_paid < grand_total:
                                print(f"[ERROR] Still owed: RM {grand_total - amount_paid:.2f}")
                            else:
                                break
                        except ValueError:
                            print("[ERROR] Enter a valid amount, such as 20 or 20.50.")
                elif pay_choice == "2":
                    payment_method = "Card"
                    amount_paid = grand_total
                else:
                    print("[ERROR] Choose 1, 2, or 0.")
                    continue

                operations.print_receipt(cart, payment_method, amount_paid)
                cart.clear()

            elif choice == "4":
                print("\nThank you for visiting Al-Yaqeen. Have a great day!\n")
                break
            else:
                print("\n[ERROR] Please choose a number from 1 to 4.")

    except KeyboardInterrupt:
        print("\n\nProgram closed. Thank you for visiting Al-Yaqeen!")


if __name__ == "__main__":
    main()
