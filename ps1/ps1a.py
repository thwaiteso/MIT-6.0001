# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 21:05:28 2019

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