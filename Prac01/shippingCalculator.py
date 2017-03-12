item_cost_list = []
number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Invalid number of items, please try again.")
    number_of_items = int(input("Enter the number of items: "))
for i in range(0, number_of_items):
    item_cost = input("Enter the price of item " + str(i + 1) + ": ")
    item_cost_list.append(int(item_cost))
total_cost = sum(item_cost_list)
if total_cost >= 100:
    total_cost *= 0.90
print("Total price for " +(str(number_of_items) + " is: $" + str(total_cost)))