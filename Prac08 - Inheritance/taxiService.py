from taxi import Taxi
from taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_bill = 0
    chosen_taxi = taxis[0]
    print("Let's Drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            chosen_taxi = get_taxi_choice(taxis)
            chosen_taxi.start_fare()

        if menu_choice == 'd':
            drive_taxi(chosen_taxi)
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, chosen_taxi.get_fare()))
            current_bill += chosen_taxi.get_fare()

        print("Bill to date: ${:.2f}".format(current_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()


def get_taxi_choice(taxis):
    display_taxis(taxis)
    taxi_choice = int(input(">>> "))
    chosen_taxi = taxis[taxi_choice]
    return chosen_taxi


def drive_taxi(taxi):
    distance = int(input("Drive how far? "))
    taxi.drive(distance)


def display_taxis(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
