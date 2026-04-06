with open("numbers.txt", "r") as file:
    print("File opened successfully")
    numbers = []

    for line in file:
        line = line.strip()   # remove whitespace
        if line:
            numbers.append(int(line))

total_count = len(numbers)
total_sum = sum(numbers)
average = total_sum / total_count

with open("results.log", "a") as log:
    log.write("File opened successfully\n")
    log.write(f"Read {total_count} numbers\n")
    log.write(f"Sum: {total_sum}\n")
    log.write(f"Average: {average}\n")
    log.write("Processing completed\n\n")

print("Processing completed. Check results.log")
