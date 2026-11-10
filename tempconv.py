
def temperature_converter():
    while True:
        print("\n===== TEMPERATURE CONVERTER =====")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        print("4. Rankine")
        print("5. Exit")

        choice = input("\nSelect option: ")

        if choice == "5":
            print("Thank you for using Temperature Converter!")
            break

        units = {
            "1": "Celsius",
            "2": "Fahrenheit",
            "3": "Kelvin",
            "4": "Rankine"
        }

        if choice not in units:
            print("Invalid choice! Try again.")
            continue

        source = units[choice]

        try:
            value = float(input(f"Enter temperature in {source}: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        celsius = {
            "Celsius": value,
            "Fahrenheit": (value - 32) * 5 / 9,
            "Kelvin": value - 273.15,
            "Rankine": (value - 491.67) * 5 / 9
        }[source]

        if celsius < -273.15:
            print("Error: Temperature cannot be below absolute zero!")
            continue

        conversions = {
            "Celsius": celsius,
            "Fahrenheit": (celsius * 9 / 5) + 32,
            "Kelvin": celsius + 273.15,
            "Rankine": (celsius + 273.15) * 9 / 5
        }

        print("\n===== CONVERSION RESULTS =====")

        for unit, result in conversions.items():
            if unit != source:
                print(f"{unit}: {result:.2f}")

        print("\n1. Convert again")
        print("2. Exit")

        again = input("Select option: ")

        if again == "2":
            print("Goodbye!")
            break


temperature_converter()
