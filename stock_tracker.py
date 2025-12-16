stock_price = {"AAPL":180, "TSLA":250}
total = 0
user_investments = []

while(True):
    stock_name = input("Enter the stock name: ").upper()
    
    if stock_name not in stock_price:
        print("This stock is not available")
        continue

    stock_quantity = int(input("Enter the stock quantity: "))

    if stock_quantity <= 0:
        print("This quantity is invalid")
        continue
    
    price = stock_price[stock_name]
    investment_value = price * stock_quantity

    total += investment_value

    user_investments.append((stock_name,price,stock_quantity,investment_value))
    
    add_stock = input("Do you want to add another stock(y/n): ").lower()
    if add_stock == "n":
        break
    
for stock in user_investments:
    print("Stock: ",stock[0], "\n Price: ",stock[1], "\n Quantity: ",stock[2], "\n Value: ",stock[3])
    
print("Total Investment: ", total)

add_to_file = input("Do you want to save results in a file(y/n): ").lower()
if add_to_file == "y":
    file_type = input("Do you want a csv or a txt file(csv\txt): ").lower()
    if file_type == "txt":
        f = open("results.txt","w")
        for stock in user_investments:
            f.write(f"{stock[0]} {stock[1]} {stock[2]} {stock[3]}\n")
        f.write(f"Total Investment: {total}")
        f.close()
    else:
        f = open("results.csv","w")
        f.write("Stock,Price,Quantity,Value\n")
        for stock in user_investments:
            f.write(f"{stock[0]} {stock[1]} {stock[2]} {stock[3]}\n")
        f.write(f"Total Investment: {total}")
        f.close()
else:
    print("skip file saving...")

print("Complete!")