# Name: Brayden Pickard
# Enter your python code below. In this file, you will call all of the
# functions that you defined in your my_functions.py file.

import a06_my_functions

def welcome_message(name):
    print(f"Hello {name}, welcome to IS 303!")

welcome_message("Diego")
welcome_message("Mai")

print(a06_my_functions.sum_two_numbers(5, 7))
print(a06_my_functions.sum_two_numbers(1000.5, -30))

print(a06_my_functions.is_even(7))
print(a06_my_functions.is_even(120))

print(a06_my_functions.get_number_parity(5))
print(a06_my_functions.get_number_parity(10))

print(a06_my_functions.fahrenheit_to_celsius(32))
print(a06_my_functions.fahrenheit_to_celsius(75))

#calls these functions
numbers_list_1 = [20, 45, 23, 2, 87, 3]
print(a06_my_functions.min_max_mean(numbers_list_1))

print(a06_my_functions.dog_message("Spot", 7))
print(a06_my_functions.dog_message("Peppy"))
print(a06_my_functions.classify_age(60, 55))
print(a06_my_functions.classify_age(62))

for _ in range(2):
    price = float(input("Enter the price for the product purchased: "))
    quantity = int(input("Enter the quantity of the product purchased: "))
    discount_percent = float(input("Enter the discount percent (formatted as a decimal): "))
    total2 = a06_my_functions.calculate_total(price, quantity, discount_percent)
    print(f"The total price after discounts is: ${total2}")

#this are the inputs