def check_temperature(temp_str):
    try:
        temperature = int(temp_str)
        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temperature}°C is perfect for plants!\n")

    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    value_test = ["25", "abc", 100, -50]

    for value in value_test:
        print(f"Testing temperature: {value}")
        check_temperature(value)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
