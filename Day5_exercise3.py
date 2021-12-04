#Write your code below this row 👇
even = []
for i in range(0, 101):
    if i % 2 == 0:
        even.append(i)

total = 0
for i in even:
    total += i

print(total)