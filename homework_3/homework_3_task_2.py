import random

def get_numbers_ticket(min, max, quantity):
    if (min < 1) or (max > 1000) or (min > max) or (quantity > (max - min + 1)):
        return []
    uniq_numbers = random.sample(range(min, max+1), quantity)
    return sorted(uniq_numbers)
numbers_print = get_numbers_ticket(2
                                   , 999, 5)
print(f"Ваші лотерейні числа: {numbers_print}")