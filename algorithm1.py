num1 = input("Binary number - ")

list = []

def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
        list.append(num % 2)
    

DecimalToBinary(int(num1))

print(*list, sep=" ")