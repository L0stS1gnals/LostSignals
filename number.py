num = int(input("Enter a number: "))
if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"
square = num ** 2
cube = num ** 3
print("\nResults:")
print("Number:", num)
print("Even/Odd:", parity)
print("Positive/Negative:", sign)
print("Square:", square)
print("Cube:", cube)
