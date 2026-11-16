# Tutorial 3: Cafe Bill Calculator

## 1 Problem Analysis

### a) Define the Problem Statement
A small cafe currently calculates customer bills manually, which is slow and prone to calculation errors. The goal is to build a Python program that automatically calculates the total bill based on the quantities of Coffee (RM 8.50), Tea (RM 6.00), and Sandwich (RM 12.00) ordered by a customer, and prints a formatted receipt.

### b) What are the Inputs?
* `customer_name`: Name of the customer (String).
* `coffee`: Quantity of coffee ordered (Integer).
* `tea`: Quantity of tea ordered (Integer).
* `sandwich`: Quantity of sandwich ordered (Integer).

### c) What are the Outputs?
* A formatted receipt displaying:
  * Customer name
  * Quantity of each item ordered (`Coffee`, `Tea`, `Sandwich`)
  * Final calculated bill amount in RM (`Total = RM XX.XX`)

### d) What would be the Typical Process Flow?
1. Prompt the user (cashier) to enter the customer's name and the quantities for Coffee, Tea, and Sandwich.
2. Multiply each item's quantity by its fixed unit price (`8.50`, `6.00`, `12.00`) and sum them up to get the `total`.
3. Format and display the receipt with all order details and the total bill.

### e) What are the Constraints?
* Fixed menu prices: Coffee = RM 8.50, Tea = RM 6.00, Sandwich = RM 12.00.
* Item quantities must be non-negative whole numbers (integers).
* The total price must be displayed formatted to two decimal places (RM).
* Logic functions (`calculate_total` and `print_receipt`) must be separated in `utils.py` and imported into `main.py`.

---

## 2 Problem Decomposition (Smaller Tasks)
The program is decomposed into three modular tasks across two files:
1. **Input Collection (`main.py`):** Gather customer name and item quantities from the cashier.
2. **Bill Calculation (`utils.py` -> `calculate_total`):** Compute the total cost using the item quantities and fixed menu prices.
3. **Receipt Generation (`utils.py` -> `print_receipt`):** Format and print the customer receipt clearly on the screen.

---

## 3 Pseudocode

```text
START
    INPUT customer_name
    INPUT coffee
    INPUT tea
    INPUT sandwich

    SET total = (coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)

    OUTPUT "===== RECEIPT ====="
    OUTPUT "Customer : ", customer_name
    OUTPUT "Coffee   : ", coffee
    OUTPUT "Tea      : ", tea
    OUTPUT "Sandwich : ", sandwich
    OUTPUT "Total = RM ", total
    OUTPUT "==================="
END
