def unit_conversion(number, source, destination, selected_unit):

    base_value = number * selected_unit[source]
    result = base_value / selected_unit[destination]

    return result


def temperature_conversion(number, source, destination):

    if source == "c":
        celsius = number

    elif source == "f":
        celsius = (number - 32) * 5 / 9

    else:
        celsius = number - 273.15

    if destination == "c":
        result = celsius

    elif destination == "f":
        result = (celsius * 9 / 5) + 32

    else:
        result = celsius + 273.15

    return result


length_unit = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "miles": 1609.344
}

weight_unit = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1,
    "tonne": 1000,
    "pound": 0.45359237
}

temperature_unit = {
    "c": "Celsius",
    "f": "Fahrenheit",
    "k": "Kelvin"
}

time_unit = {
    "milliseconds": 0.001,
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400
}


while True:

    print("\n========== UNIT CONVERTER ==========")

    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("0. Exit")

    choice = input("\nSelect a conversion category: ").strip()

    if choice == "1":
        selected_unit = length_unit

    elif choice == "2":
        selected_unit = weight_unit

    elif choice == "3":
        selected_unit = temperature_unit

    elif choice == "4":
        selected_unit = time_unit

    elif choice == "0":
        print("Thank you for using Unit Converter!")
        break

    else:
        print("Invalid choice. Select 1 to 4.")
        continue


    while True:

        number_input = input(
            "\nEnter the value and its unit (e.g. 4 km): "
        ).strip().lower()

        try:
            number, source_unit = number_input.split()
            number = float(number)

            if source_unit in selected_unit:
                break

            print("Unit not supported in this category!")

        except ValueError:
            print("Invalid input! Please enter in the format: 4 km")


    while True:

        destination_unit = input(
            "Which unit would you like to convert it into? "
        ).lower().strip()

        if destination_unit in selected_unit:
            break

        print("Unit not supported in this category!")


    if choice == "3":

        result = temperature_conversion(
            number,
            source_unit,
            destination_unit
        )

    else:

        result = unit_conversion(
            number,
            source_unit,
            destination_unit,
            selected_unit
        )


    print(
        f"\n{number} {source_unit} = "
        f"{result :.2f} {destination_unit}"
    )


    again = input(
        "\nWould you like to perform another conversion? (yes/no): "
    ).strip().lower()

    if again != "yes":
        print("\nThank you for using Unit Converter!")
        break
