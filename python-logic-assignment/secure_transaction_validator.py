balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Is the user verified (True/False): ")

is_verified = verified_input.lower() == "true"

if is_verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
