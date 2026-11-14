# Functions used by the grocery system.

import datetime


def display_products(inventory):
    """Show the products and their prices."""
    print("\n" + "=" * 40)
    print("           AVAILABLE PRODUCTS")
    print("=" * 40)
    for index, (item, price) in enumerate(inventory.items(), start=1):
        print(f" {index:>2}. {item:<16} RM {price:.2f}")
    print("=" * 40)


def calculate_total(cart):
    """Return the total cost of the cart."""
    return sum(item["total_price"] for item in cart)


def display_cart(cart):
    """Show the items currently in the cart."""
    if not cart:
        print("\n[INFO] Your shopping cart is empty.")
        return

    print("\n" + "-" * 42)
    print("              SHOPPING CART")
    print("-" * 42)
    for index, item in enumerate(cart, start=1):
        print(
            f"{index}. {item['item']:<15} "
            f"RM {item['unit_price']:.2f} each "
            f"(x{item['quantity']:<2}) = RM {item['total_price']:>7.2f}"
        )
    print("-" * 42)
    print(f"Total Amount :           RM {calculate_total(cart):>7.2f}")
    print("-" * 42)


def add_to_cart(cart, inventory, item_name, quantity):
    """Add an item, or increase its quantity if it is already in the cart."""
    if item_name not in inventory or quantity <= 0:
        print("[ERROR] Product or quantity is not valid.")
        return

    price = inventory[item_name]
    for item in cart:
        if item["item"] == item_name:
            item["unit_price"] = price
            item["quantity"] += quantity
            item["total_price"] = item["quantity"] * price
            print(f"[SUCCESS] Updated '{item_name}' quantity to {item['quantity']}.")
            return

    cart.append({
        "item": item_name,
        "quantity": quantity,
        "unit_price": price,
        "total_price": price * quantity
    })
    print(f"[SUCCESS] Added {quantity}x '{item_name}' to your cart.")


def remove_from_cart(cart, item_number):
    """Remove one product from the cart by its number."""
    if item_number < 1 or item_number > len(cart):
        print("[ERROR] Please enter a number shown in the cart.")
        return

    removed_item = cart.pop(item_number - 1)
    print(f"[SUCCESS] Removed '{removed_item['item']}' from your cart.")


def change_quantity(cart, item_number, quantity):
    """Change the quantity of one product in the cart."""
    if item_number < 1 or item_number > len(cart):
        print("[ERROR] Please enter a number shown in the cart.")
        return
    if quantity <= 0:
        print("[ERROR] Quantity must be greater than 0.")
        return

    item = cart[item_number - 1]
    item["quantity"] = quantity
    item["total_price"] = item["unit_price"] * quantity
    print(f"[SUCCESS] Updated '{item['item']}' quantity to {quantity}.")


def print_receipt(cart, payment_method, amount_paid):
    """Print the receipt with the payment and change."""
    print("\n" + "=" * 45)
    print("            AL-YAQEEN SUPERMARKET")
    print("      Persiaran Multimedia, Cyberjaya")
    print("=" * 45)

    now = datetime.datetime.now()
    print(f"Date & Time   : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 45)

    grand_total = calculate_total(cart)
    for item in cart:
        print(
            f"{item['item']:<15} RM {item['unit_price']:.2f} each "
            f"(x{item['quantity']:<2}) - RM {item['total_price']:>7.2f}"
        )

    print("-" * 45)
    print(f"TOTAL AMOUNT DUE :          RM {grand_total:>7.2f}")
    print(f"Paid ({payment_method})      :          RM {amount_paid:>7.2f}")
    change = amount_paid - grand_total if payment_method == "Cash" else 0
    print(f"Change           :          RM {change:>7.2f}")
    print("=" * 45)
    print("        Thank you for shopping with us!")
    print("           Website: www.alyaqeen.com")
    print("           Phone: +60 3-8312 5000")
    print("=" * 45 + "\n")
