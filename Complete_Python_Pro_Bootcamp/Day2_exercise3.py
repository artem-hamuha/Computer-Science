# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_ = 90
# 12 months in a year, 365 days and 52 weeks in a year
years_left = max_ - age
months = years_left * 12
weeks = years_left * 52
days = years_left * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")