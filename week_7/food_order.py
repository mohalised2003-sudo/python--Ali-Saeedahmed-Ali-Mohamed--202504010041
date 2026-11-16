def calculate_total(price, quantity):
    # Validate price and quantity inputs
    if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
        return "invalid price"
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        return "invalid quantity"

    total = price * quantity
    return total
