def main():
    score = float(input("Enter score (must be between 1 and 100): "))
    while score < 0 or score > 100:
        score = float(input("Invalid Input, Enter score (must be between 1 and 100): "))
    grade = determine_grade(score)
    print(grade)


def determine_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
