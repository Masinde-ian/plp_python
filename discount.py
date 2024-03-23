def calculate_discount(a,b):
    if b > 0:
        discount= b/100 * a
        new_price = a - discount
        return new_price
    else:
        new_price = a
        return new_price

a = int(input("Enter The Price: "))
b = int(input("Enter the percentage discount: "))
price = calculate_discount(a,b)
print('The new price is,',price)
