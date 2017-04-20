from Prac07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    test_guitar_one = Guitar("Name", 1950, 2004.23)
    test_guitar_two = Guitar("TestName", 2004, 200.3003)

    guitars = [gibson, test_guitar_one, test_guitar_two]
    for guitar in guitars:
        if guitar.is_vintage():
            print(guitar.name + " is vintage")
        else:
            print(guitar.name + " is not vintage")

    print(gibson)


main()