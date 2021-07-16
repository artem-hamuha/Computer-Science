num1 = input("Binary number - ")


def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print(num % 2)

DecimalToBinary(int(num1))