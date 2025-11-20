price = (input("Enter The Price:"))
pay = int(input("Enter The Payed Amount: "))
def balance(pay, price):
    return (pay-price)

print("The Due Amount is:", balance(pay, price))


