# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = name1 + name2
combined_names = combined_names.lower()

total_true = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")

total_love = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

total = str(total_true) + str(total_love)
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and  total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")