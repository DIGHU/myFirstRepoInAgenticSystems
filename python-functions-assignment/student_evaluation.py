def greet_student(name):
    return f"Hello, {name}"

def calculate_average(scores):
    total_subjects = len(scores)
    average_score = sum(scores) / total_subjects
    return total_subjects, average_score

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = "Dirghayush"
    scores = [75, 80, 85]

    greeting = greet_student(name)
    subjects, average = calculate_average(scores)
    result = evaluate_result(average)

    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", result)

if __name__ == "__main__":
    main()
