from functools import reduce
from typing import Callable
import re

def generator_numbers(text: str):
    words=text.split(' ')
    numbers=map(float,filter(lambda x: re.match(r'\d+\.\d+',x),words))
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
    sum=0
    for number in func(text):
        sum+=number
    return sum
 
if __name__=='__main__':

    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")