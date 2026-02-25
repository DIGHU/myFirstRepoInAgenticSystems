def calculate_average(users):
    averages = []
    for user in users:
        avg = sum(user["scores"]) / len(user["scores"])
        averages.append((user["name"], avg))
    return averages


def check_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Dirghayush",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "OM",
            "scores": [70, 75, 65],
            "roles": {"viewer"}
        }
    ]

    averages = calculate_average(users)

    for name, avg in averages:
        print("Name:", name)
        print("Average Score:", avg)

        for user in users:
            if user["name"] == name:
                admin_status = check_admin_access(user["roles"])
                print("Admin Access:", admin_status)
                print()
                

if __name__ == "__main__":
    main()
