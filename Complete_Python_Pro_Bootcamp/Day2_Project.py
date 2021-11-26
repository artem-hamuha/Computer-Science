print('The Tip Calculator welcomes you')
bill = float(input('What was the total bill? '))
tip_percent = float(input('What percent of the tip would you like to give? The tip can be anything more or equal to 0. '))
people = int(input('How many people are paying. '))

total = bill + bill * (tip_percent / 100)
each_pay = total / people

print(f'The total is: {round(total, 2)}. Each person will pay: {round(each_pay, 2)}')
