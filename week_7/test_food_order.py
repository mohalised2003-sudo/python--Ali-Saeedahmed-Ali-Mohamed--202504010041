from food_order import calculate_total as food_order


def test_order1():
    assert food_order(10, 2) == 20


# test if total food order is equal to 30
def test_order2():
    assert food_order(15, 2) == 30


# test if total food order is equal to 100
def test_order3():
    assert food_order(25, 4) == 100


# test if total food order is equal to 10
def test_order4():
    assert food_order(5, 2) == 10


# test if total food order is equal to "invalid price"
def test_invalid_price():
    assert food_order(-5, 2) == "invalid price"


# test if total food order is equal to "invalid quantity"
def test_invalid_quantity():
    assert food_order(10, -2) == "invalid quantity"
