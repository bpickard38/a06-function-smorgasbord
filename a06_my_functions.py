# Name: Brayden Pickard
# These are all the functions

def sum_two_numbers(a, b):
    sum = a + b
    return sum
#this sums numbers
def is_even(num):
    result = num % 2 == 0
    return result
    
def get_number_parity(num):
    if is_even(num) == True:
        return f"{num} is even"
    else:
        return f"{num} is odd"

def fahrenheit_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * (5/9)
    return C
#this converts fahrenheit to celsius
def min_max_mean(numbers_list):
    min_num = min(numbers_list)
    max_num = max(numbers_list)
    mean = sum(numbers_list) / len(numbers_list)
    return [min_num, max_num, mean]

def dog_message(name, age=0):
    return f"I am a dog named {name} and I'm {age} years old!"

def classify_age(age, senior_age=65):
    if age <18:
        return "Minor"
    elif age < senior_age:
        return "Adult"
    else:
        return "Senior"
#dog messages
def calculate_total(price, quantity, discount_percent= .1, threshold_total=100, bonus_discount=.02):
    total_price = price * quantity
    if total_price <= threshold_total:
        grand_total = total_price * (1- discount_percent)
        return round(grand_total, 2)
    elif total_price > threshold_total:
        grand_total = total_price * (1-(discount_percent+ bonus_discount))
        return round(grand_total, 2)
