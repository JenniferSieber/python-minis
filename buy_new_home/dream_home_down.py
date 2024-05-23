"""
        Dream Home Goals
            Based on cost of home and yearly salary,
            set your down payment and savings goals.
            Receive details on how long it will take
            to reach your goals.
"""

def get_calculations() :
    # USER INPUTS
    print('')
    # Get housing info
    house_cost = float(input('What is the price of your dream home? $ '))
    #down_payment = cost_of_dream_home * 0.25
    down_payment_perc = float(input('What percentage would you like to put down on your dream house? % '))

    down_payment = house_cost * (down_payment_perc / 100)

    # Get salary info and savings goals
    yearly_salary = float(input('\nWhat is your yearly salary? $ '))
    save_rate_perc = float(input('What percentage of your salary do you want to save? % '))
    save_rate = (save_rate_perc / 100)
    monthly_save_amt = (yearly_salary * save_rate) / 12
    raise_rate_perc = float(input('\nEnter your semi-annual raise percentage.  '))
    semi_annual_raise = (raise_rate_perc / 100)

    # Constants
    annual_interest_rate = 0.05
    monthly_interest_rate = annual_interest_rate / 12
    semi_annual = semi_annual_raise
    print(f'Starting monthly deposit: ${monthly_save_amt:.2f}')

    total_savings = 0
    month_ct = 0

    while total_savings < down_payment:
        total_savings += total_savings * monthly_interest_rate
        total_savings += monthly_save_amt
        month_ct += 1

        if month_ct % 6 == 0 :
            monthly_save_amt += monthly_save_amt * semi_annual


    # Output the results
    print(f'\nCost of dream home: ${house_cost:.2f} with a down payment of: ${down_payment:.2f}')
    
    print(f'Time to reach your deposit goal: {month_ct} months or {(month_ct/12):.2f} years.')
    print(f'\nYour ending monthly deposit: ${monthly_save_amt:.2f}')
    print('')
    start()

def start() :
    print()
    print('Welcome to Dreaming Home Savings \n')
    calculate = input('Do you want to start the calculations for your down payment? (y/n)  ').lower()
    if calculate == 'y' :
        get_calculations()
    else :
        print('Thank you for visiting! \n')

start()