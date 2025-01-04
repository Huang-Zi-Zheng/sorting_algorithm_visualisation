#input()
# Control + Command + Space + 0178 for super script
# Exercise 2

item = str( input (" What item would you like to buy: ") )
price = float( input(" What is the price: "))
quantity =  int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"The total is : ${total} ")