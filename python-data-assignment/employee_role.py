# Tuple: (id, name, department)
employee = (101, "Rahul", "IT")
roles = {"editor", "viewer", "admin"}

print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
