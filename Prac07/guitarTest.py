from Prac07.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if name.strip() == "":
            break
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))

    # gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    # test_guitar_one = Guitar("Name", 1950, 2004.23)
    # test_guitar_two = Guitar("TestName", 2004, 200.3003)

    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""

        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}"
              .format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

    # for guitar in guitars:
    #     if guitar.is_vintage():
    #         print(guitar.name + " is vintage")
    #     else:
    #         print(guitar.name + " is not vintage")

    # print(gibson)


main()
