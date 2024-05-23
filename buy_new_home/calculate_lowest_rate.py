"""
        Dream Home Savings in 3 years
            Set your goals:
            Give your initial deposit.
            Find the lowest rate that will 
            get you to your goal within 3 years.
"""

# Calculate Compound Interest
def compute_compound_interest(initial_deposit, annual_rate, months):
    monthly_rate = annual_rate / 12
    amount = initial_deposit * (1 + monthly_rate) ** months
    return 

# Calculate min rate - bisection search
months = 36
tolerance = 100
def find_min_rate(initial_deposit, target_amount, months=36, tolerance=100) :
    low = 0
    high = 1
    mid = (high + low) / 2.0
    count = 0

    while True :
        count += 1
        mid = (high + low) / 2.0
        savings = compute_compound_interest(initial_deposit, mid, months)

        if abs(savings - target_amount) <= tolerance :
            # print(f'Steps in bisection search: {count}')
            return mid
        elif savings < target_amount :
            low = mid
        else :
            high = mid
       
        if high - low < 1e-6 :
            # print(f'Steps in bisection search: {count}')
            return mid

def get_calculations() :
    # Get house cost User Inputs
    house_cost = float(input('What is the cost of your dream home?  $ '))
    down_payment_perc = float(input('What percentage would you like to put down on your dream house?  %  '))
    down_payment = house_cost * (down_payment_perc / 100)
    print(f'Your {down_payment_perc}% Down Payment is: ${down_payment:.2f} for house price of ${house_cost:.2f}')
    initial_deposit = float(input("Enter the initial deposit in your savings account: $ "))

    # Constants 
    months = 36
    tolerance = 100


    # Calculate the minimum rate of return needed
    dep_dif = down_payment - initial_deposit
    if int(dep_dif) <= 100 :
        print('Best savings rate: None')
        #print('Steps in bisection search: 0')
    else :
        min_rate = find_min_rate(initial_deposit, down_payment, months, tolerance)
        print(f"The minimum rate of return needed to save for the down payment in 3 years is: {min_rate * 100:.2f}% ")
    
    start()


def start() :
    print()
    print('Welcome to Dreaming Home Savings \n')
    calculate = input('Do you want to start the calculations for your savings? (y/n)  ').lower()
    if calculate == 'y' :
        get_calculations()
    else :
        print('Thank you for visiting! \n')

start()

