age = int(input("Enter your age:"))
id_input = input("Do you have id card(True/False):")
has_id = id_input.lower()== "true"
if age >=18 and has_id:
    print("entry allowed")
else:
    print("entry denied")