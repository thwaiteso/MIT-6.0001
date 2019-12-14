# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 21:06:37 2019

@author: Ollie
"""

# These are my answers to Problem Set 1, on the MIT course
# Introduction to Computer Science and Programming in Python (6.0001)
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf

# Part B
# Write a program to calculate how many months it will take you to save up 
# enough money for a downpayment, accounting for a payrise every 6 months.
# It is assumed that you invest your current savings wisely, 
# with an annual return of 4%.
annual_salary = float(input('What is your annual salary?: '))
portion_saved = float(input('How much of your salary will be saved, as a decimal: '))
total_cost = float(input('What is the cost of your dream house?: '))
semi_annual_raise = float(input('How much will your salary increase every 6 months, as a decimal?: '))
portion_down_payment = 0.25 * total_cost # 25% of house cost
monthly_saved_salary = (portion_saved * annual_salary) / 12
current_savings = 0
num_months = 0
while portion_down_payment >= current_savings: # while down payment is greater
    # than the current savings
       monthly_return = current_savings * 0.04 / 12 # the monthly return is
       # the annual return (of 4%) on the current savings, divided by 12
       current_savings += (monthly_return + monthly_saved_salary) # add monthly
       # return and monthly saved salary to current savings
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