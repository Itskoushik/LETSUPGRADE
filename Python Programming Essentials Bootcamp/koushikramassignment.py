principal_amount = float(input("Enter the principal amount: "))
num_of_years = float(input("Enter the number of years: "))
is_customer_female = input("Is the customer female? (yes/no): ").lower() == "yes"
is_customer_senior_citizen = input("Is the customer a senior citizen? (yes/no): ").lower() == "yes"

if is_customer_female and is_customer_senior_citizen:
    rate = 8
elif is_customer_female and not is_customer_senior_citizen:
    rate = 6
elif not is_customer_female and is_customer_senior_citizen:
    rate = 7
else:
    rate = 5

interest_amount = (principal_amount * rate * num_of_years) / 100

print("Simple Interest: ₹", interest_amount)
