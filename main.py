from texts import START_MESSAGE
from scenarios.scenarios import scenarios_dict


def main():

    while True:

        try:
            number = int(input(START_MESSAGE))
        except ValueError:
            print("Введите число!")
            continue

        scenario = scenarios_dict.get(number)

        if not scenario:
            print("Введите число от 1 до 4!")
            continue

        print()

        scenario()

        input("Нажмите Enter для продолжения")


if __name__ == "__main__":
    main()