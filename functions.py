def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
      """ checks if the Percentage discount Is Greater than 20% 
          calculates the discount amount the returs the Fnal price less discount
      """
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if final_price != original_price:
    print("Final price after applying discount:", final_price)
else:
    print("No discount applied. Final price:", final_price)
