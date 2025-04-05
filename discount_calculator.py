# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and store the result
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
print(f"The final price is: {final_price}")
