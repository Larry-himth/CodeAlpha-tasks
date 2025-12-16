# dictionary to hold stock names and their prices
stock_price = {"AAPL":180, "TSLA":250}

# variable to keep track of total investment
total = 0

# list to store details of each stock investment
user_investments = []

while(True):
    # ask user for stock name
    stock_name = input("Enter the stock name: ").upper()
    
    # check if the stock name exists in the dictionary
    if stock_name not in stock_price:
        print("This stock is not available")
        continue

    # ask user for the quantity of the stock
    stock_quantity = int(input("Enter the stock quantity: "))

    # validate the quantity
    if stock_quantity <= 0:
        print("This quantity is invalid")
        continue
    
    # get the price of the selected stock
    price = stock_price[stock_name]
    # calculate the investment value of the stock
    investment_value = price * stock_quantity

    # add the investment value to the total investment
    total += investment_value

    # store the stock investment details in the user investments list
    user_investments.append((stock_name,price,stock_quantity,investment_value))
    
    # ask user if they want to add another stock 
    add_stock = input("Do you want to add another stock(y/n): ").lower()
    if add_stock == "n":
        break
    
# display all stored stock investments
for stock in user_investments:
    print("Stock: ",stock[0], "\n Price: ",stock[1], "\n Quantity: ",stock[2], "\n Value: ",stock[3])
    
# display the total investment value
print("Total Investment: ", total)

# ask the usser if they want to save the results in a file
add_to_file = input("Do you want to save results in a file(y/n): ").lower()
if add_to_file == "y":
    
    # ask the user which type of file they want
    file_type = input("Do you want a csv or a txt file(csv\txt): ").lower()
    
    # save results to a txt file
    if file_type == "txt":
        f = open("results.txt","w")
        for stock in user_investments:
            f.write(f"{stock[0]} {stock[1]} {stock[2]} {stock[3]}\n")
        f.write(f"Total Investment: {total}")
        f.close()
        
    else:
        # save results to a csv file
        f = open("results.csv","w")
        f.write("Stock,Price,Quantity,Value\n")
        for stock in user_investments:
            f.write(f"{stock[0]} {stock[1]} {stock[2]} {stock[3]}\n")
        f.write(f"Total Investment: {total}")
        f.close()
else:
    print("skip file saving...")

print("Complete!")