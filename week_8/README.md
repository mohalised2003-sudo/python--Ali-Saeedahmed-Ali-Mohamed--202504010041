# Week 8 - Tutorial 8: Food Delivery System

## 1. Purpose of the Application
This application is a modular backend receipt generator for a Food Delivery System. It separates responsibilities into different modules (`customer.py`, `receipt.py`, and `main.py`) to collect customer order details, calculate item subtotals, add a 5% service charge and RM 5.00 delivery fee (if requested), and print a formatted receipt.

## 2. Tech Stack
* **Language:** Python 3
* **Version Control:** GitHub

## 3. How to Use
1. Open the terminal and navigate to the `week_8` directory:
   ```bash
   cd week_8
  1 Run the main program:
  python main.py
  2 Enter the customer name, food item (Cake or Muffin), quantity, price per item, and delivery choice (Y/N) to generate the receipt.
