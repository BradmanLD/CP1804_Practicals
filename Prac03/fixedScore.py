def main():
    score = float(input("Enter score (must be between 1 and 100): "))
    while score < 0 or score > 100:
        score = float(input("Invalid Input, Enter score (must be between 1 and 100): "))
    score_range = get_score_range(score)
    print(score_range)


def get_score_range(grade):
    if grade >= 90:
        return "Excellent"
    elif grade >= 50:
        return "Passable"
    else:
        return "Bad"

main()
