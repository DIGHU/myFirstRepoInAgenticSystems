name = input("Enter your name: ")
age = int(input("Enter your age: "))
active_status = input("Are you an active user (True/False): ")

is_active = active_status == "True"

print(f"User {name} is {age} years old. Active status: {is_active}")
