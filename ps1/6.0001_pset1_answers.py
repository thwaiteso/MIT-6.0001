# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:46:57 2019

@author: Ollie
"""

# These are my answers to Problem Set 1, on the MIT course
# Introduction to Computer Science and Programming in Python (6.0001)
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf


# Part A
# Write a program to calculate how many months it will take you to save up 
# enough money for a downpayment.
# It is assumed that you invest your current savings wisely, 
# with an annual return of 4%.
annual_salary = float(input('What is your annual salary?: '))
portion_saved = float(input('How much of your salary will be saved, as a decimal: '))
total_cost = float(input('What is the cost of your dream house?: '))
portion_down_payment = 0.25 * total_cost # downpayment assumed to be 25%
monthly_saved_salary = (portion_saved * annual_salary) / 12
# portion_saved is the amount you want to save in a year, from your annual salary
# therefore, the amount you save monthly is that amount divided by 12
current_savings = 0
num_months = 0
while portion_down_payment >= current_savings:
    monthly_return = current_savings * 0.04 / 12 # ROI of 4% a year, so / 12
    current_savings += (monthly_return + monthly_saved_salary)
    # add monthly return from investment and monthly saved salary to savings
    num_months += 1
# loop keeps going until savings exceed downpayment
print('Number of months =', num_months)
print('It will take you', num_months, 'months to raise', portion_down_payment,
      'for your dream house')


# Part B
# Write a program to calculate how many months it will take you to save up 
# enough money for a downpayment, accounting for a payrise every 6 months.
# It is assumed that you invest your current savings wisely, 
# with an annual return of 4%.
annual_salary = float(input('What is your annual salary?: '))
portion_saved = float(input('How much of your salary will be saved, as a decimal: '))
total_cost = float(input('What is the cost of your dream house?: '))
semi_annual_raise = float(input('How much will your salary increase every 6 months, as a decimal?: '))
portion_down_payment = 0.25 * total_cost
monthly_saved_salary = (portion_saved * annual_salary) / 12
current_savings = 0
num_months = 0
while portion_down_payment >= current_savings:
       monthly_return = current_savings * 0.04 / 12
       current_savings += (monthly_return + monthly_saved_salary)
       num_months += 1
       if num_months % 6 == 0: # raise kicks in after every 6th month, 
           # hence the remainder must equal 0 (e.g 24 % 6 = 0)
         annual_salary += semi_annual_raise * annual_salary
           # if 6 months have passed, add the raise to annual salary
         monthly_saved_salary = (portion_saved * annual_salary) / 12
           # update monthly saved salary 
print('Number of months =', num_months)
print('It will take you', num_months, 'months to raise', portion_down_payment,
      'for your dream house')


# Part C
# You are now going to try to find the best rate of savings to achieve 
# a down payment on a $1M house in 36 months. 
# Since hitting this exactly is a challenge, we simply want your savings 
# to be within $100 of the required down payment.
# Assumptions:
# Your semi­annual raise is .07 (7%)
# Your investments have an annual return of 0.04 (4%)
# The down payment is 0.25 (25%) of the cost of the house 
# The cost of the house that you are saving for is $1M
user_salary = float(input('What is your annual salary?: '))
annual_salary = user_salary
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = 0.25 * total_cost
current_savings = 0
epsilon = 100 # want to be within $100
num_guesses = 0
low = 0
high = 10000 # 10000 is 100.00% as we want to be within two decimal places

while True:
    save_rate = (low + high) / 2
    annual_salary = user_salary
    current_savings = 0
    for months in range(0, 36): # must be within 36 months
        monthly_salary = annual_salary / 12
        current_savings = current_savings + float((monthly_salary * (save_rate / 10000)))
        + current_savings * (0.04 / 12) # take any current savings, add the
        # monthly savings from salary and then add the ROI from current savings
        if months % 6 == 0: # if 6 months have passed
            annual_salary += semi_annual_raise * annual_salary # add the raise
    if abs(current_savings - portion_down_payment) <= epsilon:
        # if savings exceed downpayment and is within $100
        print('Best saving rate:', (save_rate / 10000), '%')
        print('Step in binary search:', num_guesses)
        print('Difference between downpayment and savings is:', (portion_down_payment - current_savings))
        break
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
        # if savings are greater than downpayment, but savings are not within
        # $100 of downpayment
        high = save_rate
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
        # if savings are less than downpayment and savings are not within
        # $100 of downpayment
        low = save_rate
    if low == high:
        # the rate will not chang if low == high, therefore print...
        print('It is not possible to pay the down payment in three years.')
        break
    num_guesses = num_guesses + 1

# Help needed for part c, using:
# https://github.com/tuthang102/MIT-6.0001-Intro-to-CS/blob/master/ps1/ps1c.py
# for inspiration.








    